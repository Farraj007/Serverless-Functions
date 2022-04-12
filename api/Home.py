from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Barham Farraj</h1><p>You visited: /%s</p> <br><button> <a href='/api/Hi'>Calendar</a> </button>" % (path), mimetype="text/html" )

