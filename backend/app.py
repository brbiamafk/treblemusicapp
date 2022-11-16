import os
from flask import Flask, render_template, url_for, redirect, send_from_directory, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, validators
from wtforms.validators import InputRequired, Length, DataRequired, EqualTo, ValidationError
from flask_bcrypt import Bcrypt
from flask_mail import Mail

static_folder = os.path.abspath('../frontend/static')
template_folder = os.path.abspath('../frontend/templates')
app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SECRET_KEY'] = '%C*F-JaNdRgUkXn2r5u8x/A?D(G+KbPe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push()
app.config['MAIL_SERVER'] = 'trablemusicapp.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "treble_passwordreset@gmail.com"
app.config['MAIL_PASSWORD'] = "password"
mail = Mail(app)

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
    confirm_password = PasswordField(validators=[
        validators.InputRequired(), validators.Length(min=8, max=20)], render_kw={"placeholder": "Confirm Password"})
    accept_tos = BooleanField('I have read and accept the Treble terms of service.', [validators.DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        username = username.data
        existing_user_username = User.query.filter_by(username=username).first()
        if existing_user_username:
            error = 'That username already exists. Please choose a different one.'
            raise ValidationError(error)


    def validate_password(self, password):
        password = password.data
        if len(password) < 8:
            error = 'Make sure your password is at least 8 letters.'
            raise ValidationError(error)
        # I hate password rules like these haha
        # elif not password.isdigit():
        #     error = 'Make sure your password has a number in it.'
        #     raise ValidationError(error)
        # elif not password.isupper(): 
        #     error = 'Make sure your password has a capital letter in it.'
        #     raise ValidationError(error)

    def validate_email(self, email):
        #TODO use library to validate email string
        # email = email.data
        pass

class LoginForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

class ResetPasswordForm(FlaskForm):
    email = StringField(label='email', validators=[
        validators.InputRequired(), validators.Length(min=6, max=30)], render_kw={"placeholder": "Email"})
    
    submit = SubmitField('Reset Password')   

@app.route('/logo_icon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'logo_icon.ico',mimetype='image/vnd.microsoft.icon')

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
        new_user = User(username=form.username.data, password=hashed_password, email = form.email.data)
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

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/reset-password')
def resetpassword():
    form = ResetPasswordForm()
    return render_template('reset_password.html', form=form)

print(__name__)

if __name__ == '__main__':
    app.run(debug=True, port="8080")