#!/usr/bin/env python
import cgitb
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

my_email = cookie['email'].value
my_location = form['location'].value

data = {}

print "Content-Type: text/html"
print

c.execute("UPDATE users SET location = ? WHERE email = ?;", (my_location, my_email))
conn.commit()

data['verify'] = "OK"

print json.dumps(data)

conn.close()