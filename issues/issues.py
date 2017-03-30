#!/usr/bin/python

import MySQLdb

# Opens database connection
db = MySQLdb.connect("localhost","root","password","Metrics" )

cursor = db.cursor()


sqlQuery = "SELECT Count(*) FROM issues"

try:
   cursor.execute(sql)
   # Fetch the rows
   results = cursor.fetchall()
   for row in results:
      issueNum = row[0]
      
      print("Number of Issues: %d" % (issueNum) )
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()
