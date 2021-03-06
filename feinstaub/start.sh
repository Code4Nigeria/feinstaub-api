#!/bin/bash
export DJANGO_SETTINGS_MODULE=feinstaub.settings.production
export PYTHONUNBUFFERED=0
mkdir -p /opt/code/feinstaub/feinstaub/static
mkdir -p /home/uid1000/feinstaub
mkdir -p /home/uid1000/feinstaub/logs
mkdir -p /home/uid1000/feinstaub/run
chmod -R 777 /home/uid1000/feinstaub/run
python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn feinstaub.wsgi:application --log-level=info -w 3 --bind=0.0.0.0:8000
