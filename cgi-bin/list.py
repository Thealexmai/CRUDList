#!/usr/bin/env python
import cgitb, sqlite3, cgi, json, Cookie, os

cgitb.enable()
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)
my_email = cookie['email'].value
my_buyer = c.execute("SELECT buyer FROM users WHERE email = ?;", [my_email]).fetchone()



form = cgi.FieldStorage()

data = []

listtoview = form['servicetoview'].value

def convertbuyer(theint):
	if theint==1:
		theint = "Buyer"
	else:
		theint = "Seller"
	return theint

print "Content-Type: text/html"
print

if(my_buyer[0] == 1):
	for r in c.execute("SELECT firstname, lastname, email, buyer, picture, location FROM users WHERE buyer = 0 AND service = ?;", [listtoview]):
		t = []
		email = r[0]
		firstname = r[1]
		lastname = r[2]
		buyer = r[3]
		buyer = convertbuyer(buyer)
		picture = r[4]
		location = r[5]
		t.append(email)
		t.append(firstname)
		t.append(lastname)
		t.append(buyer)
		t.append(picture)
		t.append(location)
		data.append(t)
else:
	for r in c.execute("SELECT firstname, lastname, email, buyer, picture, location FROM users WHERE buyer = 1 AND service = ?;", [listtoview]):
		t = []
		email = r[0]
		firstname = r[1]
		lastname = r[2]
		buyer = r[3]
		buyer = convertbuyer(buyer)
		picture = r[4]
		location = r[5]
		t.append(email)
		t.append(firstname)
		t.append(lastname)
		t.append(buyer)
		t.append(picture)
		t.append(location)
		data.append(t)

# print listtoview
print json.dumps(data)
conn.close()