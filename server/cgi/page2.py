#!/usr/bin/env python
 
import cgi
 
form = cgi.FieldStorage()
 
name = form.getvalue('name')
family = form.getvalue('family')
 
print "Content-type: text/html"
print
print "Name: "
print name
print "<br/>"
print "Family: "
print family

print "<br/><br/>"

print "Birthdate:<br/>"
print "<form method=\"post\" action=\"page1.py\">" 
print "<input type = \"text\" name=\"birthdate\">"
print "<br/>"
print "Main Hobby:<br/>"
print "<input type = \"text\" name=\"hobby\">"
print "<br/>"
print "<input type=\"submit\" value=\"Submit\"></form>"