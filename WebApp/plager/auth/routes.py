from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, current_user, login_required

from plager import db, oauth
from plager.models import Users
from plager.utils import utils
from plager.auth.forms import *

auth = Blueprint('auth', __name__) #Create Auth Flask blueprint.


# Login Page
# ---
# Allows users to login to the system using their credentials, or via OAuth services.
#
# Written by: James Ashenden @psyja10
@auth.route("/login", methods=['GET', 'POST']) #Page accessible via /login.
def login():
    if current_user.is_authenticated: #If a user is already logged in to a session.
        return redirect(url_for('main.student_dashboard')) #Redirect to Dashboard page.

    login_form = LoginForm() #Create a LoginForm object.
    if login_form.validate_on_submit(): #If the form passes client-side validation.
        user = Users.query.filter_by(email=login_form.email.data).first() #Query DB for User with matching email.

        if user == None or login_form.password.data != user.password: #If user doesn't exist or given password does not match DB password.
            flash("Login Unsuccessful. Please check your email and/or password.")
            return redirect(url_for('auth.login')) #Redirect to login page to try again.
        
        login_user(user, remember=False) #Login the user to LoginManager.
        
        return redirect(url_for('main.student_dashboard')) #Redirect to Dashboard page.

    return render_template('auth/login.html', login_form=login_form) #Render login.html page to browser with login_form object.


# Gitlab Login
# ---
# Redirects to Gitlab OAuth login, to allow users to login via Gitlab.com account.
#
# Written by: James Ashenden @psyja10
@auth.route('/login/gitlab')
def gitlab_login():
    redirect_uri = url_for('auth.gitlab_auth', _external=True)
    return oauth.gitlab.authorize_redirect(redirect_uri)


# Gitlab Authorisation Callbacl
# ---
# Redirect URI for Gitlab OAuth connections, logs user in via Gitlab.com account.
#
# Written by: James Ashenden @psyja10
@auth.route('/auth/gitlab')
def gitlab_auth():
    try:
        token = oauth.gitlab.authorize_access_token()
    except:
        flash("An error occurred while authenticating with Gitlab.com.", "danger") #Show error message.
        return redirect(url_for('auth.login')) #Redirect to login page.

    data = token['userinfo'] #Get user data from returned token.

    user = Users.query.filter_by(email=data['email']).first() #Search for user in db via email.
    if user == None: #If there is no row for this email.
        #Create Users object with Gitlab data.
        user = Users(email=data['email'],
                        name=data['name'],
                        role='student',
                        attempts=0,
                        locked=False)
        db.session.add(user) #Add the new object to the database.
        db.session.commit() #Confirm changes.

    login_user(user, remember=False) #Login the user to LoginManager.

    return redirect(url_for('main.student_dashboard')) #Redirect to Dashboard page.


# Logout Route
# ---
# Logs user out of session.
#
# Written by: James Ashenden @psyja10
@auth.route('/logout')
@login_required
def logout():
    logout_user() #Call LoginManager logout method.
    return redirect(url_for("main.home")) #Redirect to Home page.


# Create New User Route
# ---
# Allows creation of new users.
#
# Written by: James Ashenden @psyja10, Louis Maurice @psylm11
#@auth.route("/users/new", methods=["POST", "GET"]) #Define a page at "url/".
#def create_user():
#    user_form = CreateUserForm() #Create a RegisterForm object.
#    if user_form.validate_on_submit(): #If the form passes client-side validation.
#        #Check this user already exists.
#        if Users.query.filter_by(email=user_form.email.data).all(): #If a user with this email is in the database.
#            flash("An account with this email already exists.", 'error') #Show error messsage.
#            return redirect(url_for('students.create_user')) #Redirect to Register page.
#
#        name = (user_form.first_name.data.strip() + ' ' + user_form.surname.data.strip()).title() #Append First Name and Surname together.
#        school = user_form.school.data.strip().title() #Remove whitespace and force camel case.
#        #Create new User object.
#        new_user = Users(email=user_form.email.data,
#                         password=user_form.password.data,
#                         role=user_form.role.data,
#                         name=name,
#                         school=school,
#                         attempts=0,
#                         locked=False)
#        db.session.add(new_user) #Add the new object to the database.
#        db.session.commit() #Confirm changes.
#        return redirect(url_for('main.student_dashboard')) #Redirect to Dashboard page.
#
#    return render_template('auth/new_user.html', user_form=user_form) #Render home.html page to browser.


# View All Users Route
# ---
# Shows a table of all users.
#
# Written by: James Ashenden @psyja10
@auth.route("/users/all", methods=["POST", "GET"]) #Define a page at "url/".
@login_required
@utils.restrict_staff
def view_all_users():
    users = Users.query.all() #Get all rows from Users table.
    users.sort(key=lambda user: user.id, reverse=False)
    return render_template('auth/all_users.html', users=users) #Render all_users.html page to browser.

@auth.route("/users/toggle-role/<int:user_id>")
@login_required
@utils.restrict_staff
def toggle_role(user_id):
    user = Users.query.filter_by(id=user_id).first()
    if not user:
        return abort(404)
    if user.role == "student":
        user.role = "staff"
    else:
        user.role = "student"
    db.session.commit()
    return redirect(url_for("auth.view_all_users"))