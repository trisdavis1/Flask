from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tristan'}
    classes = [{'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Boaqiang Yan'},
               {'classInfo': {'code': 'CSC374', 'title': 'Linux Administration'}, 'instructor': 'Boaqiang Yan'},
               {'classInfo': {'code': 'CSC346', 'title': 'Enterprise Systems Java'}, 'instructor': 'Evan Noyneart'},
               {'classInfo': {'code': 'CSC386', 'title': 'Operating Systems'}, 'instructor': 'Yipkei Kwok'},
               {'classInfo': {'code': 'HIS210', 'title': 'Early Modern Europe'}, 'instructor': 'Angela Haas'}]
    return render_template('index.html', title='Home', user=user, classes=classes)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
