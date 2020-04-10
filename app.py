#!flask/bin/python
"""
Start a Flask web app.
"""
from flask import Flask

# Web app to run
app = Flask(__name__)


# Memory database
title = [
    {}
]


# Entry points
@app.route('/', strict_slashes=False)
def home():
    return "Home Page"

@app.route('/login', strict_slashes=False)
def login():
    return "Login"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888')
