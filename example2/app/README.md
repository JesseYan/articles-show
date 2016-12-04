# app directory

This directory contains the Flask application code.

The code has been organized into the following directories:

    # Code directories
    models       # Database Models and their Forms
    startup      # Application startup code and settings.py file
    views        # View functions

    # Asset and Template directories
    static       # This subdirectory will be mapped to the "/static/" URL
    templates    # Jinja2 HTML template files
    
# 运行目录
example2
emp-evenv/bin/pip -r requirements.txt

## update runserver.sh
python -> emp-venv/bin/python


## flask-user TypeError: getaddrinfo() argument 1 must be string or None
update: MAIL_SERVER = 'smtp.gmail.com'
改两项为一项

## flask-user AttributeError: 'bool' object has no attribute '__call__'
增加一个包并安装:
Flask-Login==0.2.11
