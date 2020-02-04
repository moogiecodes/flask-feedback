"""Flask user/login-logout feedback app."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db, User
from flask_debugtoolbar import DebugToolbarExtension
from forms import UserRegistration

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'waljf34riwantogoonvacation'

toolbar = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def root():
    """ Redirect to /register. """

    return redirect('/register')


@app.route('/register', methods=['GET', 'POST'])
def register_form():
    """ Show and handle user registration form. """

    form = UserRegistration()

    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        password=form.password.data,
                        email=form.email.data,
                        first_name=form.first_name.data,
                        last_name=form.last_name.data)

        db.session.add(new_user)
        db.session.commit()
        return redirect('/secret')

    else:
        return render_template('user-registration-form.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    """ Show and handle user login form. """


@app.route('/secret')
def logged_in():
    """ Return "you made it!" if logged in. """

    return "You made it!"
