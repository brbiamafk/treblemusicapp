import os

from flask import Flask, render_template, url_for
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

static_folder = os.path.abspath('../frontend/static')
template_folder = os.path.abspath('../frontend/templates')
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = '%C*F-JaNdRgUkXn2r5u8x/A?D(G+KbPe'
    db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('register.html')

@app.route('/collaborate')
def collaborate():
    return render_template('collaborate.html')

@app.route('/share')
def share():
    return render_template('share.html')

@app.route('/produce')
def produce():
    return render_template('produce.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/reset-password')
def reset_password():
    return render_template('reset_password.html')

print(__name__)

if __name__ == '__main__':
    app.run()