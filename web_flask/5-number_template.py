#!/usr/bin/python3
"""flask script"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return "C" + " " + text


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Python"""
    text = text.replace("_", " ")
    if text is None:
        return "Python is cool"
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    n = int(n)
    return "{} is a number".format(n)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
