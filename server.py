import http.server
import socketserver
import os

os.chdir(os.path.dirname(os.path.abspath(r"DIRECTORY"))) # CHANGE THIS!


PORT = 8080
handler = http.server.SimpleHTTPRequestHandler



with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()
