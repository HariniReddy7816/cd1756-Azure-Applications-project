"""
The flask application package.
"""
import os
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.config['BLOB_ACCOUNT'] = os.environ.get('BLOB_ACCOUNT')
app.config['BLOB_STORAGE_KEY'] = os.environ.get('BLOB_STORAGE_KEY')
app.config['BLOB_CONTAINER'] = os.environ.get('BLOB_CONTAINER')
app.config['BLOB_CONNECTION_STRING'] = os.environ.get('BLOB_CONNECTION_STRING')

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
