from flask import render_template, flash, session, url_for, redirect, request, g
from app import mantag, db
from .forms import RegisterForm, EvaluationForm, LFQuestions, MLQuestions
from .models import User, Object, Evaluation, Judgement, Tag
from random import shuffle

NEVALS=20

def load_objs(filename):
    objs = {}
    obj_file = open(filename)
    for line in obj_file:
        (id, title, sanity, tags, img) = line.split(" | ")
        objs[id] = (title, sanity, tags.split(), img)
    obj_file.close()
    return objs



@mantag.route('/<obj_type>')
def home(obj_type):
    return render_template('home.html', obj_type=obj_type)

@mantag.route('/index/<obj_type>', methods = ['GET', 'POST'])
def index(obj_type):
    session['nevaluated'] = 0
    form = RegisterForm()
    if form.validate_on_submit():
        if 'user_id' in session:
            print("session_userid=", session['user_id'])
        user = User(form.name.data, int(form.age.data), form.gender.data)
        db.session.add(user)
        db.session.commit()
        flash('We can start now')
        session['user_id'] = user.id
        print("Registered user:", user)
        return redirect(url_for('evaluate', obj_type=obj_type))
    return render_template('index.html', form=form)

@mantag.route('/thanks/<obj_type>')
def thanks(obj_type):
    return render_template('thanks.html', obj_type=obj_type)

@mantag.route('/evaluate/<obj_type>', methods=['GET', 'POST'])
def evaluate(obj_type):

    if obj_type == 'artist':
        questions = LFQuestions()
        selected = load_objs('data/selected_objects.txt')
        
    else:
        questions = MLQuestions()
        selected = load_objs('data/selected_objects_movielens.txt')

    print (selected)

    if 'user_id' in session:
        current_id = session['user_id']
        print("session_userid=", current_id)
        
        
        #Objects already evaluated by the current user
        
        evaluated = Evaluation.query.filter_by(user_id=current_id)
        evaluated_ids = set([evaluation.obj_id for evaluation in evaluated])
        
        if 'nevaluated' in session:
            nevaluated = session['nevaluated']
        else:
            nevaluated = len(evaluated_ids) % (NEVALS)
        
        
     
        
        #random select the objs to be evaluated, compare the objects returned by the query
        #with the one already evaluated by the user
        
        objs = Object.query.filter_by(obj_type=obj_type).all()
        
        for obj in objs:
            #print(obj)
            if obj.id not in evaluated_ids and obj.id in selected:
                form = EvaluationForm()
                #(title, sanity, tags, img) = selected[obj.id]
                #obj.tags = tags
                #obj.img = img
                #form.prev_knowledge(onclick_="enableSending();")
                #form.submit(disabled_="disabled")
                
                #form.prev_knowledge.__html__ = form.prev_knowledge.__html__().replace("input id=", "onclick=\"enableSending();\" input id=")
                #print (form.prev_knowledge.__html__().replace("input id=", "onclick=\"enableSending();\" input id="))
                #print (form.submit.__html__())
                
                #print ("\n", form.addtags.__html__(), "\n")
                
                
                #form.evaluation_tags.choices = [(tag.string, tag.string) for tag in obj.tags]
                #print("request:", request.form)
                #print("request.method:", request.method)
                #print ("PrevKnowledge", form.prev_knowledge.data)
                

                chosen_tags = []
                for tag in obj.tags:
                    if tag.string in request.form:
                        chosen_tags.append(tag.string)
                        
                #print("Chosen tags:", chosen_tags)            
                
                if request.method == 'POST':    #if form.validate_on_submit(): #and form.prev_knowledge.data != None:
                    #print("request.form:", request.form)
                    know = form.prev_knowledge.data
                    if know == 'None':
                        know = -1
                    eva = Evaluation(current_id, obj.id, int(know))
                    judgements = []
                    
                    #if form.skip.data:
                    #    print("Pulou")
                    #    return redirect(url_for('evaluate', obj_type=obj_type))
                    
                    if form.submit.data: #request.form['submit'] == 'Enviar':
                        #print("Formulario enviado")
                        chosen_tags = request.form.getlist("tagchoice")
                        #print ("Chosen Tags:", chosen_tags)
                        for tag in obj.tags:
                            judgements.append(Judgement(eva.id, tag.string, (tag.string in request.form)))

                    eva.judgements = judgements
                    
                    if not form.skip.data:
                        eva.additional_tags = request.form['addtags']
                        #print ("ADD:", eva.additional_tags)
                        #print("Evaluation:\n", eva)
                        #for j in eva.judgements:
                        #    print(j)
                        #print ("Additional tags:", eva.additional_tags)
                    
                    db.session.add(eva)
                    db.session.commit()
                    
                    if session['nevaluated'] == (NEVALS-1):
                        session['nevaluated'] = 0
                        return redirect(url_for('thanks', obj_type=obj_type))
            
                    session['nevaluated'] += 1
    
                    
                    return redirect(url_for('evaluate', obj_type=obj_type))

                #if not validate_on_submmit
                return render_template('evaluate.html', obj=obj, eva_form=form, questions=questions, progress=nevaluated+1)
    else:
        return redirect(url_for('index', obj_type=obj_type))

