#!/usr/bin/python


import urllib2#, _mysql
from lxml import html
##
# Scrapes menus and returns a dict of results
#
#
def main():
	out = {}
	places = [
		("https://housing.colorado.edu/sites/default/files/menus/week_menu_table_v3.html",'Darley and Sewall'),
		('https://housing.colorado.edu/sites/default/files/menus/week_menu_table_v4.html','Farrand and Libby')
	]
	days = ['mon','tues','wed','thurs','fri','sat','sun'];
	end = {}
	for url,name in places:
		end[name]=scrapeSite(url,days)
	return end

def scrapeSite(url,fields):
	html_tag = getTree(url)
	place = {}
	for value in fields:
		place[value] = retrieveElements(html_tag,value)
	return place

def retrieveElements(tree,value):
		out ={}
		for c in tree.find_class(value):
			items = map(lambda x:x.text,c.getchildren()[0].getchildren())
			out[c.getparent().values()[0]] = items
		return out

def getTree(url):
	site = urllib2.urlopen(url)
	raw_text = site.read()
	tree = html.fromstring(raw_text)
	return tree

print(main())
