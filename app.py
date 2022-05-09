from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    ip_address = flask.request.remote_addr
    return "Requester IP: " + ip_address

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
