from flask import Flask
from flask_cors import CORS, jsonify, request
import sys
sys.path.append('src/Controller')
from CalculosController import CalculosController

app = Flask(__name__)
CORS(app)
calculos = CalculosController()

@app.route("/pitagoras/<float:a>/<float:b>", methods=["GET"])
def pitagoras_route(a, b):
    c = calculos.pitagoras(a, b)
    return jsonify({"c": c})

if __name__ == "__main__":
    app.run()