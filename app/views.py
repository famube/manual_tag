from flask import render_template, flash, session, url_for, redirect, request, g
from app import mantag, db
from .forms import RegisterForm, EvaluationForm
from .models import User, Object, Evaluation
from random import shuffle

@mantag.route('/index', methods = ['GET', 'POST'])
def index():
    form = RegisterForm()
    #return render_template('index.html', form=form)
    if form.validate_on_submit:
        if 'user_id' in session:
            print("session_userid=", session['user_id'])
#            session.pop('user_id')
        if form.name.data == None:
            return render_template('index.html', form=form)
        user = User(form.name.data, form.age.data, form.gender.data)
        db.session.add(user)
        db.session.commit()
        flash('We can start now')
        session['user_id'] = user.id
        print("Registered user:", user)
        return redirect(url_for('evaluate'))
    return render_template('index.html', form=form)


@mantag.route('/evaluate', methods=['GET', 'POST'])
def evaluate():
    if 'user_id' in session:
        current_id = session['user_id']
        print("session_userid=", current_id)
        
        
        #Objects already evaluated by the current user
        
        evaluated = Evaluation.query.filter_by(user_id=current_id)
        evaluated_ids = set([evaluation.obj_id for evaluation in evaluated])
        
        #random select the objs to be avaluated, compare the objects returned by the query
        #with the one already evaluated by the user
        
        objs = Object.query.all()
        
        for obj in shuffle(objs):
            if obj.id not in evaluated_ids:
                form = EvaluationForm(obj)
                return render_template('evaluate.html', obj=obj, form=form)
    else:
        return redirect(url_for('index'))



