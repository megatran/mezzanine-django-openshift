from setuptools import setup

setup(
	name='megatran-mezzanine-django-openshift',
	version='1.0',
	description='Django 1.9x and Mezzanine 4.1x ready to be deployed to Redhat Openshift with minimum setup.',
	author='Nhan Tran',
	author_email='nhantrantnt@gmail.com',
	url='https://github.com/megatran/mezzanine-django-openshift',
	install_requires=['pip >= 8.1.2', 'mezzanine==4.1.0'], 
	)

