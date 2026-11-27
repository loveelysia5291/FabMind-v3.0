# FabMind v3.0 網上架設與部署指南 (Deployment Guide)

本系統為純靜態現代 Web 應用（支援自包含運行），不依賴龐大的伺服器維護，能以極高穩定度免費部署至全球各大雲端 CDN 與網頁代管平台。

---

## 方案一：Netlify Drop（推薦！最簡單，30 秒零代碼上線）

這是最快將 FabMind 放上公網供任何人點擊訪問的方法：

1. 打開瀏覽器，造訪 [https://app.netlify.com/drop](https://app.netlify.com/drop)。
2. 打開電腦中的檔案總管，定位到專案資料夾：  
   `C:\Users\USER\.gemini\antigravity\scratch\fabmind-system`
3. 將整個 `fabmind-system` 資料夾直接拖曳進瀏覽器中的 Netlify 虛線框中。
4. 上傳完成後，Netlify 會在 5 秒內為您產生一個全球可訪問的專屬網址（例如：`https://fabmind-v3.netlify.app`）。

---

## 方案二：Vercel 一鍵部署

本專案目錄內已為您預先配置好了 `vercel.json`。

### 方式 A：透過 GitHub 連動（自動更新）
1. 將此專案推送至您的 GitHub 帳號（如 `https://github.com/your-username/fabmind-system`）。
2. 前往 [Vercel](https://vercel.com/)，點選 **Add New Project**。
3. 匯入該 GitHub 儲存庫，點選 **Deploy**。
4. 部署完成後，Vercel 會提供專屬的 `.vercel.app` 網址，並具備自動 SSL 安全憑證。

---

## 方案三：GitHub Pages（團隊永久免費託管）

1. 在 GitHub 建立一個新的公開儲存庫（Repository），例如 `fabmind-v3`。
2. 在終端機進入專案目錄執行：
   ```bash
   git init
   git add .
   git commit -m "feat: initial commit of FabMind v3.0"
   git branch -M main
   git remote add origin https://github.com/<您的用戶名>/fabmind-v3.git
   git push -u origin main
   ```
3. 進入 GitHub 儲存庫頁面 -> **Settings** -> **Pages**。
4. 在 **Build and deployment** 下方的 Branch 選擇 `main` / `root`，點選 **Save**。
5. 稍等約 1 分鐘，即可在 `https://<您的用戶名>.github.io/fabmind-v3/` 線上存取。

---

## 方案四：即刻本機公網穿透（無需上傳代碼，立即展示給外部人員）

若您現在就需要給同事或主管臨時查看，且不想將代碼上傳到雲端：

1. 在本機終端機啟動伺服器：
   ```bash
   python server.py 8080
   ```
2. 開啟另一個終端機視窗，使用免安裝的公網穿透工具：
   ```bash
   npx localtunnel --port 8080
   ```
   或使用 Cloudflare 免費 Tunnel：
   ```bash
   npx trycloudflare --port 8080
   ```
3. 終端機會立即印出一個臨時的公網 URL（例如 `https://quick-fab-demo.loca.lt` 或 `https://xxxx.trycloudflare.com`），任何連上該網址的人都能立刻使用 FabMind 系統！
