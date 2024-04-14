from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required

from datetime import datetime

from plager import db
from plager.models import Users, Modules, Assignments, Enrollments
from plager.utils import utils
from plager.students.forms import *

students = Blueprint('students', __name__) #Create Main Flask blueprint.

# Create New Module Route
# ---
# Allows creation of new modules.
#
# Written by: James Ashenden @psyja10
@students.route("/modules/new", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_staff
def create_module():
    module_form = CreateModuleForm() #Create a CreateModuleForm object.
    if module_form.validate_on_submit(): #If the form passes client-side validation.
        #Check if this module already exists.
        if Modules.query.filter_by(module_code=module_form.module_code.data.strip()).all(): #If a module with this code is in the database.
            flash("A module with this code already exists.", 'danger') #Show error messsage.
            return redirect(url_for('students.create_module')) #Redirect to Create page.

        #Create new Module object with given data.
        new_module = Modules(title=module_form.title.data.strip(),
                             module_code=module_form.module_code.data.strip())
        db.session.add(new_module) #Add the new object to the database.
        db.session.commit() #Confirm changes.
        flash("Created module " + module_form.title.data.strip() + ".", 'success') #Show confirmation message.
        return redirect(url_for('students.view_all_modules')) #Redirect to View All page.

    return render_template('students/new_module.html', module_form=module_form) #Render home.html page to browser.


# Edit Module Route
# ---
# Allows staff to edit module information.
#
# Written by: James Ashenden @psyja10
@students.route("/modules/edit/<int:module_id>", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_staff
def edit_module(module_id):
    module = Modules.query.filter_by(id=module_id).first() #Get module from database by ID.
    if not module: #If a module with given ID does not exist.
        return abort(404) #Redirect to Error page.

    module_form = CreateModuleForm() #Create a CreateModuleForm object.
    add_student_form = AddStudentByEmailModule() #Create a AddStudentByEmailModule object.

    if module_form.validate_on_submit(): #If the form passes client-side validation.
        #Check if this module already exists.
        modules = Modules.query.filter_by(module_code=module_form.module_code.data.strip()).all() #Get moduels with prospective code.
        if module.module_code != module_form.module_code.data.strip() and modules: #If the code has changed and there are other modules with this code.
            flash("Another module with this code already exists.", 'danger') #Show error messsage.
            return redirect(url_for('students.edit_module', module_id=module_id)) #Redirect to Edit page.

        #Update Module object with given data.
        module.title=module_form.title.data,
        module.module_code=module_form.module_code.data.strip()

        db.session.commit() #Confirm changes.
        flash("Updated module details.", 'success') #Show confirmation message.
        return redirect(url_for('students.view_all_modules')) #Redirect to View All page.

    elif request.method == 'GET': #When the page is loaded.
        #Set form field values to current values.
        module_form.title.data = module.title 
        module_form.module_code.data = module.module_code

    if add_student_form.validate_on_submit():
        user = Users.query.filter_by(email=add_student_form.email.data.strip()).first()
        if not user:
            flash("A user with that email does not exist.", "danger")
            return redirect(url_for('students.edit_module', module_id=module_id))

        return redirect(url_for('students.add_student_to_module', user_id=user.id, module_id=module.id))

    return render_template('students/edit_module.html', module=module, module_form=module_form, add_student_form=add_student_form) #Render home.html page to browser.


# Delete Module Route
# ---
# Allows staff to delete a module.
#
# Written by: James Ashenden @psyja10
@students.route("/modules/delete/<int:module_id>")
@login_required
@utils.restrict_staff
def delete_module(module_id):
    module = Modules.query.filter_by(id=module_id).first() #Get module from database by ID.
    if not module: #If a module with given ID does not exist.
        return abort(404) #Redirect to Error page.
    if module.assignments: #If there are assignments for this module.
        for assignment in module.assignments:
            if datetime.now() < assignment.date_due: #If assignment is due in the future.
                flash("Cannot delete module. There are active assignments still due.", 'danger')
                return redirect(url_for('students.view_all_modules'))
    
    #Delete Enrollments for Module.
    for enrollment in module.enrollments:
        db.session.delete(enrollment)

    db.session.delete(module) #Delete Module Row.
    db.session.commit()#Confirm changes.
    flash("Deleted module.", 'info') #Show confirmation message.

    return redirect(url_for('students.view_all_modules'))#Redirect to View All page.


# View All Modules Route
# ---
# Shows a table of all modules.
#
# Written by: James Ashenden @psyja10
@students.route("/modules/all", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_staff
def view_all_modules():
    modules = Modules.query.all() #Get all rows from Modules table. 
    return render_template('students/all_modules.html', modules=modules) #Render home.html page to browser.


# Add Student To Module Route
# ---
# Enrolls a student to a module.
#
# Written by: James Ashenden @psyja10
@students.route("/modules/edit/<int:module_id>/add-student/<int:user_id>", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_staff
def add_student_to_module(module_id, user_id):
    module = Modules.query.filter_by(id=module_id).first() #Get module from database by ID.
    user = Users.query.filter_by(id=user_id).first() #Get user from database by ID.
    if not module or not user: #If a module with given ID does not exist.
        flash("Failed to add student. The module or user does not exist.", "danger")
        return redirect(request.referrer)
    
    enrollment = Enrollments.query.filter_by(user_id=user_id, module_id=module_id).first()
    if enrollment:
        flash("Failed to add student. They are already enrolled in this module.", "info")
        return redirect(request.referrer)

    new_enrollment = Enrollments(user_id=user_id, module_id=module_id) #Create new Enrollment object with given data.
    db.session.add(new_enrollment) #Add the new object to the database.
    db.session.commit()#Confirm changes.
    flash("Added student to module.", "success") #Show confirmation message.
    
    return redirect(request.referrer)


# Remove Student from Module Route
# ---
# Removes a students enrollment to a module.
#
# Written by: James Ashenden @psyja10
@students.route("/modules/edit/<int:module_id>/remove-student/<int:user_id>", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_staff
def remove_student_from_module(module_id, user_id):
    module = Modules.query.filter_by(id=module_id).first() #Get module from database by ID.
    user = Users.query.filter_by(id=user_id).first() #Get user from database by ID.
    if not module or not user: #If a module with given ID does not exist.
        flash("Failed to remove student. The module or user does not exist.", "danger")
        return redirect(request.referrer)
    
    enrollment = Enrollments.query.filter_by(user_id=user_id, module_id=module_id).first()
    if not enrollment:
        flash("Failed to remove student. They are not enrolled in this module.", "danger")
        return redirect(request.referrer)

    db.session.delete(enrollment) #Delete Enrollment Row.
    db.session.commit()#Confirm changes.
    flash("Removed student from module.", "info") #Show confirmation message.
    
    return redirect(request.referrer)


# Create New Assignment Route
# ---
# Allows creation of new assignments.
#
# Written by: James Ashenden @psyja10
@students.route("/assignments/new", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_staff
def create_assignment():
    assignment_form = CreateAssignmentForm() #Create a CreateAssignmentForm object.
    if assignment_form.validate_on_submit(): #If the form passes client-side validation.
        #Create new Assignment object with given data.
        new_assignment = Assignments(module_id=assignment_form.module_id.data,
                                    title=assignment_form.title.data.strip(),
                                    description=assignment_form.description.data,
                                    date_created=datetime.now(),
                                    date_due=assignment_form.date_due.data,
                                    file_type=assignment_form.file_type.data)
        db.session.add(new_assignment) #Add the new object to the database.
        db.session.commit() #Confirm changes.
        flash("Created assignment " + assignment_form.title.data.strip() + ".", 'success') #Show confirmation message.
        return redirect(url_for('assignments.staff_all_assignments')) #Redirect to View All page.

    return render_template('students/new_assignment.html', assignment_form=assignment_form) #Render home.html page to browser.


# Edit Assignment Route
# ---
# Allows staff to update assignment details.
#
# Written by: James Ashenden @psyja10
@students.route("/assignments/edit/<int:assignment_id>", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_staff
def edit_assignment(assignment_id):
    assignment = Assignments.query.filter_by(id=assignment_id).first() #Get assignment from database by ID.
    if not assignment: #If a module with given ID does not exist.
        return abort(404) #Redirect to Error page.

    assignment_form = CreateAssignmentForm() #Create a CreateAssignmentForm object.

    if assignment_form.validate_on_submit(): #If the form passes client-side validation.
        
        if assignment.submissions:
            flash("Cannot change file type - submissions have already been made for this assignment.", 'danger') #Show error messsage.
            return redirect(url_for('students.edit_assignment', assignment_id=assignment_id)) #Redirect to Edit page.
        
        #Update Assignment object with given data.
        assignment.module_id=assignment_form.module_id.data,
        assignment.title=assignment_form.title.data.strip(),
        assignment.description=assignment_form.description.data,
        assignment.date_due=assignment_form.date_due.data,
        assignment.file_type=assignment_form.file_type.data,

        db.session.commit() #Confirm changes.
        flash("Updated assignment.", 'success') #Show confirmation message.
        return redirect(url_for('assignments.staff_all_assignments')) #Redirect to View All page.
    
    elif request.method == 'GET': #When the page is loaded.
        #Set form field values to current values.
        assignment_form.module_id.data = assignment.module_id 
        assignment_form.title.data = assignment.title 
        assignment_form.description.data = assignment.description 
        assignment_form.date_due.data = assignment.date_due 
        assignment_form.file_type.data = assignment.file_type 

    return render_template('students/edit_assignment.html', assignment=assignment, assignment_form=assignment_form) #Render home.html page to browser.


# Delete Assignment Route
# ---
# Allows staff to delete an assignment.
#
# Written by: James Ashenden @psyja10
@students.route("/assignments/delete/<int:assignment_id>")
@login_required
@utils.restrict_staff
def delete_assignment(assignment_id):
    assignment = Assignments.query.filter_by(id=assignment_id).first() #Get assignment from database by ID.
    if not assignment: #If an assignment with given ID does not exist.
        return abort(404) #Redirect to Error page.
    if assignment.submissions: #If there are submissions for this assignment.
        flash("Cannot delete assignment. Submissions have been made.", 'danger')
        return redirect(url_for('assignments.staff_all_assignments')) #Redirect to View All page.

    db.session.delete(assignment) #Delete Assignment Row.
    db.session.commit()#Confirm changes.
    flash("Deleted assignment.", 'info') #Show confirmation message.

    return redirect(url_for('assignments.staff_all_assignments'))#Redirect to View All page.

# Student View Modules Route
# ---
# Shows a table of all modules.
#
# Written by: James Ashenden @psyja10
@students.route("/my-modules", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_student
def student_my_modules():
    user = Users.query.filter_by(id=current_user.id).first() #current_user.id
    modules = [enrollment.modules for enrollment in user.enrollments]
    return render_template('students/student_my_modules.html', modules=modules) #Render home.html page to browser.
