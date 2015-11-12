#!/usr/bin/env python
import cgitb, sqlite3, Cookie, os, json

cgitb.enable()

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)

print "Content-Type: text/html"
print

data = {}

# If there is absolutely no cookie stored
if not stored_cookie_string:
    data['hasCookie'] = False
    data['match'] = False
    # print json.dumps(data)

else:
	# Grab the value from the cookie
	my_emails = cookie["email"].value

	for r in c.execute('select * from users where email=?;', [my_emails]):
	    checkEmail = r[0]
	    if (checkEmail == my_emails):
	        # If the email in database matches email in cookie
	        data['hasCookie'] = True
	        data['match'] = True

	# If it has a cookie of key email, but value is not inside database
	c.execute('select * from users where email=?;', [my_emails]);
	results = c.fetchall()
	if(len(results) <= 0):
		data['hasCookie'] = True
		data['match'] = False

print json.dumps(data)

conn.close()
