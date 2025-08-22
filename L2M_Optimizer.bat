@echo off
title Lineage2M Enhancement Optimizer v2.1 - Now with Epic Drop Analysis!
color 0A

:check_python
cls
echo =========================================
echo    Lineage2M Enhancement Optimizer
echo         Tumbal Analysis System
echo =========================================
echo.
echo [*] Checking Python installation...

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [!] Python is not installed or not in PATH!
    echo.
    echo Please install Python 3.7 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [+] Python detected successfully
echo.

:run_optimizer
echo [*] Starting L2M Enhancement Optimizer...
echo.
python l2m_master_optimizer.py

if %errorlevel% neq 0 (
    echo.
    echo [!] Error running the optimizer
    echo.
    echo Possible solutions:
    echo 1. Make sure l2m_master_optimizer.py is in the same folder
    echo 2. Check if Python is properly installed
    echo 3. Try running as Administrator
    echo.
    pause
    exit /b 1
)

:end
echo.
echo Thank you for using L2M Enhancement Optimizer!
echo.
pause
exit /b 0