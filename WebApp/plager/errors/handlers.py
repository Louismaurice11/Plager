from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('error.html', title="Page Not Found - 404",
                                         message="The page you are trying to access does not exist. Please check the URL."), 404

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('error.html', title="Forbidden - 403",
                                         message="You do not have permission to do that. Please check your account."), 403

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('error.html', title="Something Went Wrong - 500",
                                         message="Server Error. Please contact the system administrator."), 500
