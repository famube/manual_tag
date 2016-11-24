from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
        
    def __init__(self, name, age, gender):
        self.nickname = name
        self.age = age
        self.gender = gender
        
    def __repr__(self):
        return '<User %r ID:%d>' % (self.nickname, self.id)




#Object-Tag Relationship Table
obj_tags = db.Table('obj_tags', db.Model.metadata,
    db.Column('obj_id', db.String, db.ForeignKey('object.id')),
    db.Column('tag', db.String, db.ForeignKey('tag.string'))
)


class Object(db.Model):
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    img = db.Column(db.String)
    
    # 0 = regular object
    # 1 = only trivially relevant tags
    #-1 = only trivially irrelevant tags
    sanity_test =  db.Column(db.Integer)
    
    #many to many Object <=> Tag
    
    tags = db.relationship('Tag', secondary=obj_tags,
        backref=db.backref('objects', lazy='dynamic'))

    def __init__(self, id, title, description, img, sanity_test):
        self.id = id
        self.title = title
        self.description = description
        self.img = img
        self.sanity_test = sanity_test

    def __repr__(self):
        return '<Object ID:%s>' % (self.id)


class Tag(db.Model):
    string = db.Column(db.String, primary_key=True)

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return '<Tag: %s>' % (self.string)


class Judgement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eval_id = db.Column('eval_id', db.Integer, db.ForeignKey('evaluation.id'))
    tag = db.Column('tag', db.String, db.ForeignKey('tag.string'))
    
    #relevance label
    relevant = db.Column('label', db.Boolean)   

    def __init__(self, eval_id, tag, relevant):
        self.eval_id = eval_id
        self.tag = tag
        self.relevant = relevant
        
    def __repr__(self):
        return '<Tag: %s RelevanceLabel: %r>' % (self.tag.string, self.relevant)


#judgements = db.Table('judgements',
#    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#    db.Column('obj_id', db.String, db.ForeignKey('object.id')),
#    db.Column('tag', db.String, db.ForeignKey('tag.string')),
#    db.Column('label', db.Boolean),   
#)


class Evaluation(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
    obj_id = db.Column('obj_id', db.String, db.ForeignKey('object.id'))
    previous_knowledge = db.Column(db.Integer)
    timestamp = db.Column('timestamp', db.DateTime)
   
    judgements = db.relationship('Judgement', backref='evaluation', lazy='dynamic')


    def __init__(self, user_id, obj_id, previous_knowledge):
        self.user_id = user_id
        self.obj_id = obj_id
        self.previous_knowledge = previous_knowledge
        #self.judgements = judgements
        timestamp = datetime.utcnow()

    def print_judgements(self):
        for judgement in self.judgements:
            print (judgement)

    def __repr__(self):
        return '<UserID: %s, ObjID: %s, Knowledge: %d>' % (self.user_id, self.obj_id, self.previous_knowledge)





