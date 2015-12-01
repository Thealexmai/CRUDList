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

my_email = cookie['email'].value
my_password = form['password'].value

c.execute("UPDATE users SET password=? WHERE email= ? ;", (my_password, my_email))
conn.commit()

print "Content-Type: text/html"
print

print "OK"

conn.close()