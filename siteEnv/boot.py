#!/usr/bin/env python
# File: boot.py
# Just pulls bootstrap.css and prints the contents, only needed because cgibin
#

print 'Content-type: text/css'
print
with open('bootstrap.css') as f:
	print f.read()
