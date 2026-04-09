# Stitch Invoice App

## Easiest way to run (recommended)

If you’re sharing this with someone non-technical, use the platform launchers:

- macOS: double‑click **Stitch Launcher.app**
- Windows: double‑click **Stitch Launcher (Windows).bat**

### Option A — Terminal (1 command)

```bash
cd "$(dirname "$0")"  # or just `cd` into the stitch folder
python3 server.py --open
```

- This starts the local server **and opens** the app in your browser.
- It also enables disk persistence via `data/invoices.json`.

To open the archive directly:

```bash
python3 server.py --open archive.html
```

### Option B — VS Code Task (1 click)

- Open the Command Palette → **Tasks: Run Task**
- Run **“Stitch: Run server (opens browser)”**

### Option C — macOS double‑click

- One-time setup (in the stitch folder):

```bash
chmod +x run.command
```

- Then double‑click `run.command`.

Alternative (recommended for non-technical users): double‑click **Stitch Launcher.app**.

This will open a Terminal window and the browser. To stop the server, close the Terminal window.

If double‑click shows an error:

- **“could not be executed… appropriate access privileges” / “Permission denied” / doesn’t run**:
  - Open Terminal once and run:
    - `cd /path/to/stitch`
    - `chmod +x run.command`
- If you’re sharing this folder to another Mac: prefer **Finder → Compress** (zip) before sending, because some copy methods can remove the executable permission; if it happens, run `chmod +x run.command` again.
- **macOS blocks it (quarantine)**:
  - Right‑click `run.command` → **Open** (do this once)
- **Python not found**:
  - Install Python 3, then retry

### Option D — Windows double‑click (no VS Code, no Terminal)

- Recommended: Double‑click **Stitch Launcher (Windows).bat**
- Or: Double‑click `run_windows.bat`
- Keep the black window open while using the app (closing it stops the server)

Open the archive directly (optional):

```bat
run_windows.bat archive.html
```

If it says Python is not installed, install **Python 3** and try again.

## Note about `python -m http.server`

You _can_ run a static server, but it won’t save invoices to disk.
Use `python3 server.py` if you want invoices to persist across reboots.
