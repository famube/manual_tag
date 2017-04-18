#!venv/bin/python3.4

from app import db, models

users = models.User.query.all()

#(uid, name, age, gender)

for user in users:
    print (user.id, "|", user.nickname, "|", user.age, "|", user.gender)




