from replit import db
from flask import Flask, request, redirect

marach = Flask(__name__)

@marach.route('/register', methods=['POST'])
def register():
  form = request.form
  if form['username'] not in db.keys():
    db[form['username']] = form
    return redirect('/login1')
  else:
    return 'User already Exists!'


@marach.route('/login', methods=['POST'])
def login():
  form = request.form
  keys = db.keys()
  if form['username'] in keys:
    if form['username'] == db[form['username']]['password']:
      return f"Hello {db[form['username']]['name']}. Kindly refresh to go back to homepage"
    else:
      return 'Incorrect Login details. Refresh to go back to homepage'
  return 'Incorrect Login details. Refresh to go back to homepage'


@marach.route('/')
def home():
  homepage = ''
  file = open('homepage.html', 'r')
  homepage = file.read()
  file.close()
  return homepage
  

@marach.route('/register1')
def register1():
  file = open('signup.html', 'r')
  page = file.read()
  file.close()
  
  return page

@marach.route('/login1')
def login1():
  page = ''
  file = open('login.html', 'r')
  page = file.read()
  file.close()
  
  return page

marach.run(host='0.0.0.0', port=81)
