#Cloudloop

###Create Database

We are going to use postgresql

createdb cloudloop
createuser -P

OR

make db 
docker run -p5432:5432 -e POSTGRES_PASSWORD=616f8ea8d0b5ef3cadde8ac9032b28f1 -e POSTGRES_USER=django -e POSTGRES_DB=cloudloop postgres

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

