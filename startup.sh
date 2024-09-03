#!/bin/bash
python manage.py collectstatic && gunicorn --workers 2 --bind 0.0.0.0:8000 hs_ideas.wsgi.application