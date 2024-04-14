from flask import Blueprint, render_template, redirect, url_for

from plager.models import Assignments, Submissions, Users
from plager.utils import utils
from flask_login import current_user, login_required

from datetime import datetime

main = Blueprint('main', __name__) #Create Main Flask blueprint.

# Main Route
# ---
#
# Written by: James Ashenden @psyja10
@main.route("/") #Define a page at "url/".
def home():
    return render_template('main/home.html') #Render home.html page to browser.

@main.route("/dashboard/staff")
@login_required
@utils.restrict_staff
def staff_dashboard():
    
    assignments = Assignments.query.filter(Assignments.date_due >= datetime.now()).all()
    submissions = Submissions.query.filter(Submissions.assignments.has(Assignments.date_due >= datetime.now())).filter(Submissions.similarity_score >= 70).all()
    
    return render_template('main/staff_dashboard.html', assignments=assignments, submissions=submissions) #Render home.html page to browser.

@main.route("/dashboard")
@login_required
def student_dashboard():
    if current_user.role == "staff":
        return redirect(url_for("main.staff_dashboard"))
    
    user = Users.query.filter_by(id=current_user.id).first()
    modules = [enrollment.modules for enrollment in user.enrollments]
    assignments = []
    for module in modules:
        for assignment in module.assignments:
            assignments.append(assignment)
            
    assignments, _ = utils.past_future_assignments(assignments)
    
    #assignments = Assignments.query.filter(Assignments.date_due >= datetime.now()).filter(Assignments.modules.enrollments.user_id == current_user.id).all()
    submissions = Submissions.query.filter(Submissions.assignments.has(Assignments.date_due >= datetime.now())).filter_by(student_id=current_user.id).all()
    
    return render_template('main/student_dashboard.html', assignments=assignments, submissions=submissions) #Render home.html page to browser.