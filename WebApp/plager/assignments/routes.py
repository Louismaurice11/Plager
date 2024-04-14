from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required
from sqlalchemy import and_

from datetime import datetime
import os

from plager import login_manager, db
from plager.models import Users, Modules, Assignments, Enrollments, Submissions
from plager.utils import utils
from plager.assignments.forms import *

assignments = Blueprint('assignments', __name__) #Create Main Flask blueprint.

# Student My Assignments Route
# ---
# Displays list of assignments for students.
#
# Written by: James Ashenden @psyja10
@assignments.route("/my-assignments", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_student
def student_my_assignments():
    user = Users.query.filter_by(id=current_user.id).first() #current_user.id
    modules = [enrollment.modules for enrollment in user.enrollments]
    assignments = []
    for module in modules:
        for assignment in module.assignments:
            assignments.append(assignment)
        
    assignments, past_assignments = utils.past_future_assignments(assignments)
    
    submitted_assignments = []
    for assignment in assignments:
        for submission in assignment.submissions:
            if submission.student_id == current_user.id:
                submitted_assignments.append(assignment.id)

    return render_template('assignments/student_my_assignments.html', assignments=assignments, past_assignments=past_assignments, submitted_assignments=submitted_assignments) #Render home.html page to browser.

@assignments.context_processor
def utility_processor():
    def get_assignment_submissions(assignment_id):
        subs = utils.get_assignment_submissions(assignment_id)
        return subs
    def get_latest_sub_score(assignment_id, student_id):
        score = utils.get_latest_sub_score(assignment_id, student_id)
        return score
    return dict(get_assignment_submissions=get_assignment_submissions, get_latest_sub_score=get_latest_sub_score)

# Staff View All Assignments Route
# ---
# Shows a table of all assignments.
#
# Written by: James Ashenden @psyja10
@assignments.route("/assignments", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_staff
def staff_all_assignments():
    assignments = Assignments.query.all() #Get all rows from Assignments table.
    assignments, past_assignments = utils.past_future_assignments(assignments)
    return render_template('assignments/staff_all_assignments.html', assignments=assignments, past_assignments=past_assignments) #Render home.html page to browser.


# Student View Route
# ---
# Shows details of assignments to students.
#
# Written by: James Ashenden @psyja10
@assignments.route("/assignment/<int:assignment_id>", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_student
def student_view_assignment(assignment_id):
    upload_form = UploadSubmissionForm()
    
    assignment = Assignments.query.filter_by(id=assignment_id).first()
    submissions = Submissions.query.filter_by(assignment_id=assignment_id).filter_by(student_id=current_user.id).all()
    submissions.sort(key=lambda sub: sub.date_submitted, reverse=True) #Sort list of submissions from latest to oldest.

    if upload_form.validate_on_submit():

        file = request.files['file'] #Get file from POST request.

        l = file.filename.split('.') #Get list of strings in filename.
        file_type = l[len(l)-1] #Get the extension from the uploaded file.
        
        #Check assignment not overdue.
        if assignment.date_due < datetime.now():
            flash("Cannot make a submission for this assignment - the due date has passed.", "danger") #Show error message.
            return redirect(url_for('assignments.student_view_assignment', assignment_id=assignment_id)) #Redirect to Assignment view.

        #Check uploaded file type matches assignment file type.
        if file_type != assignment.file_type:
            flash("Incorrect file type for assignment.", "danger") #Show error message.
            return redirect(url_for('assignments.student_view_assignment', assignment_id=assignment_id)) #Redirect to Assignment view.

        #Save file to user's uploads folder.
        path = os.path.join(utils.get_user_uploads(), file.filename)
        try:
            file.save(path)
        except:
            os.mkdir(utils.get_user_uploads())
            file.save(path)
            
        new_submission = Submissions(assignment_id=assignment_id,
                                     student_id=current_user.id,
                                     status="submitted",
                                     date_submitted=datetime.now(),
                                     filename=file.filename)
        db.session.add(new_submission)
        db.session.commit()
        
        flash("Successfully uploaded submission.", "success")
        return redirect(url_for('assignments.student_view_assignment', assignment_id=assignment_id)) #Redirect to Assignment view.

    return render_template('assignments/student_view_assignment.html', assignment=assignment, upload_form=upload_form, submissions=submissions) #Render home.html page to browser.

# Delete Submission Route
# ---
# Allows student to delete a submission.
#
# Written by: James Ashenden @psyja10
@assignments.route("/assignment/delete/<int:submission_id>")
@login_required
@utils.restrict_student
def delete_submission(submission_id):
    submission = Submissions.query.filter_by(id=submission_id).first() #Get assignment from database by ID.
    if not submission: #If an assignment with given ID does not exist.
        return abort(404) #Redirect to Error page.

    if submission.student_id != current_user.id:
        return abort(403)
    
    assignment_id = submission.assignment_id
    db.session.delete(submission) #Delete Assignment Row.
    db.session.commit()#Confirm changes.
    flash("Removed submission.", 'info') #Show confirmation message.

    return redirect(url_for('assignments.student_view_assignment', assignment_id=assignment_id))#Redirect to Assignment page.


# Staff View Route
# ---
# Shows details of assignments to staff.
#
# Written by: James Ashenden @psyja10
@assignments.route("/assignment/staff/<int:assignment_id>", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_staff
def staff_view_assignment(assignment_id):  
    assignment = Assignments.query.filter_by(id=assignment_id).first()
    submissions = utils.get_assignment_submissions(assignment_id)
    utils.compare_submissions(assignment_id, assignment.file_type)
    
    temp = []
    unsubmitted_users = assignment.modules.enrollments
    for student in unsubmitted_users:
        for submission in submissions:
            if submission.student_id == student.user_id:
                temp.append(student)
    print(temp)
    for u in temp:
        try:
            unsubmitted_users.remove(u)
        except:
            pass

    return render_template('assignments/staff_view_assignment.html', assignment=assignment, submissions=submissions, unsubmitted_users=unsubmitted_users) #Render home.html page to browser.
