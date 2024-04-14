from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify
from flask_login import login_required

from plager.utils import utils
from plager.direct.forms import *
from algorithm import comparisons

import os

direct = Blueprint("direct", __name__) #Create Direct Flask blueprint.

# Direct File Comparison Page
# ---
# Allows users to upload two files for comparison, and feedbacks the similarity score.
#
# Written by: James Ashenden @psyja10, Louis Maurice @psylm11
@direct.route("/compare", methods=['GET', 'POST'])
@login_required
@utils.restrict_staff
def compare():
    direct_form = DirectForm() #Create a DirectForm object.

    use_data = request.args.get('use_data', default=False) #Get flag to use sessions data.
    if not use_data: #If flag is not set, assume no session data.
        session['data'] = {'live' : False} #Set session data to not be 

    if direct_form.validate_on_submit(): #If the form passes client-side validation.
        file1 = request.files['file1'] #Get first file from POST request.
        path1 = os.path.join(utils.get_uploads_path(), file1.filename) #Define target save path to /static/uploads/filename.
        file1.save(path1) #Save file to defined path.

        file2 = request.files['file2'] #Get second file from POST request.
        path2 = os.path.join(utils.get_uploads_path(), file2.filename) #Define target save path to /static/uploads/filename.
        file2.save(path2) #Save file to defined path.

        session['data'] = {
            'live' : True, #Flag session data to be latest.
            'file1' : file1.filename, #Pass filenames to template.
            'file2' : file2.filename,
        }

        return redirect(url_for('direct.compare', use_data=True, data=session['data'])) #Redirect to Compare page.

    return render_template('direct/direct.html', direct_form=direct_form, data=session['data']) #Render direct.html page to browser with direct_form object.


@direct.route("/direct", methods=['GET', 'POST'])
@login_required
@utils.restrict_staff
def direct_compare():

    print("====================================")

    file1 = request.args.get('file1', default=None)
    file2 = request.args.get('file2', default=None)

    print("COMPARING: " + file1 + " AND " + file2)

    path1 = os.path.join(utils.get_uploads_path(), file1)
    path2 = os.path.join(utils.get_uploads_path(), file2)

    l = file1.split('.') #Get list of strings in filename.
    file_type = l[len(l)-1] #Get the extension from the uploaded file.
    score, matches = comparisons.direct_compare(file_type.lower(), path1, path2)

    #lines1 = json.loads(requests.get(url_for('direct.get_lines', filename=file1, _external=True)).content)
    #lines2 = json.loads(requests.get(url_for('direct.get_lines', filename=file2, _external=True)).content)

    lines1 = [] #Outer array of lines.
    with open(path1) as f:
        for line in f: #For each line in the file.
            lines1.append([line, False]) #Add a nested list containing the line, and whether it is plagiarised.

    lines2 = [] #Outer array of lines.
    with open(path2) as f:
        for line in f: #For each line in the file.
            lines2.append([line, False]) #Add a nested list containing the line, and whether it is plagiarised.

    for match in matches:
        lines1[match[0]-1][1] = True
        lines2[match[1]-1][1] = True

    dict = {"score":score, "lines1":lines1, "lines2":lines2}

    return jsonify(dict)