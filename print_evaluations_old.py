#!venv/bin/python3.4

from app import db, models


def define_relevant(count, rate=0.5):
    return (float(count[0]) / count[1] > rate)



def select_relevant(counter, rate=0.5):
    eanswer = {}
    for (obj, tags) in counter.items():
        if obj not in eanswer:
            eanswer[obj] = set()
        for (tag, count) in tags.items():
            if define_relevant(count, rate):
                eanswer[obj].add(tag)
    return eanswer

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



counter = {}

evaluations = models.Evaluation.query.all()

for evaluation in evaluations:
    print (evaluation)
    print ("Added tags:", evaluation.additional_tags)
    for judg in evaluation.judgements:
        if judg.relevant:
            print ("✓", judg.tag)
        else:
            print (judg.tag)
    print ("\n")



