#!venv/bin/python3.4

from app import db, models
import pandas


def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print ('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()


tag_map = {}
    

txt = open("data/objects.txt")

clear_data(db.session)

#db.session.query(models.Object).delete()
#db.session.commit()



#for line in txt:
#    print(line)
#    (id, title, sanity, tags, img) = line.split(" | ")
#    obj = models.Object(id, title, "", img, int(sanity), "artist")
#    for string in tags.split():
#        if string in tag_map:
#            tag_in_db = tag_map[string]
#        else:
#            tag_in_db = models.Tag(string)
#            tag_map[string] = tag_in_db
#           
#        obj.tags.append(tag_in_db)
#    
#    db.session.add(obj)
#
#txt.close()

"""

objs = models.Object.query.all()

for obj in objs:
    print (obj),
    obj.obj_type = "artist"

    print ("type=", obj.obj_type)
    for tag in obj.tags:
        print (tag),
    print

db.session.commit()

"""



#txt = open("data/objects_movielens.txt")


#for line in txt:
#    print(line)
#    (id, title, sanity, tags, img) = line.split(" | ")
#    obj = models.Object(id, title, "", img, int(sanity), "film")
#    for string in tags.split():
#        if string in tag_map:
#            tag_in_db = tag_map[string]
#        else:
#            tag_in_db = models.Tag(string)
#            tag_map[string] = tag_in_db
#           
#        obj.tags.append(tag_in_db)
#    
#    db.session.add(obj)
#


prod_data = pandas.read_csv("data/objects_elo7.txt")


for idx,row in prod_data.iterrows():
    obj = models.Object(row["oid"], row["title"], row["description"], row["img"], 0, "product")
    for string in row["tags"].split(","):
        if string in tag_map:
            tag_in_db = tag_map[string]
        else:
            tag_in_db = models.Tag(string)
            tag_map[string] = tag_in_db

        obj.tags.append(tag_in_db)

    db.session.add(obj)



db.session.commit()






objs = models.Object.query.all()

for obj in objs:
    print (obj),
    for tag in obj.tags:
        print (tag),
    print


