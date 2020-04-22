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

if __name__ == '__main__':
    app.run()
