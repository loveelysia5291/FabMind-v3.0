import base64

with open('C:/Users/USER/.gemini/antigravity/scratch/fabmind-system/index.html', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('ascii')

worker_code = f'''/**
 * =========================================================================
 * FabMind v3.0 - Cloudflare Worker 獨立運行檔案 (worker.js)
 * =========================================================================
 * 部署說明：
 * 1. 登入 Cloudflare 控制台 (https://dash.cloudflare.com)
 * 2. 點擊左側 [Workers & Pages] -> [Create application] -> [Create Worker]
 * 3. 點選 [Deploy] 後點 [Edit code] (編輯程式碼)
 * 4. 將本檔案全部代碼複製並直接覆蓋貼上，點擊 [Deploy] (部署)
 * 5. 即刻獲得全球 300+ 邊緣節點極速上線的專屬網址！
 * =========================================================================
 */

const HTML_BASE64 = "{b64}";

function getHtml() {{
  const binaryString = atob(HTML_BASE64);
  const bytes = Uint8Array.from(binaryString, c => c.charCodeAt(0));
  return new TextDecoder("utf-8").decode(bytes);
}}

const HTML_CONTENT = getHtml();

export default {{
  async fetch(request, env, ctx) {{
    const url = new URL(request.url);

    // API 健檢端點
    if (url.pathname === "/api/health") {{
      return new Response(JSON.stringify({{
        status: "healthy",
        system: "FabMind v3.0 HMI Console",
        runtime: "Cloudflare Workers Edge V8",
        timestamp: new Date().toISOString()
      }}), {{
        headers: {{
          "content-type": "application/json;charset=UTF-8",
          "access-control-allow-origin": "*"
        }}
      }});
    }}

    // 返回完整主控台頁面
    return new Response(HTML_CONTENT, {{
      headers: {{
        "content-type": "text/html;charset=UTF-8",
        "cache-control": "public, max-age=1800",
        "x-frame-options": "SAMEORIGIN",
        "x-content-type-options": "nosniff"
      }}
    }});
  }}
}};
'''

out_path = 'C:/Users/USER/.gemini/antigravity/scratch/fabmind-system/worker.js'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(worker_code)

print(f"Generated {out_path}, size: {len(worker_code)} chars")
