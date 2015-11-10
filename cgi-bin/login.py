#!/usr/bin/env python
import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

my_emails = form['loginemail'].value
my_passwords = form['loginpassword'].value

import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

print "Content-Type: text/html"
print

import json
data = {} 

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

# print '''
# 	<!doctype html> 
# 	<html>
# 		<head>
# 			<title>Login Page!</title>
# 		</head>
# 		<body>
# 		'''
# print	"Hi"
# print "</body></html>"
conn.close()
