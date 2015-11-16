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

def nameToID(diningHall):
  if diningHall == 'Center for Community Dining':
    return 'C4CD'
  elif diningHall == "CU on the Run Grab-n-Go":
    return 'C4CG'
  elif diningHall == "Farrand Market":
    return 'FarM'
  elif diningHall == 'Go Fresh @ farrand Grab-n-Go':
    return 'FarG'
  elif diningHall == 'Kittredge Market':
    return 'Kitt'
  elif diningHall == 'Libby':
    return 'Libb'
  elif diningHall == 'Sewall':
    return 'SewD'
  elif diningHall == 'Sewall Market':
    return'SewM'
  elif diningHall == 'Village grab-n-go':
    return 'VilG'
  elif diningHall == 'Village market':
    return 'VilM'
  elif diningHall == 'Weathertech':
    return 'WTec'
  elif diningHall == 'Zellers Grab-n-Go':
    return 'ZelG'

def hallsDbPrep(hours):
  dbTables = open('hallTable.sql', 'w')
  dbTables.truncate()
  dbTables.write("USE FamishedBuffs;\n")
  dbTables.write("INSERT INTO 'DiningHalls' ('ID', 'Hall', 'Station') VALUES\n")
  for key in hours:
    ID = nameToID(key)
    if ID == 'C4CD':
      dbTables.write("('"+ID+"', '"+key+"', 'Asian Shi Pin'),\n")
      dbTables.write("('"+ID+"', '"+key+"', 'Black Coats'),\n")
      dbTables.write("('"+ID+"', '"+key+"', 'Desserts'),\n")
      dbTables.write("('"+ID+"', '"+key+"', 'Italian Cibo'),\n")
      dbTables.write("('"+ID+"', '"+key+"', 'Kosher'),\n")
      dbTables.write("('"+ID+"', '"+key+"', 'Latin Comida'),\n")
      dbTables.write("('"+ID+"', '"+key+"', 'Persian Ghaza'),\n")
      dbTables.write("('"+ID+"', '"+key+"', 'Smoke n Grill'),\n")
      dbTables.write("('"+ID+"', '"+key+"', 'Sushi'),\n")
    else:
      dbTables.write("('"+ID+"', '"+key+"'),\n")
  size = dbTables.tell()
  dbTables.truncate(size-2)
  dbTables.write(';')
  dbTables.close()

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
  hallsDbPrep(out)
#  print out
#  print
#  print out['Weathertech']

main()
