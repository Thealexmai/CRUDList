#!/usr/bin/env python
import cgitb, sqlite3, Cookie, os
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

# form = cgi.FieldStorage()
cgitb.enable()
stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)

my_email = cookie["email"].value
c.execute("delete from users where email=?;", [my_email])
conn.commit()

print "Content-Type: text/html"
print

print'''
	<html>
	<head>
		<title>Deleted</title>
	</head>

	<body>
		Click here to go back to the homepage <a href="../">Home page</a>
	</body>
	</html>
	'''
conn.close()

