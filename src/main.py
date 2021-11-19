from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template
from tensorflow.python.framework.ops import name_scope
from paragraphs import Paragraphs
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from functools import wraps
import jwt
from selenium.webdriver.common.by import By

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:5432@localhost/assignment4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

db = SQLAlchemy(app)
token_save = ""


class Clients(db.Model):
	__tablename__ = 'clients'
	id = db.Column('id', db.Integer, primary_key = True)
	login = db.Column('login', db.Unicode)
	password = db.Column('password', db.Unicode)
	token = db.Column('token', db.Unicode)
	def __init__(self, id, login, password, token):
		self.login = login
		self.password = password
		self.token = token

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    coin_name =  db.Column(db.String)

    body = db.Column(db.String)

    title = db.Column(db.String)

    link =  db.Column(db.String)

    def __init__(self, coin_name, title, body, link):

        self.coin_name = coin_name

        self.title = title

        self.body = body

        self.link = link


    def __repr__(self):

        return '<title %r>' % self.title

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		find_token = request.args.get('token')
		if not find_token:
			return '''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
		integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"> <h1 class="text-warning; style="color: black; text-align: center"> You need to input the token </h1>''', 403
		real = Clients.query.filter_by(token = find_token).first()
		if real is None:
			return '''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
		integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"> <h1 class="text-danger; style="color: black; text-align: center"> The token can't be verified... </h1>'''
		return f(*args, **kwargs)
	return decorated

db.create_all()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/token')
def token():
	return '<h2>Copy paste this token in /protected to be verified: <h2>' + token_save


@app.route('/protected')
@token_required
def protected():
	return '''
	<html>
  <head>
    <link href="https://fonts.googleapis.com/css?family=Nunito+Sans:400,400i,700,900&display=swap" rel="stylesheet">
  </head>
    <style>
      body {
        text-align: center;
        padding: 40px 0;
        background: #EBF0F5;
      }
        h1 {
          color: #88B04B;
          font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
          font-weight: 900;
          font-size: 40px;
          margin-bottom: 10px;
        }
        p {
          color: #404F5E;
          font-family: "Nunito Sans", "Helvetica Neue", sans-serif;
          font-size:20px;
          margin: 0;
        }
      i {
        color: #9ABC66;
        font-size: 100px;
        line-height: 200px;
        margin-left:-15px;
      }
      .card {
        background: white;
        padding: 60px;
        border-radius: 4px;
        box-shadow: 0 2px 3px #C8D0D8;
        display: inline-block;
        margin: 0 auto;
      }
    </style>
    <body>
      <div class="card">
      <div style="border-radius:200px; height:200px; width:200px; background: #F8FAF5; margin:0 auto;">
        <i class="checkmark">✓</i>
      </div>
        <h1>Success</h1> 
        <p>We received your token and it's correct;<br/>You can continue using our website, we verified you!</p>
      </div>
    </body>
</html>
	'''


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		usernamedata = Clients.query.filter_by(login = request.form['username'], password = request.form['password']).first()
		if usernamedata is not None: 
			token = jwt.encode({'user': usernamedata.login, 'exp':datetime.utcnow() + timedelta(minutes=15)}, app.config['SECRET_KEY'])
			global token_save 
			token_save = token
			print(token)
			update_token = Clients.query.filter_by(id = usernamedata.id).first()
			token2 = token
			update_token.token = token2
			db.session.commit()
			return render_template('web.html')
		else:
			error = 'Invalid login or password!'
			return render_template('login.html', error = error)
	return render_template('login.html')


@app.route("/coin", methods = ['POST', 'GET'])
def coin():
    if request.method == 'POST':

        coin_name = request.form['coin'].lower()

        db_articles = News.query.filter_by(coin_name = coin_name).all()

        if (db_articles):
            return render_template('web.html', articles = db_articles)

        coininfo = Paragraphs()
        articles = coininfo.get_p(coin_name)

        for article in articles:
            db.session.add(News(coin_name, article['title'], article['body'], article['link']))
        

        db.session.commit()

        return render_template('web.html', articles = articles)

    elif request.method == 'GET':
        return render_template('web.html')


if __name__ == '__main__':
    app.run(debug=True)
