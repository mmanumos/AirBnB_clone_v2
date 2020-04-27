#!/usr/bin/python3
# Script that starts a flask application in a port 5000
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(exception):
    """Calls Storage close on appcontext"""
    storage.close()


@app.route("/states_list")
def state_list():
    my_states = []
    for key, value in storage.all(State).items():
        my_states.append(value)
    return render_template('7-states_list.html', my_states=my_states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
