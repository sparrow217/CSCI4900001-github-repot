#!/usr/bin/python

import MySQLdb

# Opens database connection
db = MySQLdb.connect("localhost","","","Metrics" )

cursor = db.cursor()

repo = raw_input('Input a Repository: ');

repoQuery = "SELECT id FROM projects where name = '%s' ORDER BY id LIMIT 1" % (repo)

try:
   cursor.execute(repoQuery)
   # Fetch the rows
   results = cursor.fetchall()
   for row in results:
      repoId = row[0]
      
      print("Repo id is: %d" % (repoId) )
except:
   print "Error: unable to fecth data"

countQuery = "SELECT count(*) FROM issues WHERE repo_id = '%s'" % (repoId)

try:
   cursor.execute(countQuery)
   # Fetch the rows
   results = cursor.fetchall()
   for row in results:
      issueNum = row[0]
      
      print("Number of Issues: %d" % (issueNum) )
except:
   print "Error: unable to fecth data"


#  disconnect from server
db.close()
