# 3308Project - Famished Buffs

A web scraper and website to access and display the hours and menus of the dining centers around campus in an intuitive and easy to use way.

By:
Peter Gutenko
Seth Hovestol
Paige Johnson
Alex Okeson

#Repo Organization
All the turn in parts of the project and the README.md are in the main repo.
Notes is where we stored all the files and class notes for reference.
Testing contains the bash testing scripts. 
ResponsiveSiteMockup is code for the second mockup code of the responsive site using Bootstrap. It is very similar to siteMockup.
Backend contains all files involved in creating and updating the database and scraping menus for the database.
siteEnv is the current website and is where all the scripts are run. It is very similar to ResponsiveSiteMockup. Inside siteEnv is a subdirectory AutoDoc which contains all the autodocumentation files are stored.
siteMockup is the code for the first mockup of the website.

#How to run

There are three parts to running the website, setup, initializing the database, and running the webserver

## Setup
The setup is pretty simple. There are a few dependancies that we found that the CU virtualbox needs to install. 

###Dependancies

python package lxml 
```bash
$ pip install lxml
```

mysql:

	Ubuntu:

```bash
$ sudo apt-get install mysql
```

	IOS: 

```bash
$ brew install mysql
```

python package MySQLdb:

	Ubuntu:
	
```bash
$ sudo apt-get install python-dev libmysqlclient-dev
$ sudo apt-get install python-mysqldb		
```

## Initializing the Database
The database files are in the backend subdirectory. Firs, execute the menuScrape.py file. This will create and/or update the mealTable.sql file with current information. To run all the .sql files at once navigate to the subdirectory and run the BuildDB.sql file.
Also in siteEnv there is a file called sqlpass. Update the credentials in that is order for the site to be able to access the SQL database.

The database can also be initialized by running each of the .sql files idividually. As above, before running the files make sure that hte menuScrape.py in the backend subdirectory has been run before executing mealTable.sql. Run the following files from the backend subdirectory in order build the database:
```bash
initializeDatabase.sql
hallTable.sql
hoursTable.sql
gandgMenuTable.sql
mealTable.sql
```

## Running the webserver
The webserver can be run by going into the siteEnv folder and running `cgiScript.py`. 
finally the site is ready and you can point your browser at `127.0.0.1:8000/code.py`

#How to run the test script
The test files are all in the subdirectory Testing. To run the files, navigate to this directory and then run `./test.sh`


#Dependency of CU Menu Websites
When trying to run our scripts over Thanksgiving break, we realized that during school breaks when dining halls are not open, the CU websites do not contain files that our meal scraper relies on. This results in errors in the code. If this happens during grading, you can just use the .sql files we have provided in our Github that contain meal information from previous menus to update the database
