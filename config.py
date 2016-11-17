import os
WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'precisa-mudar-isso-depois'
SECRET_KEY = 'precisa-mudar-isso-depois'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'postgresql://mantag_user:b0ravaliat@localhost/mantag_db'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
