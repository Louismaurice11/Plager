from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, SelectField, TextAreaField
from wtforms.fields import DateTimeLocalField
from wtforms.validators import ValidationError, DataRequired, InputRequired, Email

from datetime import datetime

from plager.models import Modules
from plager.direct.forms import valid_file_extensions

# Get Modules Helper Function
#
# Returns a list of tuples in the form (Module ID, Module Title) for every module in the DB.
def get_modules():
        list = []
        modules = Modules.query.all()
        for module in modules:
            list.append( (module.id, module.title) )
        return list


# CREATE MODULE FORM
# ---
# For creating new modules.
#
# Written by: James Ashenden @psyja10
class CreateModuleForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    module_code = StringField('Module Code:', validators=[DataRequired()])

    #Submit Button
    submit = SubmitField('Create')


# ADD STUDENT TO MODULE BY EMAIL FORM
# ---
# For adding students to modules.
#
# Written by: James Ashenden @psyja10
class AddStudentByEmailModule(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    #Submit Button
    submit = SubmitField('Create')


# Due Date Validator
# ---
# Custom WTForms validator to check whether the set due date is in the future.
#
# Written by: James Ashenden @psyja10
def validate_date_due(form, field):
    if field.data <= datetime.now():
        raise ValidationError("Due Date must be in the future.")


# CREATE ASSIGNMENT FORM
# ---
# For creating new assignments.
#
# Written by: James Ashenden @psyja10
class CreateAssignmentForm(FlaskForm):
    module_id = SelectField('Module:', choices=get_modules)
    title = StringField('Title:', validators=[DataRequired()])
    description = TextAreaField('Description:', render_kw={'rows': 5})
    date_due = DateTimeLocalField('Due Date:', format='%Y-%m-%dT%H:%M', validators=[InputRequired(), validate_date_due])
    file_type = SelectField('File Type:', choices=[('c', 'C'), ('cpp', 'C++'), ('cs', 'C#'), ('java', 'Java'), ('py', 'Python')])

    #Submit Button
    submit = SubmitField('Create Assignment')