from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

from main import Api_data
p1 = Api_data()
app = Flask(__name__)
@app.route('/')

def index():
    return p1.dict_data()

if __name__ == "__main__":
    app.run(debug=True)
