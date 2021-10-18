#!/usr/bin/python

import sqlite3

#conn = sqlite3.connect('test.db')
#conn = sqlite3.connect('pysqlite.ghanshyamdhiman.repl.co/db/test.db')
#conn = sqlite3.connect('https://pysqlite.ghanshyamdhiman.repl.co/db/test.db')
#conn = sqlite3.connect('pysqlite.ghanshyamdhiman.repl.co/test.db')
conn = sqlite3.connect('192.168.0.26/root/pysqlite/test.db')

print("Opened database successfully")

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()
