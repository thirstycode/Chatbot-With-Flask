from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
from flask import Flask, url_for, render_template, request, redirect, session
# from flask_sqlalchemy import flask_sqlalchemy
from __main__ import db

class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

@main.route('/', methods=['GET', 'POST'])
def home():
    """ Session control"""
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        # try:
        data = User.query.filter_by(username=name, password=passw).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('main.chatroom'))
        else:
            return 'Wrong Username or Password'
        # except:
        #     return "Dont Login2"

@main.route('/register/', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        new_user = User(username=request.form['username'], password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')

@main.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('main.home'))

@main.route('/chatroom', methods=['GET', 'POST'])
def chatroom():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        """Login form to enter a room."""
        form = LoginForm()
        if form.validate_on_submit():
            session['name'] = form.name.data
            session['room'] = form.room.data
            return redirect(url_for('.chat'))
        elif request.method == 'GET':
            form.name.data = session.get('name', '')
            form.room.data = session.get('room', '')
        return render_template('chatroom.html', form=form)

@main.route('/chat')
def chat():
    if not session.get('logged_in'):
        return render_template('index.html')
        return "fail"
    else:
        """Chat room. The user's name and room must be stored in
        the session."""
        name = session.get('name', '')
        room = session.get('room', '')
        if name == '' or room == '':
            return redirect(url_for('.chatroom'))
        return render_template('chat.html', name=name, room=room)

