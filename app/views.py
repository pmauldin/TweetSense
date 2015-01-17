from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from Twitter import Twitter

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Peter'}
    
    return render_template('index.html',
                           title='Home',
                           user=user)

def idk(s):
	return len(s)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Length of %s: %d characters' %
              (form.query.data, idk(form.query.data)))
        t = Twitter()
        a = t.getTweets(form.query.data, 100)
        print a[0]
        # s = '\n'.join(a)
        # print s
        flash(a[0])
        
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)
