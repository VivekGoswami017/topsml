@echo off
title Push Frontend to GitHub
color 0b
echo ======================================================================
echo           Pushing Frontend to GitHub Repository
echo           Target: https://github.com/VivekGoswami017/Frontend
echo ======================================================================
echo.

cd /d "d:\Machine_Learning Class\student-pass-fail-app"

echo Checking Git status...
"C:\Users\govas\AppData\Local\GitHubDesktop\app-3.6.6\resources\app\git\cmd\git.exe" status

echo.
echo Pushing branch 'main' to origin...
echo (If a browser window opens, please click 'Sign in with your browser' / 'Authorize')
echo.

"C:\Users\govas\AppData\Local\GitHubDesktop\app-3.6.6\resources\app\git\cmd\git.exe" push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ======================================================================
    echo  [SUCCESS] All files from the frontend folder have been pushed!
    echo  View your repository online:
    echo  https://github.com/VivekGoswami017/Frontend
    echo ======================================================================
) else (
    echo.
    echo ======================================================================
    echo  [ERROR] Push did not complete. Please see the message above.
    echo ======================================================================
)

echo.
echo Press any key to close this window...
pause >nul
