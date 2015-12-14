#!/usr/bin/env python
import cgitb
from string import maketrans
cgitb.enable()
import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
import cgi
form = cgi.FieldStorage()
import Cookie
import os
import json


stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)
data = {}

#Help from http://www.dotnetperls.com/remove-html-tags-python
def stripTagsfromDescription(html):
	carrots = "<>"
	brackets = "[]"
	trantable = maketrans(carrots, brackets)
	return html.translate(trantable)

my_email = cookie['email'].value
my_descript = form['description'].value
my_descript = stripTagsfromDescription(my_descript)

print "Content-Type: text/html"
print

c.execute("UPDATE users SET description = ? WHERE email = ?;", (my_descript, my_email))
conn.commit()
data['verify'] = "OK"

print json.dumps(data)

conn.close()