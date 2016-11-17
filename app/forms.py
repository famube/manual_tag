from flask_wtf import Form
from wtforms import TextField, SelectField, SubmitField, RadioField
from wtforms.validators import DataRequired, EqualTo, Length, NumberRange
from flask_wtf.html5 import IntegerField

class RegisterForm(Form):
    age = IntegerField('Age') 
    name = TextField('Name', validators=[Length(min=4, max=120)])
    gender = RadioField('Gender', choices=[('M', 'Masculino'),('F', 'Feminino')])
