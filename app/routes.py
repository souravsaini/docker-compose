from flask import render_template
from app import app

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