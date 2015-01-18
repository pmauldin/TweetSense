from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Optional


class LoginForm(Form):
    query = StringField('query', validators=[DataRequired()])
    opQuery = StringField('opQuery', validators=[Optional])
