from flask import render_template, flash, session, url_for, redirect, request, g
from app import mantag, db
from .forms import RegisterForm
from .models import User

@mantag.route('/', methods = ['GET', 'POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit:
        user = User(form.name.data, form.age.data, form.gender.data)
        db.session.add(user)
        db.session.commit
        flash('We can start now')
        return redirect(url_for('evaluate'))
    else:
        return render_template('index.html', form=form)


@mantag.route('/evaluate')
def evaluate():
    obj = models.Object.query.get(obj_id)
    #return render_template('index.html', obj=obj)
