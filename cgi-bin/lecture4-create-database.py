#!/usr/bin/env python

# the above line is for Windows. For Mac OS, use the path to your Python,
# which is usually:
#!/usr/bin/env python


# Lecture 4 - CSC210 Fall 2015
# Philip Guo

# To create a database named people.db, run:
#
# python lecture4-create-database.py


import sqlite3

# create a database file named 'people.db' if it doesn't exist yet.
# if this file already exists, then the program will quit.
conn = sqlite3.connect('people.db')
c = conn.cursor()

# create a new 'users' table with three columns: name, age, image
c.execute('create table users(name varchar(100) primary key, age integer, image varchar(100))')

# insert 3 rows of data into the 'users' table
c.execute("insert into users values('Philip', 30, '../cat.jpg');")
c.execute("insert into users values('John', 25, '../dog.jpg');")
c.execute("insert into users values('Jane', 40, '../bear.jpg');")

# commit ('save') the transaction and close the connection
conn.commit()
conn.close()
