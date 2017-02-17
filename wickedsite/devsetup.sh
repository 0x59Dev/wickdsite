#!/bin/bash 
# python manage.py makemigrations && python manage.py migrate
psql postgres://testuser:testpass@localhost/testdb?sslmode=disable < dbdump
reset
