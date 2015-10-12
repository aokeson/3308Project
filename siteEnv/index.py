#!/usr/bin/env python

'''
This is version two. It automatically parses a template in html and 
inserts information into it. This will bridge the gap between Peters
html work and my python work.

'''

def printLevel(ind,frame,starts,ends):
	size = len(starts)
	lStart = starts[size-ind]
	lStart = lStart.split('\n<!-- ')
	lStart[1] = removeLine1(lStart[1])
	try:
		lEnd = ends[size-ind]
	except IndexError:
		lEnd = ''
	if isinstance(frame,dict):
		for value in frame['keys']:
			try:
				l1tmp = lStart[1].replace("<!-- &&ID&& -->",frame[value]['ID'])
				l0tmp = lStart[0].replace("<!-- &&ID&& -->",frame[value]['ID'])
			except:
				l0tmp = lStart[0]
				l1tmp = lStart[1]
			print l0tmp
			print value
			print l1tmp
			printLevel(ind-1,frame[value],starts,ends)
			print lEnd

	else:
		for value in frame:
			print lStart[0]
			print value
			print lStart[1]
			print lEnd

def removeLine1(s):
	try:
		i = s.index('\n')
		return s[i+1:]
	except ValueError:
		return s

def addIds():
	pass

def parseTemplate():
	with open('./template.html','r') as f:
		template = f.read()

	starts = template.split('\n<!-- ##')

	static = starts[0]
	for i in range(len(starts)): # remove comments
		starts[i] = removeLine1(starts[i])
	ends = starts[-1]
	ends = ends.split('\n<!-- @@')
	starts[-1] = ends[0]

	ends = ends[:0:-1] # reverse the list and remove first element
	for i in range(len(ends)): #remove comments
		ends[i] = removeLine1(ends[i])
	return static,starts,ends

def addIds(start,Data):
	start,template,end = start.split('\n<!-- &&IDs&& -->')
	s = []
	for place in Data['keys']:
		 s += [template.replace('&&ID&&',Data[place]['ID'])]
	s = [start]+s+[end]
	return '\n'.join(s)

def printSite(Data):
	static,starts,ends = parseTemplate()

	print 'Content-type: text/html'
	print
	print addIds(static,Data)
	printLevel(len(ends),Data,starts,ends)
	print ends[0]


locData = {'keys':['C4C-Persian','C4C-Grab and Go','Farrand','Sewall'],
'C4C-Persian':
	{'keys':['Monday 11am - 2 pm','Tuesday 11am - 2 pm','Wednesday 11am - 2 pm'],
	'ID': 'C4CPersian',
	'Monday 11am - 2 pm':['Beef Kabob','food2','food3'],
	'Tuesday 11am - 2 pm':['Chicken Kabob','food2','food3'],
	'Wednesday 11am - 2 pm':['Chicken Drummies','food2','food3']
	},
'Farrand':
	{'keys':['Monday 11am - 2 pm','Tuesday 11am - 2 pm','Wednesday 11am - 2 pm'],
	'ID': 'Farrand',
	'Monday 11am - 2 pm':['Burgers','food2','food3'],
	'Tuesday 11am - 2 pm':['Pizza','food2','food3'],
	'Wednesday 11am - 2 pm':['Quesadillas','food2','food3']
	},
'Sewall':
	{'keys':['Monday 11am - 2 pm','Tuesday 11am - 2 pm','Wednesday 11am - 2 pm'],
	'ID': 'Sewall',
	'Monday 11am - 2 pm':['Chicken Nuggets','food2','food3'],
	'Tuesday 11am - 2 pm':['Pizza','food2','food3'],
	'Wednesday 11am - 2 pm':['food1','food2','food3']
	},
'C4C-Grab and Go':
	{'keys':['Monday 11am - 2 pm','Tuesday 11am - 2 pm','Wednesday 11am - 2 pm'],
	'ID': 'C4CGG',
	'Monday 11am - 2 pm':['Pizza','food2','food3'],
	'Tuesday 11am - 2 pm':['Lunch','food2','food3'],
	'Wednesday 11am - 2 pm':['Dinner','food2','food3']
	}
}

testData = {'keys':['Spot'],
			'Spot' : {'keys':['Day1'],
				'ID':'Spot',
				'Day1':['food1']
				}
			}

printSite(locData)
