#!/usr/bin/env python
import cgitb
cgitb.enable()

import sqlite3
conn=sqlite3.connect('accounts.db')
c=conn.cursor()

import Cookie
import os
import json

stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)

data = {}

print "Content-Type: text/html"
print

# If no cookies
if not stored_cookie_string:
	data['hasCookie']=False
	data['match']=False
	# print json.dumps(data)
else:
	# load() parses the cookie string
	cookie.load(stored_cookie_string)
	my_emails = cookie['email']
	for r in c.execute('select * from users where email=?;' [my_emails]):
		checkEmail = r[0]
		if(checkEmail == my_emails):
			# If the email in database matches email in cookie
			data['hasCookie']=True
			data['match']=True
			# print json.dumps(data)
		else:
			# otherwise, it has a cookie, but wrong cookie
			data['hasCookie']=True
			data['match']=False
			# print json.dumps(data)
print json.dumps(data)

conn.close()