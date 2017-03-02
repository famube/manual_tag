from flask import Flask
from flask_sqlalchemy import SQLAlchemy

mantag = Flask(__name__)
mantag.secret_key = 'precisa-mudar-isso-depois'
mantag.config.from_object('config')
db = SQLAlchemy(mantag)

from app import views, models

