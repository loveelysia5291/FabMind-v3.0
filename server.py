import http.server
import socketserver
import os
import sys
import json
import urllib.parse
import webbrowser

DEFAULT_PORTS = [3000, 8000, 8888, 5000, 9000]
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class FabMindHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        # 簡易健康檢查與機台狀態 API
        if parsed_path.path == '/api/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {
                "status": "ONLINE",
                "system": "FabMind v3.0",
                "mode": "Air-gapped Production Sandbox",
                "opa_policy": "STRICT_ENFORCEMENT",
                "active_tools": 10,
                "alarm_suppression_rate": 0.887,
                "mttr_reduction": 0.365
            }
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            return
            
        elif parsed_path.path == '/api/interlock-status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            interlock = {
                "chamber_id": "ETCH-03-A",
                "rf_power_state": "OFF_0W",
                "vacuum_pressure_mtorr": 0.024,
                "interlock_status": "LOCKED_SAFE",
                "toxic_gas_valves": "SHUT_ISOLATED"
            }
            self.wfile.write(json.dumps(interlock, ensure_ascii=False).encode('utf-8'))
            return

        # 預設回傳靜態網頁 (index.html)
        return super().do_GET()

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    
    # 決定優先測試的端口清單
    candidate_ports = []
    if len(sys.argv) > 1:
        try:
            candidate_ports.append(int(sys.argv[1]))
        except ValueError:
            pass
    candidate_ports.extend(DEFAULT_PORTS)

    server = None
    active_port = None

    for port in candidate_ports:
        try:
            # 綁定 127.0.0.1 避開 Windows 權限限制與 Hyper-V 衝突
            server = socketserver.TCPServer(("127.0.0.1", port), FabMindHandler)
            active_port = port
            break
        except (OSError, PermissionError):
            continue

    if server is None:
        # 若上述端口皆被佔用，使用 port 0 讓系統自動分配可用端口
        server = socketserver.TCPServer(("127.0.0.1", 0), FabMindHandler)
        active_port = server.server_address[1]

    url = f"http://127.0.0.1:{active_port}"
    print("==================================================================")
    print(f"  [FabMind v3.0] 晶圓廠零信任異常排解系統已成功啟動！")
    print(f"  🌐 本地伺服器網址: {url}")
    print("  (已為您自動避開被佔用的端口，並自動在瀏覽器中開啟)")
    print("  按 Ctrl+C 可隨時停止伺服器。")
    print("==================================================================")

    try:
        # 自動開啟瀏覽器
        webbrowser.open(url)
    except Exception:
        pass

    try:
        with server:
            server.serve_forever()
    except KeyboardInterrupt:
        print("\n伺服器已正常停止。")

if __name__ == '__main__':
    start_server()
