@echo off
chcp 65001 >nul
echo ===================================================
echo   FabMind v3.0 - 一鍵部署至 Cloudflare Pages
echo ===================================================
echo.
echo 正在準備發布到 Cloudflare Pages (專案名稱: fabmind-v3)...
echo (若為初次使用，系統將自動開啟瀏覽器提示登入 Cloudflare 帳號)
echo.

call npx wrangler pages deploy . --project-name=fabmind-v3 --branch=main

if %errorlevel% equ 0 (
    echo.
    echo ===================================================
    echo   🎉 恭喜！FabMind v3.0 已成功部署至 Cloudflare Pages！
    echo   全網訪問網址預設為: https://fabmind-v3.pages.dev
    echo ===================================================
) else (
    echo.
    echo [提示] 若命令列中斷，您亦可登入 Cloudflare 控制台 (https://dash.cloudflare.com)
    echo 點擊 [Workers & Pages] ➔ [Create application] ➔ [Pages] ➔ [Connect to Git]
    echo 綁定 GitHub 倉庫 loveelysia5291/FabMind-v3 進行 100% 免手動全自動部署！
)

pause
