import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, validators
from wtforms.validators import InputRequired, Length, DataRequired, EqualTo
from flask_bcrypt import Bcrypt

static_folder = os.path.abspath('../frontend/static')
template_folder = os.path.abspath('../frontend/templates')
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
basedir = os.path.abspath(os.path.dirname(__file__))
print('basedir', basedir)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SECRET_KEY'] = '%C*F-JaNdRgUkXn2r5u8x/A?D(G+KbPe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class RegisterForm(FlaskForm):
    username = StringField(label='username', validators=[
        validators.InputRequired(), validators.Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    email = StringField(label='email', validators=[
        validators.InputRequired(), validators.Length(min=6, max=30)], render_kw={"placeholder": "Email"})
    password = PasswordField(label='password', validators=[
        validators.InputRequired(), validators.EqualTo('confirm_password'), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField(label='confirm_password', validators=[
        validators.InputRequired(), validators.Length(min=8, max=20)], render_kw={"placeholder": "Confirm Password"})
    accept_tos = BooleanField('I have read and accept the Treble terms of service.', [validators.DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise app.ValidationError(
                'That username already exists. Please choose a different one.')

    def validate_password(password):
        password = input(password)
        if len(password) < 8:
            raise app.ValidationError(
                'Make sure your password is at least 8 letters.')
        elif not password.isdigit():
            raise app.ValidationError(
                'Make sure your password has a number in it.')
        elif not password.isupper(): 
            raise app.ValidationError(
                'Make sure your password has a capital letter in it.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('profile'))
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@ app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        flash('Welcome to the Treble Community!')
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

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
    app.run(debug=True, port="8080")