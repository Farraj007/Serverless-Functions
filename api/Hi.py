from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
import calendar

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    s= self.path
    url_components = parse.urlparse(s)
    query_string = parse.parse_qsl(url_components.query)
    dic=dict(query_string)
    name= dic.get('name')
    if name:
      message = f'Hello, {name}!'
    else:
      message = 'Hello, Stranger!' 
    message += f"\n Greetings from {self.server.server_address[0]} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
       
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    messageG='Today is ' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    self.wfile.write(messageG.encode())
    self.wfile.write(b'\n 2022 Calendar: \n')
    self.wfile.write(calendar.calendar(2022, 2, 1, 6).encode())
    
    
    return
