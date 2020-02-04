from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Optional, Email, Length

BSTRAP_CLASS: {'class': 'form-control'}
# sets HTML class attr to form-control, for input fields


class UserRegistration(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(), Length(max=20)],
                           render_kw=BSTRAP_CLASS)
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=6)],
                             render_kw=BSTRAP_CLASS)
    email = StringField('Email',
                        validators=[InputRequired(), Length(max=50)],
                        render_kw=BSTRAP_CLASS)
    first_name = StringField('First Name',
                             validators=[InputRequired(), Length(max=30)],
                             render_kw=BSTRAP_CLASS)
    last_name = StringField('Last Name',
                            validators=[InputRequired(), Length(max=30)],
                            render_kw=BSTRAP_CLASS)


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(), Length(max=20)],
                           render_kw=BSTRAP_CLASS)
    password = PasswordField('Password',
                             validators=[InputRequired(), Length(min=6)],
                             render_kw=BSTRAP_CLASS)


class AddFeedbackForm(FlaskForm):
    title = StringField("Title",
                        validators=[InputRequired(), Length(max=100)])
    content = TextAreaField("Content",
                            validators=[InputRequired()])
