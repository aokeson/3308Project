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
  table.write("INSERT INTO `Breakfast` (`ID`, `Day`, `Item`) VALUES\n")
  for item in menu['Farrand and Libby']['mon']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Monday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['tues']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Tuesday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['wed']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Wednesday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['thurs']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Thursday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['fri']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Friday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['mon']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Monday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['tues']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Tuesday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['wed']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Wednesday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['thurs']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Thursday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['fri']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Friday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['sat']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Saturday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['sun']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Sunday', \""+item[:-1]+"\"),\n")
  size = table.tell()
  table.truncate(size-2)
  table.write(';')
  table.close()

def lunchTable(menu):
  table = open('lunchMenuTable.sql', 'w')
  table.truncate()
  table.write('USE FamishedBuffs;\n')
  table.write("INSERT INTO `Lunch` (`ID`, `Day`, `Item`) VALUES\n")
  for item in menu['Farrand and Libby']['mon']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Monday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['tues']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Tuesday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['wed']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Wednesday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['thurs']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Thursday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['fri']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Friday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['mon']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Monday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['tues']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Tuesday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['wed']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Wednesday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['thurs']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Thursday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['fri']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Friday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['sat']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Saturday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['sun']['lunchRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Sunday', \""+item[:-1]+"\"),\n")
  size = table.tell()
  table.truncate(size-2)
  table.write(';')
  table.close()

def dinnerTable(menu):
  table = open('dinnerMenuTable.sql', 'w')
  table.truncate()
  table.write('USE FamishedBuffs;\n')
  table.write("INSERT INTO `Dinner` (`ID`, `Day`, `Item`) VALUES\n")
  for item in menu['Farrand and Libby']['mon']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Monday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['tues']['breakfastRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Tuesday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['wed']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Wednesday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['thurs']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Thursday', \""+item[:-1]+"\"),\n")
  for item in menu['Farrand and Libby']['fri']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('Libb', 'Friday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['mon']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Monday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['tues']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Tuesday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['wed']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Wednesday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['thurs']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Thursday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['fri']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Friday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['sat']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Saturday', \""+item[:-1]+"\"),\n")
  for item in menu['Darley and Sewall']['sun']['dinnerRow']:
    item = item.replace('"',"'")
    table.write("('VilG', 'Sunday', \""+item[:-1]+"\"),\n")
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
  lunchTable(end)
  dinnerTable(end)

main()
