#!/usr/bin/python3
"""task 8"""
from flask import Flask, request, jsonify
from models import storage

app = Flask(__name__)

# Método para manejar el cierre de la sesión SQLAlchemy
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


# Ruta para obtener datos de almacenamiento
def states_list():
    return render_template("7-states_list.html",
                           states=storage.all(State).values())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
