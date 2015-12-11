#!/usr/bin/env python
import cgitb, sqlite3, Cookie, os, json

cgitb.enable()

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)

def convertBuyer(theint):
	if theint==1:
		theint = "Buyer"
	else:
		theint = "Seller"
	return theint

print "Content-Type: text/html"
print

data = { }

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
	    firstname = r[1]
	    lastname = r[2]
	    service = r[4]
	    descript = r[5]
	    buyer = r[6]
	    buyer = convertBuyer(buyer)
	    picture = r[7]
	    location = r[8]
	    if (checkEmail == my_emails):
	        # If the email in database matches email in cookie
	        data['hasCookie'] = True
	        data['match'] = True
	        data['firstname'] = firstname
	        data['lastname'] = lastname
	        data['service'] = service
	        data['descript'] = descript
	        data['buyer'] = buyer
	        data['picture'] = picture
	        data['location'] = location
	        data['email'] = my_emails

	# If it has a cookie of key email, but value is not inside database
	c.execute('select * from users where email=?;', [my_emails])
	results = c.fetchall()
	if(len(results) <= 0):
		data['hasCookie'] = True
		data['match'] = False

print json.dumps(data)

conn.close()
