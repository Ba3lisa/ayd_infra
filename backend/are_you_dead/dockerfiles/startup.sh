#!/bin/sh

echo Running startup script: $STARTUP_SH
echo Moving to $WORKING_DIR
cd $WORKING_DIR

echo Running django on port $DJANGO_PORT
python3 manage.py runserver 0.0.0.0:$DJANGO_PORT
