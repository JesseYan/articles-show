# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment


app = Flask(__name__)           # The WSGI compliant web application object
db = SQLAlchemy(app)            # Setup Flask-SQLAlchemy
manager = Manager(app)          # Setup Flask-Script
moment = Moment(app)

from app.startup.create_app import create_app
