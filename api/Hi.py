from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
import calendar
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return Response("<br><button> <a href='/api/Home'>Home</a> </button>", mimetype="text/html" )

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
    message += f"\n Greetings from {self.server.server_address[1]} at {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}  \n"
       
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    if name:
      messageG='Today is ' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
      self.wfile.write(messageG.encode())
    self.wfile.write(b'\n 2022 Calendar: \n')
    self.wfile.write(calendar.calendar(2022, 2, 1, 6).encode())
    # if self.path.endswith('/Hi'):
    #     self.send_response(200)
    #     self.send_header('Content-type', 'text/plain')
    #     self.end_headers()
    #     output = ''
    #     output += '<html><body>'
    #     output += '<h1>Welocme To my Serverless Page</h1>'
    #     output += '<h3> <a href="/Hi/date"> Add Alarm </a> </h3>'
    #     output += '</body></html>'
    #     self.wfile.write(output.encode())         
    return
