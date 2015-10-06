#!/home/seth/anaconda/bin/python

top = '''
<!DOCTYPE html>
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
        <script>
            function getContent(name) {
                console.log("getContent script called with '" + name + "'");
            }
        </script>
        <script>
            console.log("onload script called, calling getContent...");
            window.onload = getContent("menus.txt");
        </script>

        <meta charset="UTF-8"> 
        <link rel="stylesheet" href="style.css">
        <title>FOOD</title>
    </head>
    <body>
        <h1 class="title">CleverlyNamedBuffs</h1>
        <p class="tagline">The quick brown fox jumps over the lazy dog.</p>
        <div class="selector">
            <ul class="nav">
                <li class="nav">[select location]</li>
                <li class="nav">[select day]</li>
                <li class="nav">[select vegetarian]</li>
            </ul>
        </div>
'''

locations = ['place1','place2','place3','place4']
locData = {
'place1':
	{'days':['day1','day2'],
	'menus':
		{'day1':['food1','food2'],
		'day2':['food3','food4']}
	}
'place2':
    {'days':['day1','day2'],
    'menus':
        {'day1':['food1','food2'],
        'day2':['food3','food4']}
    }
'place3':
    {'days':['day1','day2'],
    'menus':
        {'day1':['food1','food2'],
        'day2':['food3','food4']}
    }
'place4':
    {'days':['day1','day2'],
    'menus':
        {'day1':['food1','food2'],
        'day2':['food3','food4']}
    }
}

cards = ''
for spot in locations:
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
