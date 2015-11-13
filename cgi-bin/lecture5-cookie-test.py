#!/usr/bin/env python

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# Lecture 5 - CSC210 Fall 2015
# Philip Guo

# To run, start AMPSS and visit:
#
# http://localhost/cgi-bin/lecture5-cookie-test.py


import cgi

# to facilitate debugging
import cgitb
cgitb.enable()

import datetime
t = str(datetime.datetime.now())

import Cookie
import os

stored_cookie_string = os.environ.get('HTTP_COOKIE')
if not stored_cookie_string:
    # if the browser didn't send a cookie to us (the server), then
    # create a new cookie and send it to the browser
    c = Cookie.SimpleCookie()
    c['current_time'] = t

    print "Content-type: text/html"
    print c
    print # don't forget the extra newline!

    print "<html><body>"
    print "<h2>Hello, the current time is: " + c["current_time"].value + "</h2>"
    print "<h1>I'm sending a cookie to you!</h1>"
    print "</body></html>"
else:
    # if the browser has sent you a cookie, then print out its contents
    # to the HTML webpage
    c = Cookie.SimpleCookie(stored_cookie_string)

    print "Content-type: text/html"
    print # don't forget the extra newline!

    print "<html><body>"
    print "<h1>Hello, I received your cookie.</h1>"
    if 'current_time' in c:
        print "<h2>Its saved current_time is: " + c['current_time'].value + "</h2>"
    else:
        print "<h2>sorry your cookie doesn't have a current_time</h2>"
    print "</body></html>"
