#!/usr/bin/env python

print 'Content-type: text/css'
print
with open('style.css') as f:
	print f.read()


