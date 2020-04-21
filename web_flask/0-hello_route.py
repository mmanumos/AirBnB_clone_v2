#!/usr/bin/python3
# Script that starts a flask application in a port 5000
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
