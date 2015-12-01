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

def mealTable(menu):
  table = open('mealTable.sql', 'w')
  table.truncate()
  table.write('USE FamishedBuffs;\n')
  table.write("INSERT INTO `Meal` (`HallID`, `Day`, `Item`, `MealType`) VALUES\n")
  halls = ['Farrand and Libby', 'Darley and Sewall']
  days = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
  rows = ['breakfastRow', 'lunchRow', 'dinnerRow']
  for hall in halls:
    for day in days:
      for row in rows:
        for item in menu[hall][day][row]:
          item = item.replace('"',"'")
          if hall == 'Farrand and Libby':
            if day == 'mon':
              if row == 'breakfastRow':
                table.write("(18, 'Monday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(18, 'Monday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(18, 'Monday', \""+item[:-1]+"\", 'Dinner'),\n")
            elif day == 'tues':
              if row == 'breakfastRow':
                table.write("(18, 'Tuesday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(18, 'Tuesday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(18, 'Tuesday', \""+item[:-1]+"\", 'Dinner'),\n")
            elif day == 'wed':
              if row == 'breakfastRow':
                table.write("(18, 'Wednesday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(18, 'Wednesday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(18, 'Wednesday', \""+item[:-1]+"\", 'Dinner'),\n")
            elif day == 'thurs':
              if row == 'breakfastRow':
                table.write("(18, 'Thursday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(18, 'Thursday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(18, 'Thursday', \""+item[:-1]+"\", 'Dinner'),\n")
            else:
              if row == 'breakfastRow':
                table.write("(18, 'Friday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(18, 'Friday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(18, 'Friday', \""+item[:-1]+"\", 'Dinner'),\n")
          else:
            if day == 'mon':
              if row == 'breakfastRow':
                table.write("(07, 'Monday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(07, 'Monday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(07, 'Monday', \""+item[:-1]+"\", 'Dinner'),\n")
            elif day == 'tues':
              if row == 'breakfastRow':
                table.write("(07, 'Tuesday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(07, 'Tuesday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(07, 'Tuesday', \""+item[:-1]+"\", 'Dinner'),\n")
            elif day == 'wed':
              if row == 'breakfastRow':
                table.write("(07, 'Wednesday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(07, 'Wednesday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(07, 'Wednesday', \""+item[:-1]+"\", 'Dinner'),\n")
            elif day == 'thurs':
              if row == 'breakfastRow':
                table.write("(07, 'Thursday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(07, 'Thursday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(07, 'Thursday', \""+item[:-1]+"\", 'Dinner'),\n")
            elif day == 'fri':
              if row == 'breakfastRow':
                table.write("(07, 'Friday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(07, 'Friday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(07, 'Friday', \""+item[:-1]+"\", 'Dinner'),\n")
            elif day == 'sat':
              if row == 'breakfastRow':
                table.write("(07, 'Saturday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(07, 'Saturday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(07, 'Saturday', \""+item[:-1]+"\", 'Dinner'),\n")
            else:
              if row == 'breakfastRow':
                table.write("(07, 'Sunday', \""+item[:-1]+"\", 'Breakfast'),\n")
              elif row == 'lunchRow':
                table.write("(07, 'Sunday', \""+item[:-1]+"\", 'Lunch'),\n")
              else:
                table.write("(07, 'Sunday', \""+item[:-1]+"\", 'Dinner'),\n")
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
