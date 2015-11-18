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

def breakfastTable(menu):
  table = open('breakfastMenuTable.sql', 'w')
  table.truncate()
  table.write('USE FamishedBuffs;\n')
  table.write("INSERT INTO 'Breakfast' ('ID', 'Day', 'Item') VALUES\n")
  for item in menu['Farrand and Libby']['mon']['breakfastRow']:
    table.write("('Libb', 'Monday', '"+item+"'),\n")
  for item in menu['Farrand and Libby']['tues']['breakfastRow']:
    table.write("('Libb', 'Tuesday', '"+item+"'),\n")
  for item in menu['Farrand and Libby']['wed']['breakfastRow']:
    table.write("('Libb', 'Wednesday', '"+item+"'),\n")
  for item in menu['Farrand and Libby']['thurs']['breakfastRow']:
    table.write("('Libb', 'Thursday', '"+item+"'),\n")
  for item in menu['Farrand and Libby']['fri']['breakfastRow']:
    table.write("('Libb', 'Friday', '"+item+"'),\n")
  for item in menu['Darley and Sewall']['mon']['breakfastRow']:
    table.write("('VilG', 'Monday', '"+item+"'),\n")
  for item in menu['Darley and Sewall']['tues']['breakfastRow']:
    table.write("('VilG', 'Tuesday', '"+item+"'),\n")
  for item in menu['Darley and Sewall']['wed']['breakfastRow']:
    table.write("('VilG', 'Wednesday', '"+item+"'),\n")
  for item in menu['Darley and Sewall']['thurs']['breakfastRow']:
    table.write("('VilG', 'Thursday', '"+item+"'),\n")
  for item in menu['Darley and Sewall']['fri']['breakfastRow']:
    table.write("('VilG', 'Friday', '"+item+"'),\n")
  for item in menu['Darley and Sewall']['sat']['breakfastRow']:
    table.write("('VilG', 'Saturday', '"+item+"'),\n")
  for item in menu['Darley and Sewall']['sun']['breakfastRow']:
    table.write("('VilG', 'Sunday', '"+item+"'),\n")
  size = table.tell()
  table.truncate(size-2)
  table.write(';')
  table.close()

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
#  print(end)
  breakfastTable(end)

main()
