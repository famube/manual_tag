from app import db


class User(db.Model):
    #__tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
        
    def __init__(self, id, nickname):
        self.id = id
        self.nickname = nickname
        
    def __repr__(self):
        return '<User %r ID:%d>' % (self.name, self.id)


#Association table
#obj_tags = db.Table('obj_tags', db.metadata,
#    db.Column('obj_id', db.String, db.ForeignKey('objects.id')),
#    db.Column('tag', db.String, db.ForeignKey('tags.string'))
#)

class Object(db.Model):
    #__tablename__ = 'objects'
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    
    #many to many Object <=> Tag
    #tags = db.relationship("Tag", secondary=obj_tags)

    #tags = db.relationship('Tag', backref='tag_obj', lazy='dynamic')

#class Tag(db.Model):
    #__tablename__ = 'tags'
#    string = db.Column(db.String, primary_key=True)
