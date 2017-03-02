from flask import render_template, flash, session, url_for, redirect, request, g
from app import mantag, db
from .forms import RegisterForm, EvaluationForm, LFQuestions, MLQuestions
from .models import User, Object, Evaluation, Judgement, Tag
from random import shuffle

@mantag.route('/<obj_type>')
def home(obj_type):
    return render_template('home.html', objtype=obj_type)

@mantag.route('/index/<obj_type>', methods = ['GET', 'POST'])
def index(obj_type):
    form = RegisterForm()
    if form.validate_on_submit():
        if 'user_id' in session:
            print("session_userid=", session['user_id'])
        user = User(form.name.data, form.age.data, form.gender.data)
        db.session.add(user)
        db.session.commit()
        flash('We can start now')
        session['user_id'] = user.id
        print("Registered user:", user)
        return redirect(url_for('evaluate', obj_type=obj_type))
    return render_template('index.html', form=form)



@mantag.route('/evaluate/<obj_type>', methods=['GET', 'POST'])
def evaluate(obj_type):
    questions = LFQuestions()
    if 'user_id' in session:
        current_id = session['user_id']
        print("session_userid=", current_id)
        
        
        #Objects already evaluated by the current user
        
        evaluated = Evaluation.query.filter_by(user_id=current_id)
        evaluated_ids = set([evaluation.obj_id for evaluation in evaluated])
        
        #random select the objs to be avaluated, compare the objects returned by the query
        #with the one already evaluated by the user
        
        objs = Object.query.filter_by(obj_type=obj_type).all()
        
        for obj in objs:
            print(obj)
            if obj.id not in evaluated_ids:
                form = EvaluationForm()
                #form.evaluation_tags.choices = [(tag.string, tag.string) for tag in obj.tags]
                print("request:", request.form)
                print("request.method:", request.method)
                print ("PrevKnowledge", form.prev_knowledge.data)
                
                chosen_tags = []
                for tag in obj.tags:
                    if tag.string in request.form:
                        chosen_tags.append(tag.string)
                        
                print("Chosen tags:", chosen_tags)            
                
                if request.method == 'POST':    #if form.validate_on_submit(): #and form.prev_knowledge.data != None:
                    print("request.form:", request.form)
                    know = form.prev_knowledge.data
                    if know == 'None':
                        know = -1
                    eva = Evaluation(current_id, obj.id, int(know))
                    judgements = []
                    if form.submit.data: #request.form['submit'] == 'Enviar':
                        print("Formulario enviado")
                        chosen_tags = request.form.getlist("tagchoice")
                        print ("Chosen Tags:", chosen_tags)
                        for tag in obj.tags:
                            judgements.append(Judgement(eva.id, tag.string, (tag.string in request.form)))

                    eva.judgements = judgements
                    eva.additional_tags = form.addtags.data
                    print("Evaluation:\n", eva)
                    for j in eva.judgements:
                        print(j)
                    print ("Additional tags:", eva.additional_tags)
                    
                    db.session.add(eva)
                    db.session.commit()
                    return redirect(url_for('evaluate', obj_type=obj_type))

                #if not validate_on_submmit
                return render_template('evaluate.html', obj=obj, form=form, questions=questions)
    else:
        return redirect(url_for('index', obj_type=obj_type))

