#!flask/bin/python
"""
Start a Flask web app.
"""
from flask import Flask, make_response, jsonify, request
from flask_httpauth import HTTPBasicAuth
import jwt
from functools import wraps


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


# Token
def get_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        else:
            return jsonify({'Error': 'Token is missing'})
        try:
            data = jwt.decode(token, key)
            data == user
        except:
            return jsonify({'Error': 'Token is invalid'})

        return f(user, *args, **kwargs)

    return decorated


# Entry points
@app.route('/', strict_slashes=False)
@get_token
def home(user):
    return "Home Page"


@app.route('/login', strict_slashes=False)
@auth.login_required
def login():
    token = jwt.encode(user, key, algorithm='HS256')
    return jsonify({'token': token.decode('UTF-8')})


# Authentication
# HTTP Basic Auth
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
