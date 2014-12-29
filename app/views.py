from app import app
from flask import render_template
import json
from forms import *

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/data')
def data():
    obj={'name':"aa",'youjianyingxiao':'[120, 132, 101, 134, 90000, 230, 210]'}
    return json.dumps(obj)
@app.route('/form')
def form():
    form = MyForm()
    return render_template('submit.html',form=form)
