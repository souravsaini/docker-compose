from flask import Flask, render_template, request, redirect, flash, url_for
from config import Config

app = Flask(__name__)
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
	return render_template('login.html',title='Flask')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
