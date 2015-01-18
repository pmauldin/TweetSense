from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from Twitter import Twitter
from Analysis import analyze


d = [[]]
d2 = [[]]

def listtups_to_listlists(lt):
  return [[x, y] for (x, y) in lt]

query = ""
query2 = ""

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global query
    global query2
    global d
    global d2
    form = LoginForm()
    if form.validate_on_submit():
        # print "###################"
        count = 200

        query = form.query.data.replace('#','').strip()
        query2 = form.opQuery.data.replace('#','').strip()

        t = Twitter()

        a = t.getTweets(query, count)
        d = analyze(a, [float(i)/24.0 for i in range(-10*24, +3*24)])

        if not query2 == "":
          a = t.getTweets(query2, count)
          d2 = analyze(a, [float(i)/24.0 for i in range(-10*24, +3*24)])

        return redirect('/results')
    return render_template('index.html',
                           title='Home',
                           form=form)

@app.route('/results')
def results():
  if d ==  [] or d == [[]]:
    return redirect('/index')
  global query
  global query2
  global d
  global d2
  dataList = listtups_to_listlists(d)

  form = LoginForm()
  if form.validate_on_submit():
      # print "###################"
      count = 200

      query = form.query.data.replace('#','').strip()
      query2 = form.opQuery.data.replace('#','').strip()

      t = Twitter()

      a = t.getTweets(query, count)
      d = analyze(a, [float(i)/24.0 for i in range(-10*24, +3*24)])

      if not query2 == "":
        a = t.getTweets(query2, count)
        d2 = analyze(a, [float(i)/24.0 for i in range(-10*24, +3*24)])

      return redirect('/results')

  # print dataList
  # print query
  if not query2 == "":
    # print "Second value"
    dataList2 = listtups_to_listlists(d2)
    f = open('app/data.txt', 'w')
    f.write("dataList2: \n\n")
    f.write(str(dataList2))
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
