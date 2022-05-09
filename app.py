from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    ip_address = request.environ['REMOTE_ADDR']
    return "Requester IP: " + ip_address

app.run(host="0.0.0.0", port=8080)
