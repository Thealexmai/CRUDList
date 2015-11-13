#!/usr/bin/env python

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# Lecture 5 - CSC210 Fall 2015
# Philip Guo

# To run, start AMPSS and visit:
#
# http://localhost/cgi-bin/lecture5.py
#
# valid usernames to enter: Philip, John, Jane

# Before running this script, make sure you've first run
# lecture4-create-database.py to create the people.db database


# useful for debugging
import cgitb
cgitb.enable()


def printNotLoggedInPage():
    print '<html><body>'
    print '<p>You are not yet logged in.</p>'
    print '<form method="post" action="lecture5.py">'
    print 'Enter your name:'
    print '<input name="my_name" type=text size="30"/>'
    print '<input type="submit"/>'
    print '</form>'
    print '</body></html>'


def printLoggedInPage(username):
    import sqlite3
    conn = sqlite3.connect('people.db')
    c = conn.cursor()

    print '<html><body>'

    for r in c.execute('select * from users where name=?;', [username]):
      name = r[0]
      age = r[1]
      image = r[2]

      print '<h2>' + name + '</h2>'
      print '<h2>' + str(age) + '</h2>'
      print '<img style="width: 300px;" src="' + image + '"/>'

    conn.close()

    print '</body></html>'

import Cookie
import os

import cgi
form = cgi.FieldStorage()
if 'my_name' in form:
    name = form['my_name'].value

    # create a new cookie ...
    c = Cookie.SimpleCookie()
    c['username'] = name

    print "Content-type: text/html"
    print c # send cookie to browser
    print # don't forget the extra newline!
    printLoggedInPage(name)
else:
    stored_cookie_string = os.environ.get('HTTP_COOKIE')
    if not stored_cookie_string:
        print "Content-type: text/html"
        print # don't forget the extra newline!
        printNotLoggedInPage()
    else:
        # if the browser has sent you a cookie, then use it:
        c = Cookie.SimpleCookie(stored_cookie_string)
        # the 'username' key was in the cookie
        if 'username' in c:
            name = c['username'].value

            print "Content-type: text/html"
            print # don't forget the extra newline!
            printLoggedInPage(name)
        # the browser sent you a cookie, but 'username'
        # wasn't in it for some reason ...
        else:
            print "Content-type: text/html"
            print # don't forget the extra newline!
            printNotLoggedInPage()
