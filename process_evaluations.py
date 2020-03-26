#!venv/bin/python3.4

from app import db, models
import sys

def define_relevant(count, mincount=2, rate=0.3):
    #print ((float(count[0]) / count[1]))
    conf = float(count[0]) / count[1]
    #print (count[1], conf, file=sys.stderr)
    return (count[1] >= mincount and (conf > rate))



def select_relevant(counter, other_tags, mincount=2, rate=0.3):
    eanswer = {}
    for (obj, tags) in counter.items():
        if obj not in eanswer:
            eanswer[obj] = set()
        for (tag, count) in tags.items():
            if count[1] >= mincount:
                print (count[1], float(count[0]) / count[1], file=sys.stderr)

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

#invalid_users = set([17, 18, 19, 22, 23, 24, 27, 28, 29, 30, 31, 33, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94])
invalid_users = set([113, 123, 125, 131])

for evaluation in evaluations:
    if evaluation.user_id in invalid_users:
        continue
    obj = models.Object.query.filter_by(id=evaluation.obj_id).all()
    if obj[0].sanity_test != 0:
        continue
    if evaluation.obj_id not in counter:
        counter[evaluation.obj_id] = {}
    count = counter[evaluation.obj_id]
    if evaluation.obj_id not in other_tags:
        other_tags[evaluation.obj_id] = set()
    obj_tags = other_tags[evaluation.obj_id]

    none_rel = True

    for judg in evaluation.judgements:
        tag = judg.tag
        if tag == "":
            continue
        if tag not in count:
            count[tag] = [0, 0]
        if judg.relevant:
            none_rel = False
            count[tag][0] += 1
        count[tag][1] += 1

    if none_rel:
        for judg in evaluation.judgements:
            tag = judg.tag
            if tag == "":
                continue
            count[tag][1] -= 1

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
#for (oid, tags) in eanswer.items():
#    if len(tags) > 0:
#        print (oid, end=",")
#        print (",".join(tags))


for oid, tags in counter.items():
    print (oid, end="")
    for t, count in tags.items():
        if count[1] >= mincount:
            print (",%s:%f" % (t, float(count[0])/count[1]), end="")
    print()







