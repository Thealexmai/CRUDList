#!/usr/bin/env python
import cgitb
cgitb.enable()

# insert new user data into the database
import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

import cgi
form = cgi.FieldStorage()

my_firstname = form['firstname'].value
my_lastname = form['lastname'].value
my_email = form['email'].value
my_password = form['password'].value
my_description = form['description'].value
my_services = form['services'].value

# Help from https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html
c.execute('select * from users where email=?;', [my_email])
# fetches all the rows that has the key email
results=c.fetchall()

if len(results)>0:
	print"Content-Type: text/html"
	print
	print '''
		<!doctype html>
		<html>
		<head>
			<title>Cannot</title>
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
			<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
		</head>

		<body>
		<div class="container">
		<h1>Your email already exists. Please go back and try again.<h1><br>
		<a class="btn btn-danger btn-lg" href="../">Home Page</a>
		</div>
		</body>
		</html>'''
else:

	c.execute('insert into users values (?, ?, ?, ?, ?, ?)', (my_email, my_firstname, my_lastname, my_password, my_services, my_description))
	conn.commit()

	print "Content-Type: text/html"
	print 

	print '''
			<!doctype html>
			<html>
			<head>
				<title>Created</title>
				<meta name="viewport" content="width=device-width, initial-scale=1">
				<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
				<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
				<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
			</head>

			<body>
				<div class="container">
				<h1>CRUDLIST</h1>
				Hello ''' + my_firstname +  " " + my_lastname + " " 
	print 	'''<h2>You have created an account!</h2>
				Click here to return to the main page.<br>
				<a class="btn btn-success" href="../">Home Page</a>
				</div>
				</body> </html>'''

conn.close()