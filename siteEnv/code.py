#!/usr/bin/env python
# File: code.py
# Generates html for website
#
"""@package code.py
Builds webpage from sql db when called
"""
import MySQLdb
from sqlpass import password,username

## Creates the ID strings for the divs in the javascript
# @param IDs a dictionary with keys of an ID for each location and a value of the stations below
def genIDs(IDs):
	out = ""
	for key in IDs:
		out += "var toggle"+key+" = true;"
	out += "$(document).ready(function() {"
	for key in IDs:
		out += genIDforLocation(key)
		for val in IDs[key]:
			out+=genIDforStation(val)+''
	out += "});"
	return out
## Generates the slightly longer javascript ids for locations
# @param s variable name like string to identify the station
def genIDforLocation(s):
	out =( 
	' $("#'+s+'button").click(function() {'+
	' $("#'+s+'").toggle(300);'+
	' if (toggle'+s+') {'+
	" $('#"+s+"icon').rotate({"
	" angle: 0,"+
	" animateTo:45"+
	" });"+
	" } else {"+
	"$('#"+s+"icon').rotate({"+
	"angle: 45,"+
	"animateTo:0"+
	"});"+
	"}"+
	"toggle"+s+" = !toggle"+s+";"+
	"});"
	)
	return out
## Generates the ID for stations that dont' need as much as locations
# @param s string of id for station
def genIDforStation(s):
	out = (
	'$("#'+s+'button").click(function() {'+
	'$("#'+s+'").toggle(300);\n});'
	)
	return out

## Generates head of html file
#
# @param IDs a dictionary with keys of an ID for each location and a value of the stations below
# 
def getHead(IDs):
	head = (
	"""
<!DOCTYPE html>
<html>
	<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>FOOD</title>
	<link rel="stylesheet" type="text/css" href="boot.py">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
	<script src="rotate.py"></script>
	<script>
			function getContent(name) {
				console.log("getContent script called with '" + name + "'");
			}
		</script>
	<script>
			console.log("onload script called, calling getContent...");
			window.onload = getContent("menus.txt");
		</script>
	<script>\n"""+
	genIDs(IDs)+
	"""
		</script>
	<!-- Google font -->
	<link href='https://fonts.googleapis.com/css?family=Source+Sans+Pro' rel='stylesheet' type='text/css'>
	<link rel="stylesheet" href="style.py">
	<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
	<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
	<!--[if lt IE 9]>
<script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
<script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
	</head>"""
	)
	return head

##
# Returns overhead for the body of the html
# 
def startBody():
	out = """
	<body>
		<div class="container-fluid"></div>
		<div class="wrapper">
		
		<h1 class="title">What's on the Buff(et)?</h1>
		<div class="selector">
		<p id="taglineContent" class="tagline">Because chicken nuggets won't find themselves.</p>
		</div>
	"""
	return out
##
# Builds html for a specific location
# @param TITLE Title of Location (e.g. C4C)
# @param vals if hasStation dict of Stations otherwise dict of meals and their items
# @param hasStation only true for the C4C, where there are stations
#
def buildLocation(TITLE,vals,hasStation=False):
	out = ""
	ID = makeVariableName(TITLE);
	out += startLocation(ID,TITLE)
	if hasStation:
		for statTitle in vals:
			statID = makeVariableName(statTitle)
			out += startStation(statID,statTitle)
			for meal in vals[statTitle]:
				out += genMeal(meal,vals[statTitle][meal])
			out += endStation()
	else:
		for meal in vals:
			out += genMeal(meal,vals[meal])
	out += endLocation();
	return out

##
# Overhead html for a location
# @param ID a variable name string for location for javascript
# @param TITLE What the page displays as the title for the location
#
def startLocation(ID,TITLE):
	overhead = (
	"<div class=\"location\">"+
	"<div class=\"clickable\" id=\""+ID+"button\" href=\"javascript:void(0);\">"+
	"<img class=\"expandicon_location\" id=\""+ID+
	"icon\" src=\"img/icon1.png\" alt=\"\" href=\"javascript:void(0);\">"+
	"<h2 class=\"locationtitle\" >"+
	"<a class=\"title\">"+
	TITLE+
	"</a>"+
	"</h2>"+
	"</div>"+
	"<div class=\"startHidden\" id=\""+ID+"\">"
	)
	return overhead
##
# Starts the html for a specific station
# 
# 
def startStation(ID,TITLE):
	out = (
	'<div class="station">'+
	'<div class="clickable" id="'+ID+'button" href="javascript:void(0);">'+
	'<h2 class="stationtitle" >'+
	'<a class="title">'+
	TITLE+
	'</a>'+
	'</h2>'+
	'</div>'+
	'<div class="startHidden" id="'+ID+'">'
	)
	return out
##
# Balances the divs that were opened for each station
#
def endStation():
	return '</div></div>'

##
# Generates a meal card
# @param Title Title of meal (e.g. Breakfast)
# @param Items list of items available at that meal
#
def genMeal(Title,Items):
	out = (
	'<div class="meal">'+
	'<h2 class="mealtitle">'+Title+'</h2>'+
	'<ul class="menu">'
	)
	for i in Items:
		out += '<li class="menuitem" >'+i+'</li>'
	out += '</ul></div>'
	return out
def endLocation():
	return "</div></div>\n"
def endBody():
	out = '''
	<div class="push"></div> <!-- also used for sticky footer -->
	</div> <!-- wrapper -->
		<div class="footer">
			Discalimer: All information is only as good as the information provided by the University of Colorado. 
			<br>
			Garbage in, Garbage out.
			<br>
			&copy& We made this
		</div>
		
	</body>
<html>
	'''
	return out
## Removes all non alpha numeric characters
# @param s string identifier
def makeVariableName(s):
	return ''.join(c for c in s if c.isalnum())

## Pulls the whole thing together. This is where the real work is done.
def GenerateSite():
	# Set up Database
	db = MySQLdb.connect(user=username,db='FamishedBuffs',passwd=password);
	query = db.cursor()
	
	#collect one time info
	query.execute("SELECT * from DiningHalls where Station is null")
	Halls = query.fetchall()
	query.execute("SELECT * from DiningHalls where Station is not null")
	stations = query.fetchall()
	
	c4cStat = map(lambda x: makeVariableName(x[2]),stations)
	#parse collected info
	locations = map(lambda x: x[1],Halls)
	hallids = map(lambda x:str(x[0]),Halls)
	ids = map(makeVariableName,locations);
	headIdDict = {}
	for item in ids:
		if item == "C4C":
			headIdDict[item] = c4cStat
		else:
			headIdDict[item] = []
	
	page = getHead(headIdDict);
	page+=startBody()
	for (loc,hID) in zip(locations,hallids):
		if loc == "C4C":
			StationOut = {}
			for ID,_,Station in stations:
				query.execute("SELECT * from Hours where HallID="+str(ID))
				meals = query.fetchall()
				mealStrs = map(getMealStr,meals)
				mealIds = map(lambda x:str(x[0]),meals)
				mealsOut = {}
				for mId,ms in zip(mealIds,mealStrs):
					# this loop goes through the hours and gets the items
					query.execute("SELECT Item from Meal where HourID="+mId)
					mealsOut[ms]= map(lambda x:x[0],query.fetchall())
				StationOut[Station]=mealsOut
			page += buildLocation(loc,StationOut,True);
		else:
			query.execute("SELECT * from Hours where HallID="+str(hID))
			meals = query.fetchall()
			mealStrs = map(getMealStr,meals)
			mealIds = map(lambda x:str(x[0]),meals)
			mealsOut = {}
			for mId,ms in zip(mealIds,mealStrs):
				# this loop goes through the hours and gets the items
				query.execute("SELECT Item from Meal where HourID="+mId)
				mealsOut[ms]= map(lambda x:x[0],query.fetchall())
			page += buildLocation(loc,mealsOut);
	page += endBody()
	return page
## Really just calls GenerateSite
def main():
	#
	print 'Content-type: text/html'
	print
	print(GenerateSite())

## Parses sql database into a nice string for meals
def getMealStr(x):
	Day = x[4]
	Meal = x[5]
	OpenTime = x[2]
	CloseTime = x[3]
	if not OpenTime:
		return Day + " => Closed"
	elif not Meal:
		return Day + " => "+ OpenTime + " to " + CloseTime
	return Day + " " + Meal + " => "+ OpenTime + " to " + CloseTime
main()
