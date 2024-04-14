# Software Requirements

### Purpose

The purpose of this document is to outline the system requirements for the Plagiarism Detection software project. It presents an initial, detailed interpretation of what the system should do, who the relevant stakeholders are, and analysis of how the system will be used.

This document is intended for members of Group 28, the project academic supervisor, prospective users of the system including relevant professors and other module convenors, and the COMP2002 module convenor.

### Overview

Below are several sections which outline the requirements for this project. The Overall Description Section analyses the stakeholders of the system, as well as specific use cases these stakeholders will have for the system. The System Features and Requirements section outlines specific requirements, functions and constraints which the final system must fulfil and adhere to, both Functionally and Non-Functionally. The Validation section presents the justification for the requirements shown previously, to ensure they are accurate and define the intended system.

## Overall Description

### Personas

| Persona 1            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                 | Dr Archie Davis                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Photo                | ![Photo of Archie Davis](https://natsci.source.colostate.edu/wp-content/uploads/sites/6/2020/12/Strauss-243x300.jpg)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Job Title            | Module Convenor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Age                  | 40                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Background and Tasks | Archie is a highly experienced Computer Scientist who holds a PhD. He spends much of time researching for the Univsersity in his field, alongside teaching 1st year students. As well as grading his students' work, one of his concerns is reviewing them carefully to check for plagiarism. <br><br> Currently, Archie spends his work time: <br>- Giving lectures to his students about his module. <br>- Answering questions asked by students relating to the module. <br>- Reviewing and grading his students' submitted assignments. <br>- Manually checking each of his students' submitted assignments for plagiarism. |
| Environment          | Archie always has access to a computer, whether it's his personal laptop or his desktop in his office in the Computer Science building. If he's not in his office, he is in a lecture theatre or at home, where he does not have direct access to the School of Computer Science servers.                                                                                                                                                                                                                                                                                                                                       |
| Quote                | "I will have your assignments reviewed and graded by end of this semester."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Familar Software     | Archie currently uses and has experience with: <br>- TurnItIn <br>- Moodle <br>- Microsoft Office Suite <br>- Git and Gitlab                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

| Persona 2            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name                 |  Lucy Brown                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Photo                | ![Photo of Lucy Brown](https://media-exp1.licdn.com/dms/image/C4D03AQHmW6SbhPw0mQ/profile-displayphoto-shrink_800_800/0/1600099331949?e=2147483647&v=beta&t=Lgxs9XbVNNpnZdgoOriJQpDGlO9sjoxrO7fEr6DP6Bk)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Job Title            | Computer Science Tutor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Age                  | 23                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Background and Tasks | Lucy is currently a PhD Computer Science candidate, having already graduated with her Masters and Bachelors degree. Alongisde her own study and research, she is a tutor for Archie's module, teaching a small group of students about the current week's module content on a regular basis. One of her concerns is making sure all students are submitting their own code for each assignment. <br><br> Lucy spends her work time: <br>- Teaching tutorials and providing one on one support to students. <br>- Marking and grading her student's assignments. <br>- Maintaining communication between the module convenor and the students. |
| Environment          | Lucy teaches tutorials and completes her research in the Computer Science building. She often studies in this building, but sometimes works at home.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Quote                | "Make sure your assignment is submitted by next Monday."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Familar Software     | Lucy used Moodle, TurnItIn and Git/Gitlab as a student to submit her own assignments, and currently uses these systems to manage her students' work. She is also familiar with the Microsoft Office Suite.                                                                                                                                                                                                                                                                                                                                                                                                                                      |

| Persona 3            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                 | Harvey Fletcher                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Photo                | ![Photo of Harvey Fletcher](https://www.superprof.co.uk/images/teachers/teacher-home-biomedical-sciences-student-with-teaching-experience-offering-biology-level-and-maths-gcse-lessons-oxford.jpg)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Job Title            | Computer Science Student                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Age                  | 20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Background and Tasks | Harvey is a developing Computer Scientist, currently on track to recieve a 2:1 in his Bachelors degree in the subject. As a Computer Science student, he is experienced in using a computer and spends much of his time on his laptop. Harvey is a very motivated student and has opted to be a mentor for 1st year students. One of his concerns is ensuring he does not break his university's academic code of conduct by submitting a plagiarised assignment. <br><br> Harvey spends his work time: <br>- Attending lectures for all his modules.<br>- Completing his set assignments before deadlines.<br>- Studying outside of lectures to build his knowledge on taught subjects. |
| Environment          | Harvey attends his lectures on campus in person, making notes using his laptop. He often studies in the Computer Science building using school computers, as well as at home.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Quote                | "I need to submit my code before this Monday."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Familar Software     | Harvey currently uses Moodle, TurnItIn and Git/Gitlab as to submit his assignments and view module material. He also uses the Microsoft Office Suite.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

### User Stories

| No. | User Story                                                                                                                                                                                                                                       |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | As a **Computer Science tutor**, I want to be able to **_view source code similarities_** so that I can _easily identify whether a student has plagiarised work or not_.                                                                         |
| 2   | As a **module convenor** I want to be able to **_view a student’s history of suspected plagiarism_** so that I can have _extra context when making decisions on alleged malpractice within coursework or exams_.                                 |
| 3   | As a **student**, I want to be able to **_view areas of suspected plagiarism within my work_** so that I can _ensure I have correctly cited quotes from given sources._                                                                          |
| 4   | As a **Computer Science tutor**, I want to be able to **_see where in a file plagiarism has taken place_** so that I can _present evidence to the academic misconduct panel_.                                                                    |
| 5   | As a **module convenor** I want to be able to **_set students assignments_** so that I can have _them upload their answers and process their submissions to check for plagiarism_.                                                               |
| 6   | As a **student**, I want to be able to **_view the assignments I have been set_** so that I can _ensure I upload and submit on time._                                                                                                            |
| 7   | As a **module convenor** I want to be able to **_see areas where similar commits were made in seperate Git repositories_** so that I can have _decide whether the timing suggests plagiarism may have been commited and infer who was at fault_. |

### Scenarios

|            | Scenario 1                                                                                                                                                                                                                                                                                                                                                       |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title/Goal | Checking for areas of similarity between code submissions                                                                                                                                                                                                                                                                                                        |
| Overview   | People - married woman, computer literate, module convenor. Context - office in Computer Science building. Technology - MacBook                                                                                                                                                                                                                                  |
| Details    | Staff runs plagiarism checker on a specified git repo, the program will analyse the source code files. Each will be given a score based on how original/similar it is to others. Files above a certain threshold will be highlighted. Staff will then be able to click on different offending files to see the similarities.                                     |
| Notes      | Staff might select wrong repo - when selecting, program will ask for a confirmation of selecting the repo chosen, if click no, will return to repo selection screen. After reviewing the similarities themselves, the staff member will be able to flag up the students who submitted the offending files, and deal with it following the University guidelines. |

|            | Scenario 2                                                                                                                                                           |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Title/Goal | Checking for Git commit histories to determine when changes made in time                                                                                             |
| Overview   | People - single man, not good at using computer, module convenor. Context - office in Computer Science building. Technology - Windows desktop                        |
| Details    | Staff selects repos, clicks history - can see when commits were made + whether commits were made in close proximity i.e. within minute of each other                 |
| Notes      | Staff might select wrong repo - when selecting, program will ask for a confirmation of selecting the repo chosen, if click no, will return to repo selection screen. |

## System Features and Requirements

### 3.1 Functional Requirements

The requirements below detail functions the user of the system needs to be able to complete, and by extension the functions that the software will include. They are split into individual features which could be completed in a sprint cycle.

#### 3.1.1 Similarity Algorithm

| No.     | Requirement                                                     |
| ------- | --------------------------------------------------------------- |
| 3.1.1.1 | The similarity algorithm should give a score between 0 and 100. |
| 3.1.1.2 | The similarity algorithm should check for Direct Plagiarism.    |
| 3.1.1.3 | The similarity algorithm should check for Mosaic Plagiarism.    |

#### 3.1.2 Direct File Comparison

| No.     | Requirement                                                                       |
| ------- | --------------------------------------------------------------------------------- |
| 3.1.2.1 | Staff should be able to upload source code files.                                 |
| 3.1.2.2 | Staff should be able to select 2 source code files for comparison.                |
| 3.1.2.3 | Staff should be able to see the similarity score between 2 source code files.     |
| 3.1.2.4 | Staff should be able to see the areas of each source code file which are similar. |

#### 3.1.3 Batch File Comparison

| No.     | Requirement                                                                               |
| ------- | ----------------------------------------------------------------------------------------- |
| 3.1.3.1 | Staff should be able to select multiple source code files for comparison.                 |
| 3.1.3.2 | Staff should be able to see the similarity score between all selected source codes files. |
| 3.1.3.3 | Staff should be able to see the areas of each source code file which are similar.         |

#### 3.1.4 Git History Comparison

| No.     | Requirement                                                                                              |
| ------- | -------------------------------------------------------------------------------------------------------- |
| 3.1.4.1 | Staff should be able to select multiple Git respositories to compare.                                    |
| 3.1.4.2 | Staff should be able to select Git respositories from Gitlab.                                            |
| 3.1.4.3 | Staff should be able to see when similar commits have been made in selected repositories.                |
| 3.1.4.4 | Staff should be able to see the similarity score between the source code files in selected respoitories. |

#### 3.1.5 User Operations

| No.     | Requirement                                   |
| ------- | --------------------------------------------- |
| 3.1.5.1 | Users should be able to log in.               |
| 3.1.5.2 | Users should be able to reset their password. |
| 3.1.5.3 | Users should be able to log out.              |

#### 3.1.6 Student User Management

| No.     | Requirement                                                                  |
| ------- | ---------------------------------------------------------------------------- |
| 3.1.6.1 | Staff should be able to create students.                                     |
| 3.1.6.2 | Staff should be able to remove students.                                     |
| 3.1.6.3 | Staff should be able to create groups.                                       |
| 3.1.6.4 | Staff should be able to remove groups.                                       |
| 3.1.6.5 | Staff should be able to add students to groups.                              |
| 3.1.6.6 | Staff should be able to remove students from groups.                         |
| 3.1.6.7 | Staff should be able to see a history of students past plagiarism incidents. |

#### 3.1.7 Student Submission

| No.      | Requirement                                                                                                             |
| -------- | ----------------------------------------------------------------------------------------------------------------------- |
| 3.1.7.1  | Students should be able to view their assignments.                                                                      |
| 3.1.7.2  | Students should be able to upload their source code file to an assignment.                                              |
| 3.1.7.3  | Students should be able to see the similarity score before submission if staff allows.                                  |
| 3.1.7.4  | Students should be able to submit their source code file.                                                               |
| 3.1.7.5  | Staff should be able to create assignments.                                                                             |
| 3.1.7.6  | Staff should be able to assign students to an assignment.                                                               |
| 3.1.7.7  | Staff should be able to assign groups to an assignment.                                                                 |
| 3.1.7.8  | Staff should be able to set whether students can see the similarity score for their source code file before submission. |
| 3.1.7.9  | Staff should be able to set a due date for assignments.                                                                 |
| 3.1.7.10 | Staff should be able to see the similarity score between all source code files submitted to an assignment.              |

### 3.2 Non-Functional Requirements

The requirements below detail constraints on what the user needs to do, and how well the system performs.

#### 3.2.1 Security

| No.     | Requirement                                                             |
| ------- | ----------------------------------------------------------------------- |
| 3.2.1.1 | The system should encrypt all sensitive data that it stores.            |
| 3.2.1.2 | The system should ensure only relevant users can see similarity scores. |

#### 3.2.2 Compatibility

| No.     | Requirement                                                          |
| ------- | -------------------------------------------------------------------- |
| 3.2.2.1 | The system should be accessible on Windows, macOS and Linux systems. |
| 3.2.2.2 | The system should only accept C and Python source code files.        |

#### 3.2.3 Scalability

| No.     | Requirement                                                                                            |
| ------- | ------------------------------------------------------------------------------------------------------ |
| 3.2.3.1 | The system should be able to compare 2 source code that are 100 lines long files within 30 seconds.    |
| 3.2.3.2 | The system should be able to compare 100 source codes files that are 100 lines long within 5 minutes.  |
| 3.2.3.3 | The system should be able to compare 300 source codes files that are 100 lines long within 10 minutes. |

## Validation

//Internal and external validation

## References

https://assets.asana.biz/m/d8e9793595d9978/original/software-requirement-document-template.pdf

https://www.reqview.com/papers/ReqView-Example_Software_Requirements_Specification_SRS_Document.pdf

https://www.cse.msu.edu/~chengb/RE-491/Papers/SRSExample-webapp.doc

COMP1003
