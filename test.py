#!venv/bin/python3.4

from app import db, models

u = models.User(nickname='famube', id=1)
db.session.add(u)
db.session.commit()

users = models.User.query.all()


