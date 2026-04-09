#!/usr/bin/env python3
"""Local server + on-disk invoice storage.

- Serves this folder as static files.
- Persists invoices to ./data/invoices.json so they survive reboots and browser storage resets.

Run:
  python3 server.py
Optionally:
  PORT=5173 python3 server.py
  python3 server.py 5173
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import webbrowser
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler
from pathlib import Path
from socketserver import TCPServer
from typing import Any

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
INVOICES_PATH = DATA_DIR / "invoices.json"


def _read_json_file(path: Path, default: Any) -> Any:
    try:
        raw = path.read_text(encoding="utf-8")
        return json.loads(raw)
    except FileNotFoundError:
        return default
    except Exception:
        return default


def _atomic_write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


class Handler(SimpleHTTPRequestHandler):
    # Avoid caching during dev
    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def _send_json(self, status: int, payload: Any) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_request_json(self) -> Any:
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length <= 0:
            return None
        raw = self.rfile.read(length)
        try:
            return json.loads(raw.decode("utf-8"))
        except Exception:
            return None

    def do_GET(self) -> None:  # noqa: N802
        if self.path.rstrip("/") == "/api/invoices":
            data = _read_json_file(INVOICES_PATH, [])
            if not isinstance(data, list):
                data = []
            self._send_json(HTTPStatus.OK, data)
            return

        return super().do_GET()

    def do_PUT(self) -> None:  # noqa: N802
        if self.path.rstrip("/") == "/api/invoices":
            payload = self._read_request_json()
            if not isinstance(payload, list):
                self._send_json(HTTPStatus.BAD_REQUEST, {"error": "Expected a JSON array"})
                return

            # Basic sanitation: only keep JSON-serializable dicts
            safe: list[Any] = []
            for item in payload:
                if isinstance(item, dict):
                    safe.append(item)
            _atomic_write_json(INVOICES_PATH, safe)
            self._send_json(HTTPStatus.OK, {"ok": True, "count": len(safe)})
            return

        self._send_json(HTTPStatus.NOT_FOUND, {"error": "Not found"})


def _pick_port(start: int, tries: int = 20) -> int:
    for i in range(tries):
        port = start + i
        try:
            with TCPServer(("127.0.0.1", port), Handler) as httpd:
                # If we can bind, close immediately and reuse below.
                return port
        except OSError:
            continue
    raise RuntimeError(f"No free port found in range {start}-{start + tries - 1}")


def main() -> int:
    os.chdir(ROOT)

    parser = argparse.ArgumentParser(description="Serve the app and persist invoices to disk.")
    parser.add_argument(
        "port",
        nargs="?",
        type=int,
        help="Preferred port (will use the next free one if busy). You can also set PORT env var.",
    )
    parser.add_argument(
        "--open",
        nargs="?",
        const="code.html",
        default=None,
        metavar="PATH",
        help="Open PATH in the default browser once the server starts (default: code.html).",
    )
    args = parser.parse_args()

    port = args.port
    if port is None:
        env_port = os.environ.get("PORT")
        if env_port:
            try:
                port = int(env_port)
            except ValueError:
                port = None

    start_port = port if port is not None else 5173
    chosen = _pick_port(start_port)

    TCPServer.allow_reuse_address = True
    with TCPServer(("127.0.0.1", chosen), Handler) as httpd:
        base_url = f"http://localhost:{chosen}"
        print(f"Serving on {base_url} (data: {INVOICES_PATH.relative_to(ROOT)})")

        if args.open is not None:
            open_path = str(args.open).lstrip("/")
            url = f"{base_url}/{open_path}" if open_path else f"{base_url}/"
            try:
                webbrowser.open(url)
            except Exception:
                pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
