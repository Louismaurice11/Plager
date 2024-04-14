from flask import abort
from flask_login import current_user

from plager import db
from plager.models import Submissions
from algorithm import comparisons

import os
from datetime import datetime
from functools import wraps

# Restrict Staff Decorator
# ---
# Restricts access to function to staff only.
def restrict_staff(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if current_user.role != "staff":
            return abort(403)
        return function(*args, **kwargs)

    return wrapper

# Restrict Student Decorator
# ---
# Restricts access to function to staff only.
def restrict_student(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if current_user.role != "student":
            return abort(403)
        return function(*args, **kwargs)

    return wrapper


# Get Root Path Function
# ---
# Returns a string for root plager package folder.
#
# Written by: James Ashenden @psyja10
def get_root_path():
    root_path, _ = os.path.dirname(__file__).split("plager")
    return root_path + "plager/"

# Get Uploads Path Function
# ---
# Returns a string for the uploads folder.
#
# Written by: James Ashenden @psyja10
def get_uploads_path():
    return os.path.join(get_root_path(), "static/uploads/")

# Get User Uploads Path Function
# ---
# Returns a string for the path to the current user's uploads folder.
#
# Written by: James Ashenden @psyja10
def get_user_uploads():
    return os.path.join(get_uploads_path(), str(current_user.id))

# Get Assignment Submissions Function
# ---
# Returns arrary of submissions, including only the latest submission from each user.
#
# Written by: James Ashenden @psyja10
def get_assignment_submissions(assignment_id):
    submissions = Submissions.query.filter_by(assignment_id=assignment_id).all()
    submissions.sort(key=lambda sub: sub.date_submitted, reverse=True) #Sort list of submissions from latest to oldest.
    #Filter to only latest submission from each student.
    ids = []
    to_remove = []
    for submission in submissions:
        if submission.student_id in ids:
            to_remove.append(submission)
        else:
            ids.append(submission.student_id)
    for remove in to_remove:
        submissions.remove(remove)
    return submissions

# Run Assignment Comparison Function
# ---
# Compares each submission for an assignment with 
#
# Written by: James Ashenden @psyja10
def compare_submissions(assignment_id, file_type):
    submissions = get_assignment_submissions(assignment_id)

    for submission in submissions:
        print("CURRENT SUBMISSION: " + str(submission.id))
        scores = []
        other_submissions = get_assignment_submissions(assignment_id)
        other_submissions.remove(submission)
        print("SUBMISSIONS: " + str(submissions))
        print("OTHER_SUBMISSIONS: " + str(other_submissions))
        path1 = os.path.join(get_uploads_path(), str(submission.student_id) + "/" + submission.filename)
        
        for other in other_submissions:
            print("COMPARING TO: " + str(other.id))
            path2 = os.path.join(get_uploads_path(), str(other.student_id) + "/" + other.filename)
            score, _ = comparisons.direct_compare(file_type, path1, path2)
            scores.append(score)
            print("SCORE: " + str(score))
        
        print("SCORES: " + str(scores))
        if other_submissions:
            average = sum(scores) / len(scores)
        else:
            average = 0
        submission.similarity_score = average
        db.session.commit()

# Past Future Assignments Function
# ---
# Returns list of both past and future assignments by due date.
#
# Written by: James Ashenden @psyja10
def past_future_assignments(assignments):
    assignments.sort(key=lambda assignment: assignment.date_due, reverse=False)
    
    split_index = 0
    for assignment in assignments:
        if assignment.date_due < datetime.now():
            continue
        split_index = assignments.index(assignment)
        break
    past_assignments = assignments[:split_index]
    assignments = assignments[split_index:]
    
    if len(assignments) == 1:
        if assignments[0].date_due < datetime.now():
            assignments = []
            past_assignments = assignments
            
    return assignments, past_assignments
    
    
# Get Latest Score for a Submission
# ---
# Returns list of both past and future assignments by due date.
#
# Written by: James Ashenden @psyja10
def get_latest_sub_score(assignment_id, student_id):
    submissions = get_assignment_submissions(assignment_id)
    score = None
    for submission in submissions:
        if submission.student_id == student_id:
            score = submission.similarity_score
    return score