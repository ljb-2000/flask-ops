from app import app
from flask import render_template
import json

@app.route('/')
def index():
    return render_template("index.html.bak")
@app.route('/data')
def data():
    obj={'name':"aa",'value':'11'}
    return json.dumps(obj)
