#Cloudloop

###Create Database

We are going to use postgresql
createdb cloudloop
createuser -P

###Install postgres dev headers to build psycopg2 and nginx

sudo apt update && sudo apt install libpq-dev nginx

###Create VirtualEnv

python3 -m venv env
source env/bin/activate

###Install requirements

pip install -r requirements.txt

###Run Migrations

python3 manage.py migrate

###Run Server

python3 manage.py runserver

