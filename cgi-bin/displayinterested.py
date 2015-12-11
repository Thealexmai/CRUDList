#!/usr/bin/env python
import cgitb
cgitb.enable()
import sqlite3
conn = sqlite3.connect('accounts.db')
c = conn.cursor()
import cgi
form = cgi.FieldStorage()
import Cookie
import os
import json
# from django.utils import simplejson

stored_cookie_string = os.environ.get('HTTP_COOKIE')
cookie = Cookie.SimpleCookie(stored_cookie_string)
#data = {}
x = [] #list

global my_services
my_email = cookie['email'].value
my_buyer = c.execute("SELECT buyer FROM users WHERE email = ?;", [my_email]).fetchone() #gets the status of the buyer
row = c.execute("SELECT service FROM users WHERE email = ?;", [my_email]).fetchone() #gets the interested service of the buyer
if row:
	my_services = row[0]
else:
	pass

<<<<<<< HEAD
=======
# print my_services

>>>>>>> origin/master
print "Content-Type: text/html"
print 
if (my_buyer[0] == 1): #The person logged in is a buyer

<<<<<<< HEAD
	for r in c.execute("SELECT firstname, lastname, email, picture, location FROM users WHERE buyer = 0 AND service = ?;", [my_services]):
=======
	for r in c.execute("SELECT firstname, lastname, email FROM users WHERE buyer = 0 AND service = ?;", [my_services]):
>>>>>>> origin/master
		t = [] # new list
		email = r[0]
		firstname = r[1]
		lastname = r[2]
<<<<<<< HEAD
		picture = r[3]
		location = r[4]
		buyer = "Seller"
		t.append(email)
		t.append(firstname)
		t.append(lastname)
		t.append(buyer)
		t.append(picture)
		t.append(location)
=======
		t.append(email)
		t.append(firstname)
		t.append(lastname)
>>>>>>> origin/master
		x.append(t)

else: #The person logged in is a seller

<<<<<<< HEAD
	for counter in c.execute("SELECT firstname, lastname, email, picture, location FROM users WHERE buyer = 1 AND service = ?;", [my_services]):
=======
	for counter in c.execute("SELECT firstname, lastname, email FROM users WHERE buyer = 1 AND service = ?;", [my_services]):
>>>>>>> origin/master
		t = [] # new list
		email = counter[0]
		firstname = counter[1]
		lastname = counter[2]
<<<<<<< HEAD
		picture = counter[3]
		location = counter[4]
		buyer = "Buyer"
		t.append(email)
		t.append(firstname)
		t.append(lastname)
		t.append(buyer)
		t.append(picture)
		t.append(location)
=======
		t.append(email)
		t.append(firstname)
		t.append(lastname)
>>>>>>> origin/master
		x.append(t)
		
print json.dumps(x)

<<<<<<< HEAD
=======

# def my_ajax_view(request):
# 	if not request.is_ajax():
# 		raise Http404

# 	data =

>>>>>>> origin/master
conn.commit()
conn.close()
