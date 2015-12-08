#!/usr/bin/env python
# File: rotate.py
# Just pulls jQueryRotate.js and prints the contents, only needed because cgibin
#



print 'Content-type: text/js'
print
with open('jQueryRotate.js') as f:
	print f.read()
