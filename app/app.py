from flask import Flask, render_template, request, redirect, flash, url_for
from config import Config
from db import db
from models import User
#import redis

#App Created
app = Flask(__name__)

#open connection
@app.before_request
def before_request():
	db.connect()

#close connection
@app.teardown_request
def teardown_request(response):
	db.close()
	return response

app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'John' }
	posts = [
		{
			'author' : {'username' : 'Miguel'},
			'body' : 'Beautiful day in Scottland!'
		},
		{
			'author' : {'username' : 'Susan'},
			'body' : 'Spiderman movie was awesome!'
		}
	]
	return render_template('index.html', title='Flask', user=user, posts=posts) 

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		print(email)
		password = request.form.get('password')
		print(password)
		flash('Login successful for {}!'.format(email))
		return redirect('/index')
	return render_template('login.html',title='Sign In')

@app.route('/adduser', methods=['GET','POST'])
def adduser():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        age = request.form.get('age')
        User.create(username=username, email=email, age=age)
    return render_template('adduser.html',title='Add User')

@app.route('/listusers', methods=['GET'])
def getuser():
	if request.method == 'GET':
		#r = redis.Redis(host='localhost', port=6379, db=db)
		users = User.select()
		return render_template('listusers.html', title='List User', users=users)

if __name__ == '__main__':
	db.create_tables([User], safe=True)
	app.run(debug=True, host='0.0.0.0')
