from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class AddUserForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

class EditUserForm(FlaskForm):
    """Form for editing users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    image_url = StringField('(Optional) Image URL')
    header_image_url = StringField('(Optional) Header Image URL')
    bio = StringField('Bio')
    password = PasswordField('Password', validators=[Length(min=6)])

class BeforeSurveyForm(FlaskForm):
    """'Before' survey form."""


class AfterSurveyForm(FlaskForm):
    """'After' survey form."""