from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired, ValidationError

# File Extension Validator
# ---
# Custom WTForms validator to check whether the file type of an uploaded file is corerct.
#
# Written by: James Ashenden @psyja10
valid_file_extensions = ['c', 'cpp', 'java', 'py', 'cs'] #List of extensions of valid file types.
def check_file_type(form, field):
    try:
        list = field.data.filename.split('.') #Get the extension from the uploaded file.
        extension = list[len(list)-1]
    except:
        raise ValidationError("An error occurred uploading a file.")
    if extension.lower() not in valid_file_extensions: #If the extension isn't in the valid list.
        raise ValidationError("Please select a valid source file.") #Raise WTForms ValidationError.

# DIRECT FORM
# ---
# For direct comparison of two files.
#
# Written by: James Ashenden @psyja10
class DirectForm(FlaskForm):
    #First File for Comparison - required field.
    file1 = FileField('File 1', validators=[DataRequired(), check_file_type])
    #First File for Comparison - required field.
    file2 = FileField('File 2', validators=[DataRequired(), check_file_type])
    #Submit Button
    submit = SubmitField('Plager It!')

    def validate(self, extra_validators):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
 
        l1 = self.file1.data.filename.split('.')  #Get list of strings in filename.
        ext1 = l1[len(l1)-1] #Get the extension from the uploaded file.
        l2 = self.file2.data.filename.split('.') #Get list of strings in filename.
        ext2 = l2[len(l2)-1] #Get the extension from the uploaded file.

        if ext1.lower() != ext2.lower():
            self.file2.errors.append("Files must be of the same type.")
            return False

        return True