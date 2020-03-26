from flask_wtf import Form
from wtforms import TextField, StringField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, NumberRange
from flask_wtf.html5 import IntegerField
from flask import flash

class RegisterForm(Form):
    age = SelectField('Idade', choices=[('20', 'Menos de 20'),('25', '20-24'),('30', '25-29'),('35', '30-34'),('40', '35-39'),('45', '40-44'), ('50', '45-49'), ('55', 'Mais de 50')])
    name = TextField('Nome', validators=[Length(min=4, max=120), DataRequired()])
    gender = RadioField('Sexo', choices=[('M', 'Masculino'),('F', 'Feminino')])

    labels = {'age': 'Idade', 'name': 'Nome', 'gender': 'Sexo'}
    error_msg = {'age': 'Escolha uma opção', 'name': 'Campo de preenchimento obrigatório', 'gender': 'Escolha uma opção'}
    
    def flash_errors(self):
        for field, errors in self.errors.items():
            for error in errors:
                flash(u"Error in the %s field - %s" % (getattr(self, field).label.text, error), "error")



class EvaluationForm(Form):        
    prev_knowledge = RadioField('Knowledge', choices=[(2, 'Muito'), (1, 'Pouco'), (0, 'Nada')])
    submit = SubmitField(label='Enviar', render_kw={'disabled':'disabled'})
    #submit = SubmitField(label='Enviar')
    skip = SubmitField(label='Pular')
    #addtags = StringField('AddTags')
    
    #evaluation_tags = SelectMultipleField('ChosenTags', widget=SelectCheckbox()) 
    
    #def set_choices(taglist):
    #    evaluation_tags.choices = [(tag, tag) for tag in taglist]



class LFQuestions:
    first = "Você conhece algo sobre essa banda / artista?"
    second = "Quais dessas palavras caracterizam a banda / artista acima? (Marque todas as palavras que julgar relevante)"
    #third = "(Opcional) Inclua até 5 tags (palavras-chave separadas por ";") que você considera relevantes e que não foram citadas acima:"

class MLQuestions:
    first = "Você conhece algo sobre esse filme?"
    second = "Quais dessas palavras caracterizam o filme acima? (Marque todas as palavras que julgar relevante)"

class Elo7Questions:
    first = "Você sabe do que se trata esse produto?"
    second = "Quais dessas palavras-chave caracterizam o produto acima? (Marque todas as palavras que julgar relevante)"



