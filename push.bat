@echo off
chcp 65001 >nul
echo ===================================================
echo   FabMind v3.0 - 一鍵推送至遠端 Git 儲存庫
echo ===================================================
echo.

set "GIT_EXE=C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe"

if not exist "%GIT_EXE%" (
    set "GIT_EXE=git"
)

set /p REMOTE_URL="請貼上您的遠端 Git 倉庫網址 (例如 https://github.com/your-name/fabmind.git): "

if "%REMOTE_URL%"=="" (
    echo [錯誤] 遠端網址不可為空！
    pause
    exit /b 1
)

echo.
echo [1/3] 設定遠端 origin: %REMOTE_URL%
"%GIT_EXE%" remote remove origin 2>nul
"%GIT_EXE%" remote add origin %REMOTE_URL%

echo [2/3] 確認本地分支為 main...
"%GIT_EXE%" branch -M main

echo [3/3] 推送程式碼至遠端...
"%GIT_EXE%" push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ===================================================
    echo   恭喜！FabMind 專案已成功推送到遠端倉庫！
    echo ===================================================
) else (
    echo.
    echo [提示] 若推送失敗，請確認該倉庫是否已建立，或檢查 GitHub 存取權限 (Personal Access Token)。
)

pause
