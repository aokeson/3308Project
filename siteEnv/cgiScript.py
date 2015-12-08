#!/usr/bin/env python
# File: cgiscript.py
# I made this simply so that I could silence the errors when pressing ctrl-c
# 

 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]
 
httpd = server(server_address, handler)
try:
	httpd.serve_forever()
except KeyboardInterrupt:
	print # Puts out a new line
