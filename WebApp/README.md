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

### References
- https://www.digitalocean.com/community/tutorials/how-to-set-up-a-continuous-deployment-pipeline-with-gitlab-ci-cd-on-ubuntu-18-04
- https://docs.gitlab.com/runner/executors/shell.html
- https://docs.gitlab.com/runner/register/
- https://www.rosehosting.com/blog/how-to-deploy-flask-application-with-nginx-and-gunicorn-on-ubuntu-20-04/
- https://www.hostinger.co.uk/tutorials/how-to-set-up-nginx-reverse-proxy/
- https://www.cyberciti.biz/faq/linux-unix-running-sudo-command-without-a-password/#A_Better_Solution
- https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04
OAuth
- https://realpython.com/flask-google-login/
- https://docs.gitlab.com/ee/api/oauth2.html
- https://github.com/ityoung/gitlab-oauth-example/blob/master/main.py
- https://docs.authlib.org/en/latest/client/flask.html
- https://github.com/authlib/demo-oauth-client/blob/master/flask-google-login/app.py