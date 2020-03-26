#!venv/bin/python3.4

from app import db, models


def define_relevant(count, mincount=2, rate=0.3):
    #print ((float(count[0]) / count[1]))
    return (count[1] >= mincount and ((float(count[0]) / count[1]) > rate))



def select_relevant(counter, other_tags, mincount=2, rate=0.3):
    eanswer = {}
    for (obj, tags) in counter.items():
        if obj not in eanswer:
            eanswer[obj] = set()
        for (tag, count) in tags.items():
            #print(count)
            if define_relevant(count, mincount, rate):
                eanswer[obj].add(tag)
    

    for (obj, tags) in other_tags.items():
        if obj not in eanswer:
            eanswer[obj] = set()
        for tag in tags:
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
other_tags = {}

evaluations = models.Evaluation.query.all()

for evaluation in evaluations:
    if evaluation.obj_id not in counter:
        counter[evaluation.obj_id] = {}
    count = counter[evaluation.obj_id]
    if evaluation.obj_id not in other_tags:
        other_tags[evaluation.obj_id] = set()
    obj_tags = other_tags[evaluation.obj_id]

    for judg in evaluation.judgements:
        tag = judg.tag
        if tag not in count:
            count[tag] = [0, 0]
        if judg.relevant:
            count[tag][0] += 1
        count[tag][1] += 1

    if evaluation.additional_tags == None:
        continue
    added_tags = evaluation.additional_tags.strip().lower().split(";")
    for t in added_tags:
        obj_tags.add(t)



import sys

mincount = 2
rate = 0.3

if len(sys.argv) > 1:
    mincount = float(sys.argv[1])
    rate = float(sys.argv[2])

eanswer = select_relevant(counter, other_tags, mincount, rate)


#print(eanswer)
for (oid, tags) in eanswer.items():
    print (oid, end=" ")
    for t in tags:
        print(t, end=" ")
    print()







