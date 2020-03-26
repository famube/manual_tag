#!venv/bin/python3.4

from app import db, models

#u = models.User(nickname='famube', id=1)
#db.session.add(u)
#db.session.commit()

#users = models.User.query.all()

#objs = models.Object.query.all()

#for obj in objs:
#    print (obj),
#    for tag in obj.tags:
#        print (tag),
#    print


#print ("Users:")

#for user in users:
#    print (user)


evaluations = models.Evaluation.query.all()

#(eid, uid, oid, know, timestamp, addtags, judgs)

for eva in evaluations:
    
    print (eva.id, "|", eva.user_id, "|", eva.obj_id, "|", eva.previous_knowledge, "|", eva.timestamp, "|", eva.additional_tags, end=' | ')
    for judg in eva.judgements:
        print (judg.tag, end=':')
        if judg.relevant:
            print (1, end=',')
        else:
            print (0, end=',')
    print ("")


