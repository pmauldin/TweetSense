from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from Twitter import Twitter
import numpy
from Analysis import analyze


d = [[]]

def listtups_to_listlists(lt):
  return [[x, y] for (x, y) in lt]

query = ""

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global query
    global d
    form = LoginForm()
    if form.validate_on_submit():
        # print "###################"
        count = 200
        total = 0
        query = form.query.data
        # print "Query: %s" % query
        t = Twitter()
        a = t.getTweets(form.query.data, count)
        f = open('app/data.txt', 'w')
        f.write(str(a))

        d = analyze(a, [-10.0, -7.0, -3, 0.0, 2.0])
        f2 =open('app/data2.txt', 'w')
        f2.write(str(d))
        # print graph
        # print a
        # flash(a)
        return redirect('/results')
    return render_template('index.html',
                           title='Home',
                           form=form)

@app.route('/results')
def results():
  global query
  global d
  dataList = listtups_to_listlists(d)

  print dataList
  print query

  return render_template('results.html',
                           title='Results',
                           q=query,
                           data=dataList)
