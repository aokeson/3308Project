#!/usr/bin/python
import urllib2
from lxml import html
import MySQLdb

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

def mealTable(menu):
  db = MySQLdb.connect(user='root',db='FamishedBuffs');
  query = db.cursor()
  table = open('mealTable.sql', 'w')
  table.truncate()
  table.write('USE FamishedBuffs;\n')
  table.write("INSERT INTO `Meal` (`HallID`, `Item`, `HourID`) VALUES\n")
  dayDict = {
  'mon':'Monday', 
  'tues':'Tuesday', 
  'wed':'Wednesday', 
  'thurs':'Thursday', 
  'fri':'Friday', 
  'sat':'Saturday', 
  'sun':'Sunday'
  }
  mealDict = {
  'breakfastRow':'Breakfast',
  'lunchRow':'Lunch',
  'dinnerRow':'Dinner'
  }
  hallDict = {
  'Farrand and Libby':'18', 
  'Darley and Sewall':'07'
  }
  for hall in hallDict:
    for day in dayDict:
      for meal in mealDict:
        idStr = "SELECT ID from Hours WHERE HALLID="+hallDict[hall]+" and Day='"+dayDict[day]+"' and Meal='"+mealDict[meal]+"'"
        query.execute(idStr)
        try:
          result = query.fetchall()
          hourid = str(result[0][0])
          for item in menu[hall][day][meal]:
            item = item.replace('"',"'")
            cmd = "("+hallDict[hall]+", \""+item[:-1]+"\", "+hourid+"),\n"
            table.write(cmd)
        except:
          pass
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
  mealTable(end)

main()
