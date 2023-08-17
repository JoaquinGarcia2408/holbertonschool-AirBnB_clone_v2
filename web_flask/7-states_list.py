#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, request, jsonify
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    "Close the session after each request"
    storage.close()


def states_list():
    return render_template("7-states_list.html",
                           states=storage.all(State).values())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
