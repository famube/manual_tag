#!venv/bin/python3.4

from app import db, models

#u = models.User(nickname='famube', id=1)
#db.session.add(u)
#db.session.commit()

#users = models.User.query.all()

objs = models.Object.query.all()

for obj in objs:
    print (obj),
    print ("type=", obj.obj_type)
    for tag in obj.tags:
        print (tag),
    print


#print ("Users:")

#for user in users:
#    print (user)


#for eva in models.Evaluation.query.all():
#    print (eva)
