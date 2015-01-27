#!/usr/bin/env python

import cgi

form = cgi.FieldStorage()
 
birthdate = form.getvalue('birthdate')
hobby = form.getvalue('hobby')

print "Content-type: text/html"
print 
print "Birthdate: "
print birthdate
print "<br/>"
print "Main Hobby: "
print hobby

print "<br/><br/>"

print "Name:<br/>"
print "<form method=\"post\" action=\"page2.py\">" 
print "<input type = \"text\" name=\"name\">"
print "<br/>"
print "Family:<br/>"
print "<input type = \"text\" name=\"family\">"
print "<br/>"
print "<input type=\"submit\" value=\"Submit\"></form>"

