from flask import Flask
from flask_socketio import SocketIO
from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

socketio = SocketIO()


def create_app(app,debug=False):
	"""Create an application."""

	# with open('data.pkl', 'w') as f:  # Python 3: open(..., 'wb')
	#     pickle.dump([db], f)

	app = Flask(__name__)
	app.debug = debug
	app.config['SECRET_KEY'] = '123'

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	socketio.init_app(app)
	return app

