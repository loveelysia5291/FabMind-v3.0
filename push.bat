@echo off
chcp 65001 >nul
echo ===================================================
echo   FabMind v3.0 - 一鍵推送至 GitHub 遠端儲存庫
echo   目標倉庫: https://github.com/loveelysia5291/FabMind-v3.0.git
echo ===================================================
echo.

set "GIT_EXE=C:\Program Files\Microsoft Visual Studio\2022\Professional\Common7\IDE\CommonExtensions\Microsoft\TeamFoundation\Team Explorer\Git\cmd\git.exe"

if not exist "%GIT_EXE%" (
    set "GIT_EXE=git"
)

echo [1/3] 確認遠端 origin 設定...
"%GIT_EXE%" remote remove origin 2>nul
"%GIT_EXE%" remote add origin https://github.com/loveelysia5291/FabMind-v3.0.git

echo [2/3] 切換分支為 main...
"%GIT_EXE%" branch -M main

echo [3/3] 正在推送到 GitHub...
echo (若彈出 GitHub 登入視窗，請點選授權/登入)
"%GIT_EXE%" push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ===================================================
    echo   🎉 恭喜！FabMind 專案已成功推送到 GitHub！
    echo   倉庫網址: https://github.com/loveelysia5291/FabMind-v3.0
    echo ===================================================
) else (
    echo.
    echo [提示] 推送若中斷，請確認是否已在彈出的瀏覽器視窗中完成 GitHub 登入。
)

pause
