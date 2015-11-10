#!/usr/bin/env python

import sqlite3

# create a database file named 'people.db' if it doesn't exist yet.
# if this file already exists, then the program will quit.
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

# create a new 'users' table with three columns: name, age, image
c.execute('create table users(email varchar(100) primary key, firstname varchar(100), lastname varchar(100), password varchar(100), service varchar(100), description varchar(100))')

# insert 3 rows of data into the 'users' table
c.execute("insert into users values ('amai2@u.rochester.edu', 'Alex', 'Mai', 'hi', 'Haircut', 'Dogs');")

# commit ('save') the transaction and close the connection
conn.commit()
conn.close()