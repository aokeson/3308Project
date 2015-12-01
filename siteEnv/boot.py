#!/usr/bin/env python

print 'Content-type: text/css'
print
with open('bootstrap.css') as f:
	print f.read()
