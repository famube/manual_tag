from flask_wtf import Form
from wtforms import TextField, SelectField, SubmitField, RadioField
from wtforms.validators import DataRequired, EqualTo, Length, NumberRange
from flask_wtf.html5 import IntegerField

class RegisterForm(Form):
    age = IntegerField('Age', validators=[DataRequired()]) 
    name = TextField('Name', validators=[Length(min=4, max=120)])
    gender = RadioField('Gender', choices=[('M', 'Masculino'),('F', 'Feminino')])
    

class EvaluationForm(Form):        
    __init__(self, obj):
       self.prev_knowledge = RadioField('Knowledge', choices=[('Muito', 'Muito'), ('Pouco', 'Pouco'), ('Nada', 'Nada')])
       self.evaluation_tags = SelectField('Tags')
       self.evaluation_tags.choices = [(tag.string, tag.string) for tag in obj.tags]

