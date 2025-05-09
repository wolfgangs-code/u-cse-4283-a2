@echo off

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python to run this script.
    exit /b 1
)

python -u bmi_cli/cli.py %*