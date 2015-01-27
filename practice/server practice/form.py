#!/usr/bin/env python
 
print "Content-type: text/html"
print
print "<form method=\"post\" action=\"test_form.py\">" 
print "<textarea name=\"comments\" cols=\"40\" rows=\"5\" placeholder = \"Enter comments here...\">"
print "</textarea><br/>"
print "<input type=\"submit\" value=\"Submit\"></form>"
