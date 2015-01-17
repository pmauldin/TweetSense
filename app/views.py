from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from Twitter import Twitter
import numpy
# from Analysis import analyze

# total = 0
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        # print "###################"
        count = 200
        total = 0
        t = Twitter()
        a = t.getTweets(form.query.data, count)

        # graph = analyze(a, [-1.0, 0.0, 1.0])
        # print graph
        # print a
        # flash(a)
        return redirect('/results')
    return render_template('index.html',
                           title='Home',
                           form=form)

@app.route('/results')
def results():
  return render_template('results.html',
                           title='Results')
