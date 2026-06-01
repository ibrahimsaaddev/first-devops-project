from http.server import HTTPServer, BaseHTTPRequestHandler

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """
        <html>
        <head>
            <title>Ibrahim DevOps Project</title>
        </head>
        <body>
            <h1>Hello Ibrahim</h1>
            <h2>My First DevOps Project</h2>
            <p>Ubuntu + Python + Systemd + Nginx</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

server = HTTPServer(("0.0.0.0", 8000), App)
server.serve_forever()
