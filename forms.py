from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Optional, Email, Length

BSTRAP_CLASS: {'class': 'form-control'}
# sets HTML class attr to form-control, for input fields


class UserRegistration(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=6)])
    email = StringField('Username', validators=[
                        InputRequired(), Length(max=50)])
    first_name = StringField('Username', validators=[
                             InputRequired(), Length(max=30)])
    last_name = StringField('Username', validators=[
                            InputRequired(), Length(max=30)])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           InputRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=6)])
