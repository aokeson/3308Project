#!/usr/bin/env python

'''
This is version two. It automatically parses a template in html and 
inserts information into it. This will bridge the gap between Peters
html work and my python work.

'''

def printLevel(ind,frame):
	size = len(starts)
	lStart = starts[size-ind]
	lStart = lStart.split('\n<!-- ')
	lStart[1] = removeLine1(lStart[1])
	try:
		lEnd = ends[size-ind]
	except IndexError:
		lEnd = ''
	for value in frame:
		print lStart[0]
		print value
		print lStart[1]
		if isinstance(frame,dict):
			printLevel(ind-1,frame[value])
		print lEnd

def removeLine1(s):
	try:
		i = s.index('\n')
		return s[i+1:]
	except ValueError:
		return s

def addIds

#def parseTemplate():
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

locData = {
'C4C-Persian':
	{'keys':['Monday 11am - 2 pm','Tuesday 11am - 2 pm','Wednesday 11am - 2 pm'],
	'ID': 'Persian',
	'Monday 11am - 2 pm':['food1','food2','food3'],
	'Tuesday 11am - 2 pm':['food1','food2','food3'],
	'Wednesday 11am - 2 pm':['food1','food2','food3']
	},
'Farrand':
	{'keys':['Monday 11am - 2 pm','Tuesday 11am - 2 pm','Wednesday 11am - 2 pm'],
	'ID': 'Persian',
	'Monday 11am - 2 pm':['food1','food2','food3'],
	'Tuesday 11am - 2 pm':['food1','food2','food3'],
	'Wednesday 11am - 2 pm':['food1','food2','food3']
	},
'Sewall':
	{'keys':['Monday 11am - 2 pm','Tuesday 11am - 2 pm','Wednesday 11am - 2 pm'],
	'ID': 'Persian',
	'Monday 11am - 2 pm':['food1','food2','food3'],
	'Tuesday 11am - 2 pm':['food1','food2','food3'],
	'Wednesday 11am - 2 pm':['food1','food2','food3']
	},
'C4C-Grab and Go':
	{'keys':['Monday 11am - 2 pm','Tuesday 11am - 2 pm','Wednesday 11am - 2 pm'],
	'ID': 'Persian',
	'Monday 11am - 2 pm':['food1','food2','food3'],
	'Tuesday 11am - 2 pm':['food1','food2','food3'],
	'Wednesday 11am - 2 pm':['food1','food2','food3']
	}
}

testData = {'Spot' : {'Day1':['food1']}}

print 'Content-type: text/html'
print
print static
printLevel(len(ends),locData)
print ends[0]
