#!/usr/bin/python3
# Script that starts a flask application in a port 5000
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(exception):
    """Calls Storage close on appcontext"""
    storage.close()


@app.route("/states")
def state_list():
    my_states = []
    for key, value in storage.all(State).items():
        my_states.append(value)
    return render_template('9-states.html', my_states=my_states)


@app.route("/states/<id>")
def state_var(id=None):
    name = None
    for key, value in storage.all(State).items():
        if value.id == id:
            name = value.name

    my_cities = []
    for key, value in storage.all(City).items():
        if value.state_id == str(id):
            my_cities.append(value)

    return render_template('9-states.html', my_cities=my_cities, name=name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
