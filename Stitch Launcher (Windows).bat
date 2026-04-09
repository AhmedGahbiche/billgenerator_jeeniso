@echo off
setlocal

REM Stitch Launcher (Windows)
REM Double-click to start. Keep this window open while using the app.

cd /d "%~dp0"

set "OPEN_PATH=%~1"
if "%OPEN_PATH%"=="" set "OPEN_PATH=code.html"

where py >nul 2>nul
if %errorlevel%==0 (
	py -3 server.py --open "%OPEN_PATH%"
	exit /b %errorlevel%
)

where python >nul 2>nul
if %errorlevel%==0 (
	python server.py --open "%OPEN_PATH%"
	exit /b %errorlevel%
)

where python3 >nul 2>nul
if %errorlevel%==0 (
	python3 server.py --open "%OPEN_PATH%"
	exit /b %errorlevel%
)

echo Python is not installed (or not on PATH).
echo Please install Python 3 from https://www.python.org/downloads/windows/ or the Microsoft Store.
echo Then re-run this file.
pause
exit /b 1
