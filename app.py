#!flask/bin/python
"""
Start a Flask web app.
"""
from flask import Flask, make_response, jsonify
from flask_httpauth import HTTPBasicAuth
import jwt


# Web app to run
app = Flask(__name__)

# auth object
auth = HTTPBasicAuth()

# Memory database
user = {
    'username': 'admin',
    'password': 'admin'
}

# Secret Key
key = 'secret'

# Entry points
@app.route('/', strict_slashes=False)
def home():
    return "Home Page"


@app.route('/login', strict_slashes=False)
@auth.login_required
def login():
    return jwt.encode({'some': 'payload'}, key, algorithm='HS256')
#     return 'test'

# Authentication
@auth.get_password
def get_password(username):
    if username == user['username']:
        return user['password']
    return None


@auth.error_handler
def unauthorized():
    return make_response({'Error': 'Invalid credentials'}, 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
