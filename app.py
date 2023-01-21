from flask import Flask
from flask_cors import CORS, jsonify, request
import sys
sys.path.append('src/Controller')
from CalculosController import CalculosController

app = Flask(__name__)
CORS(app)
calculos = CalculosController()
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
@app.route("/pitagoras/<float:a>/<float:b>", methods=["GET"])
def pitagoras_route(a, b):
    c = calculos.pitagoras(a, b)
    return jsonify({"c": c})

if __name__ == "__main__":
    app.run()