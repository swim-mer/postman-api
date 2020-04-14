# Python - Postman - API
Create a REST API in Python 3. The user logs in using basic HTTP authentication to acquire a user token. The user provides the token in the request header to access protected pages. 

## Flask Installation on Mac:
Create virtual environment called flask, inside of root directory of cloned repository:
- `$ python3 -m venv flask` for Python 3.3+

Activate environment:
- `$ . flask/bin/activate`

Install flask in virtual environment:
- `$ pip install flask`

Install Flask HTTPAuth:
- `$ pip install flask-httpauth`

Install PyJWT:
- `$ pip install pyjwt`

## To access protected pages:
- Run flask environment in a terminal and execute `app.py`
- Make a POST request in Postman at http://0.0.0.0:8888/login with credentials: 
  - 'user': 'admin', 'password': 'admin'
- Copy token in provided response and create header called 'x-access-token' with token as value in request headers
