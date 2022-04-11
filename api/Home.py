# from http.server import BaseHTTPRequestHandler

# class handler(BaseHTTPRequestHandler):

#     def do_Get(self):
#         self.send_response(200)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()
#         self.send_response(200)
#         self.path = ''
#         with open(self.path, 'rb') as f:
#             self.wfile.write(f.read())
#         return
from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")