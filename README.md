# Auth Service

### Generate Private KEY
openssl genrsa -out private.pem 2048

### Generate Public KEY
openssl rsa -in private.pem -outform PEM -pubout -out public.pem

### Generate Private Refresh KEY
openssl genrsa -out private-refresh.pem 2048

### Database tables

copy on -> tables.txt

### ENV

sample .env on .env.example

### How ru RUN
`python -m venv env`

active your virtual env

`pip install -r requirements.txt`

`python main.py`
