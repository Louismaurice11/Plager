<h3 align="center">Plager</h3>

<p align="center">
  <img src="Prototype/assets/logoBright.png" alt="Logo" width=100 height=100>
  </p>



  <p align="center">
   A comprehensive and effective plagiarism detection system for source code, designed for academic staff and students.
    <br>
  </p>



## Table of contents

- [Project Description](#brief-description)
- [Creators](#project-creators)
- [How to run](#how-to-run)


## Project Description
Plager is a web based plagiarism detection software used to highlight similiarities in offending source code files.
The software was built using Python3 and Flask for the backend and a combination of ANTLR and Python3 for the algorithm

The software can be seen in action by visiting the following link:

https://plager.co.uk/


## Project Creators

**Conor Cowley** (Developer)

- <https://projects.cs.nott.ac.uk/psycc4>

**Xavier Parnell** (Developer)

- <https://projects.cs.nott.ac.uk/psyxp1>

**Louis Maurice** (Developer)

- <https://projects.cs.nott.ac.uk/psylm11>

**James Ashenden** (Developer)

- <https://projects.cs.nott.ac.uk/psyja10>

**Hitarth Shah** (Developer)

- <https://projects.cs.nott.ac.uk/psyhs11>

**Ronnie El-Hames** (Developer)

- <https://projects.cs.nott.ac.uk/efyre1>

**Trijit Saha** (Developer)

- <https://projects.cs.nott.ac.uk/psyts15>



# Web App Configuration

The WebApp is hosted on a VM in Google Cloud at http://34.148.24.24/, which hosts both the web server and the PostgreSQL database.

## How to Deploy to Web Server
Any commits made on the #deploy-webapp branch automatically triggers a CI/CD pipeline to push the latest files to the Web Server, and reload it. Some important points to note are:

- Some files, such as ```run.py``` and ```config.py```, are configured differently for the Hosted version compared to the Local version. The pipeline is configured to copy these files from the ```/DeployConfig``` folder onto the server, therefore files should be configured as such.

## Development Process

1. Make a branch from dev-webapp for the intended feature, usually via an Issue.

2. Develop on a locally-hosted version of the WebApp, ensuring the code works as intended.

3. Merge to #dev-webapp when the feature has been implemented, deleting the source branch.

4. Merge #dev-webapp into #deploy-webapp when you want to deploy, **WITHOUT** deleting the source branch.

## How to Run the Web Server Locally

1. Pull this Repository and navigate to the ```WebApp``` folder.

2. Create a Python virtual environment using ```python3 -m venv env``` (or equivalent for your OS).

3. Activate the environment using ```source env/bin/activate``` (or equivalent for your OS).

4. Install the required libraries using ```pip3 install -r requirements.txt```.

5. *IMPORTANT*: Update ```config.py``` ```SQLALCHEMY_DATABASE_URI``` attribute with DB credentials - ask @psyja10.

6. Start the Python-Flask web server by running the ```run.py``` file, e.g. ```python3 run.py```.

7. To access the website, navigate to ```localhost:8080```.

8. To deactivate the Python virtual environment, execute the ```deactivate``` command.

Note: To add additional libraries to the requirements, ```pip3 install``` the relevant library/packages, then run ```pip3 freeze > requirements.txt``` in the ```WebApp``` folder.


