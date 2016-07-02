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


Fork of github.com/biwin/django-on-openshift and github.com/mush42/mushy-mezzanine-on-openshift with mezzanine required settings added and tweaked to run on openshift.