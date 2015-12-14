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
my_description = form['description'].value
my_services = form['servicebutton'].value

<<<<<<< HEAD:cgi-bin/updatepass.py
<<<<<<< HEAD:cgi-bin/updatepass.py
data = {}

=======
>>>>>>> origin/master:cgi-bin/updatepass.py
c.execute("UPDATE users SET password=? WHERE email= ? ;", (my_password, my_email))
=======
c.execute("UPDATE users SET password=?, description=?, service=? WHERE email =?;", (my_password, my_description, my_services, my_email))
>>>>>>> parent of 7ab3749... Final Product:cgi-bin/update.py
conn.commit()

print "Content-Type: text/html"
print

print "OK"

conn.close()