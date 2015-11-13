#!/usr/bin/env python

# For debugging
import cgitb
cgitb.enable()

# For getting form data
import cgi
form = cgi.FieldStorage()

my_emails = form['loginemail'].value
my_passwords = form['loginpassword'].value

# Accessing database
import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

import json
data = {} 

print "Content-Type: text/html"
print

for r in c.execute('select * from users where email=?;', [my_emails]):
	email = r[0]
	firstname=r[1]
	lastname=r[2]
	password=r[3]
	services=r[4]
	descript=r[5]

	if (password == my_passwords):
		data['email'] = email
		data['firstname'] = firstname
		data['lastname']=lastname
		data['password']=password
		data['services']=services
		data['descript']=descript
		print json.dumps(data)

conn.close()
