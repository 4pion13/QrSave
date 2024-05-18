#!/bin/sh
python3 manage.py migrate
uwsgi --ini /etc/uwsgi/apps-enabled/django.ini