#!/usr/bin/python

import MySQLdb
import sys

# Opens database connection
db = MySQLdb.connect("localhost","","","Metrics" )

cursor = db.cursor()

repo = raw_input('Input a Repository: ');


urlQuery = "SELECT url,id FROM projects WHERE name = '%s'" % (repo)

#finds all repos with  the input name
try:
   count = cursor.execute(urlQuery)
   results = cursor.fetchall()
   if count == 0:
      print "Error: Unable to locate repository."
      sys.exit()
   print "Input repository id:"
   print "Repo Url		Repo Id"
   for row in results:
      url = row[0]
      repoId = row[1]
      print "%s,%d" % (url, repoId)
except:
      print "Error: Unable to retrieve data."
      sys.exit()


repoId = raw_input('Input Repository Id: ')

repoQuery = "SELECT * FROM projects WHERE id = '%s'" % (repoId)

#checks if input id exists
try:
   count = cursor.execute(repoQuery)
   # Fetch the rows
   results = cursor.fetchall()
   if count == 0:
      print "Error: unable to locate repository"
      sys.exit()
   for row in results:
      Id = row[0]
      des = row[4]      
      print("Repository id: %d\ndescription: %s" % (Id,des) )
except:
   print "Error: unable to fecth data"
   sys.exit()

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


commentQuery = "SELECT count(*) FROM issues LEFT JOIN issue_comments ON issues.id = issue_comments.issue_id WHERE issue_comments.issue_id IS NULL AND issues.repo_id = '%s';" % (repoId)


try:
   cursor.execute(commentQuery)
   # Fetch the rows
   results = cursor.fetchall()
   for row in results:
      commNum = row[0]
      print("Number of Issues without comments: %d" % (commNum) )
except:
   print "Error: unable to fecth data"

closedQuery = "SELECT DISTINCT count(id) FROM issues INNER JOIN issue_events ON issues.id = issue_events.issue_id WHERE action = 'closed' AND issues.repo_id = '%s';" % (repoId)

try:
   cursor.execute(closedQuery)
   # Fetch the rows
   results = cursor.fetchall()
   for row in results:
      closeNum = row[0]
      print("Number of closed issues: %d" % (closeNum) )
except:
   print "Error: unable to fecth data"


#  disconnect from server
db.close()
