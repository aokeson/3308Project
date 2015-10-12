#!/home/seth/anaconda/bin/python
'''
This is version two. It automatically parses a template in html and 
inserts information into it. This will bridge the gap between Peters
html work and my python work.

'''

with open('../template.txt','r') as f:
	template = f.read()

parts = template.split('\n<!-- ##')

static = parts[0]

print static

locData = {
'C4C-Persian':
	{'days':['day1','day2'],
	'menus':
		{'day1':['food1','food2'],
		'day2':['food3','food4']}
	}
'Farrand':
    {'days':['day1','day2'],
    'menus':
        {'day1':['food1','food2'],
        'day2':['food3','food4']}
    }
'Sewall':
    {'days':['day1','day2'],
    'menus':
        {'day1':['food1','food2'],
        'day2':['food3','food4']}
    }
'C4C-Grab and Go':
    {'days':['day1','day2'],
    'menus':
        {'day1':['food1','food2'],
        'day2':['food3','food4']}
    }
}


'''
cards = ''
for spot in locData:
	dic = locData[spot]
	cards += '\t\t<div class="location">\n'
	cards += '\t\t\t<h1 class="locationtitle">'+spot+'</h1>\n'
	for day in dic['days']:
		cards += '\t\t\t\t<div class="day">\n'
		cards += '\t\t\t\t\t<h3 class="daytitle">'+day+'</h3>\n'
		cards += '\t\t\t\t\t<ul class="menu">\n'
		for item in dic['menu'][day]:
			cards += '\t\t\t\t\t\t<li>'+item+'</li>\n'
		cards += '\t\t\t\t\t</ul>\n'
		cards += '\t\t\t\t</div>\n'
	cards += '\t\t</div>\n'
cards += '\t</body>\n'





print 'Content-type: text/html'
print
print top+card
'''
