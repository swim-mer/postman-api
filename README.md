# Python - Postman - API
Create a REST API in Python 3. The user logs in using basic HTTP authentication to acquire a user token. The user provides the token in the request header to access the home page. 

## Flask Installation on Mac:
Run venv with Flask:
- `$ python3 -m venv flask` for Python 3.3+

Activate environment:
- `$ . flask/bin/activate`

Install flask in virtual environment:
- `$ pip install flask`

Install Flask HTTPAuth:
- `$ pip install flask-httpauth`

Install PyJWT:
- `$ pip install pyjwt`

## To access home page:
- Run flask environment in a terminal and enter `$ ./app.py`
- Make a GET request in Postman at http://0.0.0.0:8888/login with credentials: 
  - 'user': 'admin', 'password': 'admin'
- Copy token in response and create request header called 'x-access-token' with token as value
- Make a GET request in Postman at http://0.0.0.0:8888
