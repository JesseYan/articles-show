#!venv/bin/python

__author__ = 'jesse'

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import *


# Use a Class-based config to avoid needing a 2nd file
# os.getenv() enables configuration through OS environment variables
class ConfigClass(object):
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'THIS IS AN INSECURE SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', db_path)
    CSRF_ENABLED = True

    # Flask-Mail settings
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', MAIL_USERNAME)
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', MAIL_PASSWORD)
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', MAIL_DEFAULT_SENDER)
    MAIL_SERVER = os.getenv('MAIL_SERVER', MAIL_SERVER)
    MAIL_PORT = int(os.getenv('MAIL_PORT', MAIL_PORT))
    MAIL_USE_SSL = int(os.getenv('MAIL_USE_SSL', MAIL_USE_SSL))

    # Flask-User settings
    USER_APP_NAME = "Articles-show"                # Used by email templates


myapp = Flask(__name__)
myapp.config.from_object(__name__+'.ConfigClass')

# Load local_settings.py if file exists         # For automated tests
try:
    myapp.config.from_object('local_settings')
except Exception as ex:
    print 'Exception:', ex
    pass

# Initialize Flask extensions
mail = Mail(myapp)                                # Initialize Flask-Mail
db = SQLAlchemy(myapp)                            # Initialize Flask-SQLAlchemy


