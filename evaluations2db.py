#!venv/bin/python3.4

from app import db, models
from datetime import datetime
import sys

def db_insert_evals(filename, offset):
    eval_file = open(filename)
    tags = set()
    for db_tag in models.Tag.query.all():
        tags.add(db_tag.string)
    for line in eval_file:
        print(line)
        (eid, uid, oid, know, timestamp, addtags, judgs) = line[:len(line)-1].split(" | ")
        
        eva = models.Evaluation(uid, oid, int(know))
        time = datetime.now()
        eva.timestamp = time
        eva.id = int(eid) + offset
        eva.additional_tags = addtags
        judgements = []
        
        for elem in judgs.split(","):
            if len(elem) != 2:
                continue
            (tag, label) = elem.split(":")
            if label == "0":
                rel = False
            else:
                rel = True
            tag = tag.strip()
            if tag in tags:
                judgements.append(models.Judgement(eva.id, tag, rel))
        eva.judgements = judgements
        
        db.session.add(eva)
        db.session.commit()
        #print("Evaluation:\n", eva)
        #for j in eva.judgements:
        #    print(j)
        #    print ("Additional tags:", eva.additional_tags)
        #    print ("Time:", eva.timestamp)
    eval_file.close()





def db_insert_users(filename, offset):
    users_file = open(filename)
    for line in users_file:
        (uid, name, age, gender) = line[:len(line)-1].split(" | ")
        user = models.User(name, int(age), gender)
        user.id = int(uid) + offset
        db.session.add(user)
        db.session.commit()
        print(user)
    users_file.close()
    



offset = 0
if len(sys.argv) == 4:
    offset = int(sys.argv[3])


db_insert_users(sys.argv[1], offset)
db_insert_evals(sys.argv[2], offset)



        
        
        
