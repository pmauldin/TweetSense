from flask import render_template, flash, redirect, request
from app import app
from .forms import LoginForm, RandomForm
from Twitter import Twitter
from Analysis import analyze
from RandomTopic import get_random_topic


d = [[]]
d2 = [[]]

def listtups_to_listlists(lt):
  return [[x, y] for (x, y) in lt]

def setGraphs(form):
  global query
  global query2
  global d
  global d2

  count = 80

  query = str(form.query.data.replace('#','').strip())
  query2 = str(form.opQuery.data.replace('#','').strip())

  t = Twitter()

  a = t.getTweets(query, count)
  d = analyze(a, [float(i)/24.0 for i in range(-10*24, +3*24)])

  if not query2 == "":
    a = t.getTweets(query2, count)
    d2 = analyze(a, [float(i)/24.0 for i in range(-10*24, +3*24)])


query = ""
query2 = ""

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        # print "###################"
        setGraphs(form)

        return redirect('/results')
    return render_template('index.html',
                           title='Home',
                           form=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
  # if d ==  [] or d == [[]]:
    # return redirect('/index')
  global query
  global query2
  global d
  global d2
  dataList = listtups_to_listlists(d)

  form = LoginForm()
  if form.validate_on_submit():
      # print "###################"
      setGraphs(form)

      return redirect('/results')

  # print dataList
  # print query
  if not query2 == "":
    # print "Second value"
    dataList2 = listtups_to_listlists(d2)
    return render_template('results.html',
                           title='Results',
                           q=query,
                           q2=query2,
                           data=dataList,
                           data2=dataList2,
                           form=form)

  return render_template('results.html',
                           title='Results',
                           q=query,
                           data=dataList,
                           form=form)

@app.route('/about')
def about():
  return render_template('about.html',
                          title='Results')

@app.route('/random', methods=['GET', 'POST'])
def random():

  form = RandomForm()
  if form.validate_on_submit():
    print "??"
    if request.form['btn'] == 'Randomize':
      t1=get_random_topic().split(' ', 1)[0]
      while not Twitter().checkTerm(t1):
        t1=get_random_topic().split(' ', 1)[0]

      t2=get_random_topic().split(' ', 1)[0]
      while not Twitter().checkTerm(t2):
        t2=get_random_topic().split(' ', 1)[0]
      print "t1: %s\nt2: %s" % (t1, t2)
      form.query.data=t1
      form.opQuery.data=t2
    else:
      if form.query != "" or form.opQuery != "":
        setGraphs(form)
        
        return redirect('/results')

  return render_template('random.html',
                          form=form)

@app.route('/hof')
def hof():
  return render_template('hof.html')