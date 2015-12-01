#!/usr/bin/env python

def genIDs(IDs):
	#! @param IDs a dictionary with keys of an ID for each location and a vlue of the stations below
	out = ""
	for key in IDs:
		out += genIDforLocation(key)
		for val in IDs[key]:
			out+=genIDforStation(key+val)
	return out
def genIDforLocation(s):
	out =( 
	"var toggle"+s+" = true;"+
	"$(document).ready(function() {"+
	'$("#'+s+'button").click(function() {'+
	'$("#'+s+'").toggle(300);'+
	'if (toggle'+s+') {'+
	"$('#"+s+"icon').rotate({"
	"angle: 0,"+
	"animateTo:45"+
	"});"+
	"} else {"+
	"$('#"+s+"icon').rotate({"+
	"angle: 45,"+
	"animateTo:0"+
	"});}toggle"+s+" = !toggle"+s+";});"
	)
	return out
def genIDforStation(s):
	out = (
	'$("#'+s+'").click(function() {'+
	'$("#'+s+'").toggle(300);});'
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
	<script src="js/JQueryRotate.js"></script>
	<script>
			function getContent(name) {
				console.log("getContent script called with '" + name + "'");
			}
		</script>
	<script>
			console.log("onload script called, calling getContent...");
			window.onload = getContent("menus.txt");
		</script>
	<script>"""+
	genIDs(IDs)
	+"""
			});
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
def buildLocation(TITLE,ID,vals,hasStation=False):
	#! @param TITLE Title of Location (e.g. C4C)
	#! @param ID ID of location for the buttons, must be like a variable name
	#! @param vals if hasStation dict of Stations otherwise dict of meals and their items
	#! @param hasStation only true for the C4C, where there are stations
	out = ""
	out += startLocation(ID,TITLE)
	if hasStation:
		for statID,statTitle in vals:
			out += startStation(statID,statTitle)
			for meal in vals[(statID,statTitle)]:
				out += genMeal(meal,vals[(statID,statTitle)][meal])
			out += endStation();
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
	"</h1>"+
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
	'</h1>'+
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
	return "</div></div>"
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

def main():
	#
	print(getHead({"C4C":['Persian','Asian'],'Libby':[]}))
