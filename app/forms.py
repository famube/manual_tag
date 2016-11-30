from flask_wtf import Form
from wtforms import TextField, BooleanField, SubmitField, RadioField, SelectMultipleField
from wtforms.validators import DataRequired, EqualTo, Length, NumberRange
from flask_wtf.html5 import IntegerField


class RegisterForm(Form):
    age = IntegerField('Age', validators=[DataRequired()]) 
    name = TextField('Name', validators=[Length(min=4, max=120), DataRequired()])
    gender = RadioField('Gender', choices=[('M', 'Masculino'),('F', 'Feminino')])


#class SelectCheckbox(object): 
#
#    def __call__(self, field, **kwargs): 
#        html = [''] 
#        for val, label, selected in field.iter_choices(): 
#            html.append(self.render_option(field.name, val, label, selected)) 
#        return HTMLString(u''.join(html)) 


#    def render_option(cls, name, value, label, selected): 
#        options = {'value': value} 
#        if selected: 
#            options['checked'] = u'checked' 
#        return HTMLString(u'<input type="checkbox" name="%s" %s>%s</input>' % (name, html_params(**options), escape(unicode(label)))) 


  

class EvaluationForm(Form):        
    prev_knowledge = RadioField('Knowledge', choices=[(2, 'Muito'), (1, 'Pouco'), (0, 'Nada')])
    submit = SubmitField(label='Enviar')
    skip = SubmitField(label='Pular')
    
    #evaluation_tags = SelectMultipleField('ChosenTags', widget=SelectCheckbox()) 
    
    #def set_choices(taglist):
    #    evaluation_tags.choices = [(tag, tag) for tag in taglist]


