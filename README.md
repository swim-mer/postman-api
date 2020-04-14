# Python - Postman - Flask - API
Create a REST API in Python 3. The user logs in using basic HTTP authentication to acquire a user token. The user provides the token in the request header to access protected pages. 

## App Installation on Mac:
Clone repository
- `$ git clone https://github.com/swim-mer/postman-api.git`

Create virtual environment called flask, inside root directory of cloned repository:
- `$ python3 -m venv flask` for Python 3.3+

Activate environment:
- `$ . flask/bin/activate`

Install flask in virtual environment:
- `$ pip install flask`

Install Flask HTTPAuth:
- `$ pip install flask-httpauth`

Install PyJWT:
- `$ pip install pyjwt`

### Run server
- Execute `app.py` (`$ ./app/app.py`)

## To access protected pages:
- Make a POST request in Postman at http://0.0.0.0:8888/login with credentials: 
  - 'user': 'admin', 'password': 'admin'
- Copy token in provided response and create header called 'x-access-token' with token as value in request headers

### Protected pages:
- http://0.0.0.0:8888 - Home Page
- http://0.0.0.0:8888/protected - Acquire payload
