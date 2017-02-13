#!venv/bin/python3.4

from app import db, models



def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print ('Clear table %s' % table)
        session.execute(table.delete())
    session.commit()
    

txt = open("data/objects.txt")

tag_map = {}

clear_data(db.session)

for line in txt:
    print(line)
    (id, title, sanity, tags, img) = line.split(" | ")
    obj = models.Object(id=id, title=title, description="", sanity_test=int(sanity), img=img)
    for string in tags.split():
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


