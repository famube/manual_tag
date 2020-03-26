#!venv/bin/python3.4

from app import db, models

objs = models.Object.query.all()

#(uid, name, age, gender)

for o in objs:
    print (o.id)


