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

stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)

print "Content-Type: text/html"
print

my_email = cookie['email'].value
my_descript = form['description'].value
c.execute("UPDATE users SET description = ? WHERE email = ?;", (my_descript, my_email))
conn.commit()

print "OK"

conn.close()