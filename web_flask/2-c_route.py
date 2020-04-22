#!/usr/bin/python3
# Script that starts a flask application in a port 5000
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<var>', strict_slashes=False)
def c_is_fun(var):
    return "C " + var.replace("_", " ")


if __name__ == '__main__':
    app.run()
