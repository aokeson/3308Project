#!/usr/bin/python

import urllib2
from lxml import html

def hasDay(s):
	days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']
	for day in days:
		tmp = s.find(day)
		if tmp != -1:
			return True
	return False

def hasTime(s):
	reg = '[012]{0,1}[0-9]:[0-5][0-9]'
	if re.match(reg,s):
		return True
	return False 


def main():
	urlBase = "https://housing.colorado.edu"
	out = {}
	places = [
		("/center-community", 'Center for Community Dining'), #C4C is "special"
		("/dining/locations-hours/cu-run-grab-n-go","CU on the Run Grab-n-Go"),
		("/dining/locations-hours/farrandmarket","Farrand Market"),
		("/dining/locations-hours/go-fresh-farrand-grab-n-go",'Go Fresh @ farrand Grab-n-Go'),
		("/kittredgemarket",'Kittredge Market'),
		("/dining/locations-hours/libby-dining-center" ,'Libby'),
		("/dining/locations-hours/sewall-dining-center" ,'Sewall'),
		("/dining/locations-hours/sewall-market",'Sewall Market' ),
		("/dining/locations-hours/village-express-grab-n-go" ,'Village grab-n-go'),
		("/dining/locations-hours/village-market" ,'Village market'),
		("/dining/locations-hours/weathertech-cafe" ,'Weathertech'),
		("/dining/locations-hours/zellers-grab-n-go" ,'Zellers Grab-n-Go'),
	]
	for url,name in places:
		try:
			url = urlBase+url
			raw = urllib2.urlopen(url).read()
			
			html_tag = html.fromstring(raw)
			table = html_tag.find_class('dcTable')[0].getchildren()[0].getchildren()
			place = {}
			curr = ''
			for elem in table:
				for e in elem.getchildren():
					if e.tag == 'td':
						if hasDay(e.text):
							curr = e.text
							place[curr] = []
						else:
							place[curr] += [e.text]
			out[name] = place
		except IndexError:
			print name
	print out

main()
