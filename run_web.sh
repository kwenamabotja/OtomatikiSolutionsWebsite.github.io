#!/bin/bash

# run tests first
python manage.py test

pip install -r requirements.txt

echo yes | python manage.py collectstatic

sleep 5

python manage.py makemigrations --merge && python manage.py migrate

sleep 2

gunicorn otomatiki.wsgi:application -b 0:8000 -w 2 --log-level DEBUG --reload
