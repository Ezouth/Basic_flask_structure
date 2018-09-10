from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    name = 'Max'
    num = 3
    names = ['Connor', 'Chet', 'Todd', 'Tyler', 'Fiona', 'Tara']
    return render_template('index.html', var=name, num=num, names=names)
    #This says take our variable here and push it to the front
    #this is rendering an html file to be shown
