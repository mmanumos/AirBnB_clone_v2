#!/usr/bin/python3
# Script that starts a flask application in a port 5000
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<var>')
def c_is_fun(var):
    return "C " + var.replace("_", " ")


@app.route('/python')
@app.route('/python/<var>')
def python_is_cool(var="is cool"):
    return "Python " + var.replace("_", " ")


@app.route('/number/<int:n>')
def is_number(n):
    if isinstance(n, int):
        return str(n) + " is a number"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
