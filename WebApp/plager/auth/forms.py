from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo

#LOGIN FORM
# ---
# For initial login screen.
#
# Written by: James Ashenden @psyja10
class LoginForm(FlaskForm):
    #Username - string, required field.
    email = StringField('Email', validators=[DataRequired()])
    #Password - string masked by dots, required field.
    password = PasswordField('Password', validators=[DataRequired()])
    #Submit Button
    submit = SubmitField('Login')


# CREATE USER FORM
# ---
# For registering new users.
#
# Written by: James Ashenden @psyja10, Louis Maurice @psylm11
class CreateUserForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    surname = StringField('Surname:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email(), EqualTo('confirm_email', message="Emails must match.")])
    confirm_email = StringField('Confirm Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Password:', validators=[DataRequired(), EqualTo('confirm_password', message="Passwords must match.")])
    confirm_password = PasswordField('Confirm Password:', validators=[DataRequired()])
    school = SelectField('School:', choices=[('Computer Science', 'Computer Science'), ('Mathematics', 'Mathematics'), ('Economics', 'Economics')])
    role = SelectField('Role:', choices=[('student', 'Student'), ('staff', 'Staff')])

    #Submit Button
    submit = SubmitField('Register')