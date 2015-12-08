# 3308Project
See the Project 1 PDF for more details.


#How to run

There are three parts to running the website, setup, initializing the database, and running the webserver

## Setup
The setup is pretty simple. There are a few dependancies that we found that the CU virtualbox needs to install. These can be found in the Dependancies section.

## Initializing the Database

Also in siteEnv there is a file called sqlpass. Update the credentials in that is order for the site to be able to access the SQL database.

## Running the webserver
The webserver can be run by going into the siteEnv folder and running cgiScript.py. 
finally the site is ready and you can point your browser at 127.0.0.1:8000/code.py

#Dependancies
python package lxml 
	- "pip install lxml"
mysql 
	- Ubuntu: "sudo apt-get install mysql"
	- IOS: "brew install mysql"
python package MySQLdb
	- Ubuntu- 
		"""
		sudo apt-get install python-dev libmysqlclient-dev
		sudo apt-get install python-mysqldb
		"""

