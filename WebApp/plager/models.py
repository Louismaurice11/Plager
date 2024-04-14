from flask_login import UserMixin
from plager import login_manager, db

@login_manager.user_loader #LoginManager callback for loading User object.
def load_user(user_id):
    return Users.query.get(int(user_id)) #Return User from DB to session.

# USERS- Database Model
# ---
# Represents the Users table in the Postgres DB as an object.
#
# Written by: James Ashenden @psyja10
class Users(db.Model, UserMixin):
    __tablename__ = 'users' #Name of the table in DB.
    
    #Specifying columns in DB, their types and properties.
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String())
    role = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    school = db.Column(db.String())
    attempts = db.Column(db.Integer, nullable=False)
    locked = db.Column(db.Boolean, nullable=False)

    #Defines the relationships between columns, so changes to one column affects the column in the other table.
    enrollments = db.relationship('Enrollments', back_populates='users')
    submissions = db.relationship('Submissions', back_populates='users')


# MODULES - Database Model
# ---
# Represents the Modules table in the Postgres DB as an object.
#
# Written by: James Ashenden @psyja10
class Modules(db.Model):
    __tablename__ = 'modules' #Name of the table in DB.
    
    #Specifying columns in DB, their types and properties.
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    module_code = db.Column(db.String(), nullable=False)

    #Defines the relationships between columns, so changes to one column affects the column in the other table.
    enrollments = db.relationship('Enrollments', back_populates='modules')
    assignments = db.relationship('Assignments', back_populates='modules')


# ENROLLMENTS - Database Model
# ---
# Represents the Enrollments table in the Postgres DB as an object.
#
# Written by: James Ashenden @psyja10
class Enrollments(db.Model):
    __tablename__ = 'enrollments' #Name of the table in DB.
    
    #Specifying columns in DB, their types and properties.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))

    #Defines the relationships between columns, so changes to one column affects the column in the other table.
    users = db.relationship('Users', back_populates='enrollments')
    modules = db.relationship('Modules', back_populates='enrollments')


# ASSIGNMENTS - Database Model
# ---
# Represents the Assignments table in the Postgres DB as an object.
#
# Written by: James Ashenden @psyja10
class Assignments(db.Model):
    __tablename__ = 'assignments' #Name of the table in DB.
    
    #Specifying columns in DB, their types and properties.
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.id'))
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    date_created = db.Column(db.DateTime(), nullable=False)
    date_due = db.Column(db.DateTime())
    file_type = db.Column(db.String(), nullable=False)

    #Defines the relationships between columns, so changes to one column affects the column in the other table.
    modules = db.relationship('Modules', back_populates='assignments')
    submissions = db.relationship('Submissions', back_populates='assignments')


# SUBMISSIONS - Database Model
# ---
# Represents the Submissions table in the Postgres DB as an object.
#
# Written by: James Ashenden @psyja10
class Submissions(db.Model):
    __tablename__ = 'submissions' #Name of the table in DB.
    
    #Specifying columns in DB, their types and properties.
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignments.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(), nullable=False)
    date_submitted = db.Column(db.DateTime(), nullable=False)
    filename = db.Column(db.String(), nullable=False)
    similarity_score = db.Column(db.Integer)

    #Defines the relationships between columns, so changes to one column affects the column in the other table.
    assignments = db.relationship('Assignments', back_populates='submissions')
    users = db.relationship('Users', back_populates='submissions')
