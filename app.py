"""Flask user/login-logout feedback app."""

from flask import Flask, request, render_template, redirect, session, flash
from models import db, connect_db, User, Feedback
from flask_debugtoolbar import DebugToolbarExtension
from forms import UserRegistration, LoginForm, AddFeedbackForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///feedback_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'waljf34riwantogoonvacation'

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

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
        new_user = User.register(username=form.username.data,
                                 password=form.password.data,
                                 email=form.email.data,
                                 first_name=form.first_name.data,
                                 last_name=form.last_name.data)

        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.username
        return redirect(f"/users/{new_user.username}")

    else:
        return render_template('user-registration-form.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    """ Show and handle user login form. """

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data, form.password.data)

        if user:
            session["user_id"] = user.username
            return redirect(f"/users/{user.username}")

    return render_template("user-login-form.html", form=form)


@app.route("/logout")
def logout_user():
    session.pop("user_id")
    return redirect("/")


@app.route('/users/<username>')
def show_user_details(username):
    """ Return "you made it!" if logged in. """

    if "user_id" in session and username == session["user_id"]:
        user = User.query.filter_by(username=session["user_id"]).first()
        return render_template("user-details.html", user=user, feedback_list=user.feedback)
    else:
        flash("You didn't make it!")
        return redirect("/")


@app.route("/users/<username>/delete")
def delete_user(username):

    if "user_id" in session and username == session["user_id"]:
        user = User.query.filter_by(username=session["user_id"]).first()
        db.session.delete(user)
        db.session.commit()

    return redirect('/')


@app.route("/users/<username>/feedback/add", methods=["GET", "POST"])
def add_user_feedback(username):
    if "user_id" in session and username == session["user_id"]:
        form = AddFeedbackForm()
        if form.validate_on_submit():
            title = form.title.data
            content = form.content.data
            feedback = Feedback(
                title=title, content=content, username=username)

            db.session.add(feedback)
            db.session.commit()
            return redirect(f"/users/{username}")
        else:
            return render_template("add-feedback-form.html", form=form)
    return redirect('/')


@app.route("/feedback/<feedback_id>/update", methods=["GET", "POST"])
def update_feedback(feedback_id):
    user_feedback = Feedback.query.filter_by(id=feedback_id).first()

    if session.get('user_id') == user_feedback.username:
        form = AddFeedbackForm(obj=user_feedback)
        if form.validate_on_submit():
            user_feedback.title = form.title.data
            user_feedback.content = form.content.data

            db.session.commit()
            return redirect(f"/users/{user_feedback.username}")
        else:
            return render_template("update-feedback-form.html", form=form)
    return redirect('/')


@app.route("/feedback/<feedback_id>/delete", methods=["POST"])
def delete_feedback(feedback_id):
    user_feedback = Feedback.query.filter_by(id=feedback_id).first()

    if session.get('user_id') == user_feedback.username:
        db.session.delete(user_feedback)
        db.session.commit()
        return redirect(f'/users/{user_feedback.username}')
    return redirect('/')
