import http.server
import ssl
import os

# 替換為 mkcert 生成的憑證檔案名
CERT_FILE = "localhost+2.pem" # 根據你 mkcert 生成的檔名修改
KEY_FILE = "localhost+2-key.pem" # 根據你 mkcert 生成的檔名修改

# 檢查憑證檔案是否存在
if not os.path.exists(CERT_FILE) or not os.path.exists(KEY_FILE):
    print(f"錯誤：憑證檔案 {CERT_FILE} 或 {KEY_FILE} 不存在。")
    print("請確認已在當前目錄下執行 'mkcert localhost 127.0.0.1'。")
    exit()

server_address = ('', 8000)
handler = http.server.SimpleHTTPRequestHandler

print(f"Serving on https://localhost:{server_address[1]}")
print("如果您在瀏覽器中遇到安全警告，請選擇 '繼續前往' 或 '進階' 並接受風險。")

with http.server.HTTPServer(server_address, handler) as httpd:
    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        server_side=True,
        certfile=CERT_FILE,
        keyfile=KEY_FILE,
        ssl_version=ssl.PROTOCOL_TLS_SERVER
    )
    httpd.serve_forever()
