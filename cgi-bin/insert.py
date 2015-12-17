#!/usr/bin/env python
import cgitb, sqlite3, cgi
from string import maketrans
cgitb.enable()

# insert new user data into the database
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

form = cgi.FieldStorage()

my_firstname = form['firstname'].value
my_lastname = form['lastname'].value
my_email = form['email'].value
my_password = form['password'].value
my_description = form['description'].value
my_services = form['servicebutton'].value
my_buyer = form['buysell'].value
my_picture = form['picture'].value
my_location = form['location'].value

# Help from https://docs.python.org/2/library/stdtypes.html
def stripTags(html):
	result = html.translate(None, '/<>!@#$%^&*()+=|{}[]`~""\\:;,.')
	result = result.capitalize()
	return result

def stripTagsfromDescription(html):
	carrots = "<>"
	brackets = "[]"
	trantable = maketrans(carrots, brackets)
	return html.translate(trantable)

my_firstname = stripTags(my_firstname)
my_lastname = stripTags(my_lastname)
my_description = stripTagsfromDescription(my_description)

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
			<meta name="viewport" content="width=device-width, initial-scale=1">
			<title>Cannot</title>
			<!-- Defensive coding in case bootstrap server is down -->
			<script
				src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
			<script src="../js/jquery-1.11.3.min.js"></script>
			<link rel="stylesheet" href="../css/bootstrap.css">
			<link rel="stylesheet" href="../css/bootstrap.min.css">
			<link rel="stylesheet" href="../css/bootstrap-theme.css">
			<link rel="stylesheet" href="../css/bootstrap-theme.min.css">
			
			
			<script src="../js/bootstrap.js"></script>
			<script src="../js/bootstrap.min.js"></script>
			<!-- Get from online -->

			<script
				src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
			<link rel="stylesheet"
				href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
		</head>

		<body>
		<div class="container">
		<h1>Your email already exists. Please go back and try again.<h1><br>
		<a class="btn btn-danger btn-lg" href="../">Home Page</a>
		</div>
		</body>
		</html>'''
else:

	c.execute('insert into users values (?, ?, ?, ?, ?, ?, ?, ?, ?)', (my_email, my_firstname, my_lastname, my_password, my_services, my_description, my_buyer, my_picture, my_location))
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