"""Flask Login Example and instagram fallowing find"""

from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from app import create_app, socketio



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# class User(db.Model):
#     """ Create user table"""
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     password = db.Column(db.String(80))

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

app = create_app(app,debug=True)
# Saving the objects:
# with open('data.pkl', 'w') as f:  # Python 3: open(..., 'wb')
#     pickle.dump([db], f)
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app = Flask(__name__)
# app.debug = debug
# app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'



if __name__ == '__main__':
	app.debug = True

	# class User(db.Model):
	#     # global db
	#     """ Create user table"""
	#     id = db.Column(db.Integer, primary_key=True)
	#     username = db.Column(db.String(80), unique=True)
	#     password = db.Column(db.String(80))

	#     def __init__(self, username, password):
	#         self.username = username
	#         self.password = password

	db.create_all()

	app.secret_key = "123"
	# User = User(db.username,db.password)
	# app.run(host='0.0.0.0')
	socketio.run(app)
	