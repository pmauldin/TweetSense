from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from Twitter import Twitter

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        print "###################"
        count = 10
        flash('Printing %d tweets about \'%s\':\n' %
              (count, form.query.data)) 
        t = Twitter()
        a = t.getTweets(form.query.data, 5)
        # z = t.getScore(a)

        flash(a)
        
        return redirect('/results')
    return render_template('index.html',
                           title='Home',
                           form=form)

@app.route('/results')
def results():
  return render_template('results.html',
                           title='Results')
