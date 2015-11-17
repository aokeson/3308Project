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
	out = {}
	places = [
		("https://housing.colorado.edu/sites/default/files/menus/week_menu_table_v3.html",'Darley and Sewall'),
		('https://housing.colorado.edu/sites/default/files/menus/week_menu_table_v4.html','Farrand and Libby')
	]
	days = ['mon','tues','wed','thurs','fri','sat','sun'];
	rows = ['breakfastRow','lunchRow','dinnerRow']
	end = {}
	for url,name in places:
		raw = urllib2.urlopen(url).read()
		html_tag = html.fromstring(raw)
		place = {}
		for day in days:
			meals ={}
			for c in html_tag.find_class(day):
				menuItems = map(lambda x:x.text,c.getchildren()[0].getchildren())
				meals[c.getparent().values()[0]] = menuItems
			place[day] = meals
		end[name]=place
	print(end)

main()

