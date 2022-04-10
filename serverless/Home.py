from http.server import BaseHTTPRequestHandler
from cow import Cowacter

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = Cowacter().milk('Hello from Python from a Serverless Function!')
        self.wfile.write(message.encode())
        return
    