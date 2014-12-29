from flask_wtf import Form
from wtforms import TextField,SubmitField
from wtforms.validators import DataRequired

class MyForm(Form):
    name   = TextField('name',validators=[DataRequired])
    submit = SubmitField('submit')

