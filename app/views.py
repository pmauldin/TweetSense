from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from Twitter import Twitter

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        # print "###################"
        count = 65
        t = Twitter()
        a = t.getTweets(form.query.data, count)
        p = a.split("#?#?#?")
        # print len(p)
        if len(p) <= 1:
          flash('No tweets about \'%s\' found\n' %
              form.query.data)
        else:
          flash('Printing %d tweets about \'%s\':\n' %
                (len(p) - 1, form.query.data))
          for i in range(len(p)-1):
            print "p[%d]: %s" % (i, p[i])
            flash("#%d   -   %s\n"  % (i+1, p[i]))
        # z = t.getScore(a)

        # flash(a)
        
        return redirect('/results')
    return render_template('index.html',
                           title='Home',
                           form=form)

@app.route('/results')
def results():
  return render_template('results.html',
                           title='Results')
