from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from plager.config import Config

from authlib.integrations.flask_client import OAuth

db = SQLAlchemy() #Create SQLAlchemy object to handle database interaction.
login_manager = LoginManager() #Create LoginManager object to handle authentication.
login_manager.login_view = 'auth.login' #Set login_view attribute to app Login route.
oauth = OAuth() #Create OAuth object to handle OAuth authentication.

# Create App Function
# ---
# Creates an instance of the Web Server.
#
# Written by: James Ashenden @psyja10, Louis Maurice @psylm11
def create_app(config_class=Config):
    app = Flask(__name__) #Create Flask app object.
    app.config.from_object(config_class) #Set config of App using Config object from config.py.

    db.init_app(app) #Bind Database object to Flask app.
    login_manager.init_app(app) #Bind LoginManger object to Flask app.
    oauth.init_app(app) #Bind OAuth object to Flask app.

    #Register Gitlab as OAuth service.
    oauth.register(
        name='gitlab',
        client_id='4c260ff0f3c1bf97705fe1eefcb10a5ae1be4ee7ae8f0d0969171ff515785978',
        client_secret='5d6a4396aa887c6c42f3ae9d576a5c633e7e97ac4e2be16fab0bc600c71405b2',
        server_metadata_url='https://gitlab.com/.well-known/openid-configuration',
        client_kwargs={
            'scope': 'openid email profile'
        }
)

    from plager.main.routes import main #Import Main routes.
    from plager.auth.routes import auth #Import Auth routes.
    from plager.direct.routes import direct #Import Direct routes.
    from plager.students.routes import students #Import Students routes.
    from plager.assignments.routes import assignments #Import Students routes.
    from plager.errors.handlers import errors #Import error handling routes.

    app.register_blueprint(main) #Register Main routes with App.
    app.register_blueprint(auth) #Register Auth routes with App.
    app.register_blueprint(direct) #Register Direct routes with App.
    app.register_blueprint(students) #Register Students routes with App.
    app.register_blueprint(assignments) #Register Assignments routes with App.
    app.register_blueprint(errors) #Register error handling routes with App.
    return app