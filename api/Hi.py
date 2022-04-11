from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib.parse import urlparse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    u=urlparse(https://serverless-functions-4xjz2dsnl-farraj007.vercel.app/api/home)
    return
