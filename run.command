#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

PYTHON_BIN=""
if command -v python3 >/dev/null 2>&1; then
	PYTHON_BIN="python3"
elif [[ -x "/usr/bin/python3" ]]; then
	PYTHON_BIN="/usr/bin/python3"
fi

if [[ -z "$PYTHON_BIN" ]]; then
	echo "Python 3 was not found on this Mac."
	echo "Install Python 3 (python.org) then double-click this file again."
	echo
	read -r -p "Press Enter to close..." _
	exit 1
fi

"$PYTHON_BIN" server.py --open
