from app import app
from flask import render_template
import json

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/data')
def data():
    obj={'name':"aa",'youjianyingxiao':'[120, 132, 101, 134, 90000, 230, 210]'}
    return json.dumps(obj)
