# importing necessary modules
from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from app import create_app, socketio

# declaring app , some part here, some in create_app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

app = create_app(app,debug=True)

if __name__ == '__main__':
	app.debug = True
	db.create_all()
	app.secret_key = "123"
	socketio.run(app)
	
