#!/usr/bin/env python
import MySQLdb

def genIDs(IDs):
	#! @param IDs a dictionary with keys of an ID for each location and a value of the stations below
	out = ""
	for key in IDs:
		out += "\t\tvar toggle"+key+" = true;\n"
	out += "\t\t$(document).ready(function() {\n"
	for key in IDs:
		out += genIDforLocation(key)
		for val in IDs[key]:
			out+=genIDforStation(val)+'\n'
	out += "});\n"
	return out
def genIDforLocation(s):
	out =( 
	'\t\t\t $("#'+s+'button").click(function() {\n'+
	'\t\t\t\t $("#'+s+'").toggle(300);\n'+
	'\t\t\t\t if (toggle'+s+') {\n'+
	"\t\t\t\t\t $('#"+s+"icon').rotate({\n"
	"\t\t\t\t\t\t angle: 0,\n"+
	"\t\t\t\t\t\t animateTo:45\n"+
	"\t\t\t\t\t });\n"+
	"\t\t\t\t } else {\n"+
	"\t\t\t\t\t $('#"+s+"icon').rotate({\n"+
	"\t\t\t\t\t\t angle: 45,\n"+
	"\t\t\t\t\t\t animateTo:0\n"+
	"\t\t\t\t\t });\n"+
	"\t\t\t\t }\n"+
	"\t\t\t\t toggle"+s+" = !toggle"+s+";\n"+
	"\t\t\t });\n"
	)
	return out
def genIDforStation(s):
	out = (
	'$("#'+s+'button").click(function() {'+
	'$("#'+s+'").toggle(300);\n});\n'
	)
	return out
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
def startBody():
	out = """
	<body>
		<div class="container-fluid"></div>
		<div class="wrapper">
		
		<h1 class="title">What's on the Buff(et)?</h1>
		<p id="taglineContent" class="tagline">Because chicken nuggets won't find themselves.</p>
		<div class="selector">
		  <ul class="nav">
				<li class="nav">today</li>
				<li class="nav">tomorrow</li>
				<li class="nav">wednesday</li>
			</ul>
		</div>
	"""
	return out
def buildLocation(TITLE,vals,hasStation=False):
	#! @param TITLE Title of Location (e.g. C4C)
	#! @param ID ID of location for the buttons, must be like a variable name
	#! @param vals if hasStation dict of Stations otherwise dict of meals and their items
	#! @param hasStation only true for the C4C, where there are stations
	out = ""
	ID = makeVariableName(TITLE);
	out += startLocation(ID,TITLE)+"\n"
	if hasStation:
		for statTitle in vals:
			statID = makeVariableName(statTitle)
			out += startStation(statID,statTitle)+"\n"
			for meal in vals[statTitle]:
				out += genMeal(meal,vals[statTitle][meal])+"\n"
			out += endStation()+"\n"
	else:
		for meal in vals:
			out += genMeal(meal,vals[meal])
	out += endLocation();
	return out
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
def endStation():
	return '</div></div>'
def genMeal(Title,Items):
	#! @param Title Title of meal (e.g. Breakfast)
	#! @param Items list of items available at that meal
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
			footer content!<br>copyright and shit I dunno<br>we made this
		</div>
		
	</body>
<html>
	'''
	return out
def makeVariableName(s):
	return ''.join(c for c in s if c.isalnum())

def GenerateSite():
	# Set up Database
	db = MySQLdb.connect(user='root',db='FamishedBuffs');
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

def main():
	#
	print 'Content-type: text/html'
	print
	print(GenerateSite())

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
	
"""
CREATE TABLE IF NOT EXISTS `Hours` (
  `ID` int(1) PRIMARY KEY AUTO_INCREMENT,
  `HallID` int(1) NOT NULL,
  `Open` varchar(6) DEFAULT NULL,
  `Close` varchar(6) DEFAULT NULL,
  `Day` varchar(10) DEFAULT NULL,
  `Meal` varchar(10) DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `Meal` (
  `ID` int(1) PRIMARY KEY AUTO_INCREMENT,
  `HallID` int(1) NOT NULL,
  `Item` varchar(64) NOT NULL,
  `HourID` int(1) NOT NULL
);
"""
