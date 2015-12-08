#!/usr/bin/env python
# File: style.py
# Just pulls style.css and prints the contents, only needed because cgibin
#

print 'Content-type: text/css'
print
with open('style.css') as f:
	print f.read()


