from flask import render_template, flash, session, url_for, redirect, request, g
from app import mantag, db
from .forms import RegisterForm
from .models import User

@mantag.route('/', methods = ['GET', 'POST'])
def index():
    form = RegisterForm()
    #return render_template('index.html', form=form)
    if form.validate_on_submit:
        user = User(form.name.data, form.age.data, form.gender.data)
        db.session.add(user)
        db.session.commit
        flash('We can start now')
        session['user_id'] = user.id
        return redirect(url_for('evaluate'))
    return render_template('index.html', form=form)


@mantag.route('/evaluate')
def evaluate():
    if "id" in session:
        current_id = session['id']
        #evaluated = models.Evaluation.query.filter_by(user_id=current_id)
        #evaluated_ids = set([evaluation.obj_id for evaluation in evaluated])
        
        #random select the objs to be avaluated, compare the objects returned by the query
        #with the one already evaluated by the user
        
        obj = models.Object.query.get(obj_id)

        return render_template('evaluate.html', obj=obj)
    else:
        return redirect(url_for('index'))
