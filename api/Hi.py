from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib.parse import urlparse
import calendar

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message='Today is ' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    self.wfile.write(message.encode())
    self.wfile.write(b'\n 2022 Calendar:')
    self.wfile.write(calendar.calendar(2022, 2, 1, 6).encode())
    u=urlparse("https://serverless-functions-fhcu5fh5j-farraj007.vercel.app/api/Hi")
    u.path()
    self.wfile.write(u.path().encode())
    return
