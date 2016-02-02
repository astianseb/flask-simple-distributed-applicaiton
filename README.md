flask-simple-distributed-application
========================================

This is simple microblog application based on https://github.com/kielpedia/flask-sqlalchemy-postgres-heroku-example/tree/master/Flasktest to showcase distributed application for demo purposes.

There are several prequisities to make it work:
1. Install & start postgress DB: https://fedoraproject.org/wiki/PostgreSQL
2. Create DB 
postgres=# CREATE USER sguser  WITH PASSWORD 'sgpass';
postgres=# CREATE DATABASE flaskdb OWNER sguser;

3. Create TABLE

flaskdb=# CREATE TABLE entry
(id serial,
title varchar(20) NOT NULL,
text varchar(200) NOT NULL);
flaskdb=# GRANT ALL PRIVILEGES ON TABLE entry to sguser
flaskdb=# GRANT USAGE, SELECT ON SEQUENCE entry_id_seq to sguser;

-----------

1. Install dependencies
sudo yum install python-pip
sudo yum install python-devel
sudo yum install postgresql-devel
sudo pip install flask
sudo pip install SQLAlchemy
sudo pip install psycopg2

2. Configure model
vi database.py:
uri = os.environ.get('DATABASE_URL', 'postgres://sguser:sgpass@127.0.0.1/flaskdb')

