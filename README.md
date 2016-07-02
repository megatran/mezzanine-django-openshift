Django + Mezzanine On OpenShift
===

This project is to provide the simplest way possible to run mezzanine on the openshift stack with the best possible defaults for development and production.

Minimum setup to deploy the latest versions of Django 1.9.x and Mezzanine 4.1x to Redhat Openshift

###Features
* Ready to use for local development
* Easy to push to Openshift
* Works with  either PostgreSQL or MySQL
* Minimal changes to default django 1.9.x installation
* Uses new folder layout from Openshift March 2014 release
* Allows for debug mode on Openshift with the help of an environment variable.
* Use of static files is pre-configured
* Code formatting as per PEP8 recommendations


###How to use this repository
- Create an account at https://www.openshift.com
- Install the RHC client tools if you have not already done so.


    `sudo gem install rhc`
    `rhc setup`


- Create a Python 2.7 application, replacing mezzanineapp with your application name:


    `rhc app create mezzanineapp python-2.7 postgresql-9.2`

- Add this upstream repo

```
    cd mezzanineapp
    git remote add upstream -m master https://github.com/megatran/mezzanine-django-openshift.git
    git pull -s recursive -X theirs upstream master
```


- Set Python application environment variable like this:
    

        ``rhc env set OPENSHIFT_PYTHON_WSGI_APPLICATION=wsgi/wsgi.py --app mezzanineapp`


- Push the repo upstream


    `git push`

- SSH into the application to create a django superuser.


    `python app-root/repo/manage.py createsuperuser`


- Now use your browser to connect to the Admin site at:

` https//<your-app-name>-<your-user-name>.rhcloud.com/admin/`


### Static files
Static files are already setup and ready to use for either local or Openshift use. 

Place all static files / folders into the project-directory/static.  They will be collected with collectstatic when 
pushed to openshift.

**DO NOT PUT STATIC FILES INTO /wsgi/static/**, this is merely a place holder for the collectstatic command.

### Where do I put my HTML Templates?
You are free to place the HTML template files either on the seperate template directory or in-app template directory or
 on both.
Your HTML templates can be placed on,

 * `project/template`
 * `project/app/template`


### Running locally
This repository was designed to allow you to quickly develop and deploy a website to Openshift.  For local development, make sure you have the following setup:

- Virtualenv for this instance of python / django.
- pip (should be installed with virtualenv)

Once you have those installed, install the requirements for this repository:


    pip install -r requirements.txt


The default database and application configuration should be sufficient for local and production development.

### Configuration details
When a git push is done, the .openshift/action_hooks/deploy is executed.  This script does two things:

1.  Runs python manage.py migrate to update any changes to the Schema
2.  Runs python manage.py collectstatic to move all necessary static files into /wsgi/static

#### Debugging mode and Openshift
By default, debug mode is off when pushed to Openshift.  However, if you'd like to turn on debugging (settings.DEBUG) while running on Openshift, you can set the environment variable DEBUG to True and then stop and start your application, and debugging will be turned on.

    rhc env set DEBUG=True

### HTTPS redirection
HTTPS redirection is accompished by telling the local Apache gear to redirect all traffic to the HTTPS version of your site.  You'll need to make sure that the following lines are present in your wsgi/.httaccess file:
    
    
    ```
    RewriteEngine on
    RewriteCond %{HTTP:X-Forwarded-Proto} !https
    RewriteRule .* https://%{HTTP_HOST}%{REQUEST_URI} [R,L]  
    ```

This will redirect **ALL** HTTP traffic to the site to HTTPS.

### Notes on compatibility
This setup works with python 2.7 and 3.3. Issues, pull requests are welcome.



Fork of github.com/biwin/django-on-openshift and github.com/mush42/mushy-mezzanine-on-openshift with mezzanine required settings added and tweaked to run on openshift.

