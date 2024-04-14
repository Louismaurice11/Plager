from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import ValidationError, DataRequired, InputRequired, Email

# UPLOAD SUBMISSION FORM
# ---
# For students uploading a submission.
#
# Written by: James Ashenden @psyja10, Louis Maurice @psylm11
class UploadSubmissionForm(FlaskForm):
    file = FileField('File', validators=[DataRequired()])
    submit = SubmitField('Upload')