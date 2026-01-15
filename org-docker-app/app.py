student@DESKTOP-3GMCIP9:~/org-docker-app$ cat app.py
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Hello from Dockerized App 🚀".encode("utf-8"))

server = HTTPServer(("0.0.0.0", 8000), MyHandler)
print("Server running on port 8000")
server.serve_forever()
