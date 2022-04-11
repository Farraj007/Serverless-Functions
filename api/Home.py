from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_Get(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.send_response(200)
        self.path = ''
        with open(self.path, 'rb') as f:
            self.wfile.write(f.read())
        return