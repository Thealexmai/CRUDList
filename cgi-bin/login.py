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

def convertBuyer(theint):
	if theint==1:
		theint = "Buyer"
	else:
		theint = "Seller"
	return theint

print "Content-Type: text/html"
print

for r in c.execute('select * from users where email=?;', [my_emails]):
	email = r[0]
	firstname=r[1]
	lastname=r[2]
	password=r[3]
	services=r[4]
	descript=r[5]
	buyer=r[6]
	picture = r[7]
	location = r[8]

	if (password == my_passwords):
		data['email'] = email
		data['firstname'] = firstname
		data['lastname']=lastname
		data['password']=password
		data['services']=services
		data['descript']=descript
		data['buyer']=convertBuyer(buyer)
		data['picture'] = picture
		data['location'] = location
		print json.dumps(data)

conn.close()
