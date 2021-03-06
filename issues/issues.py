#!/usr/bin/python

import MySQLdb
import sys
from connect import connection

db = connection()

cursor = db.cursor()

repo = raw_input('Input a Repository: ');

#finds all repos with  the input name
urlQuery = "SELECT url,id FROM projects WHERE name = '%s'" % (repo)

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
      print "Error: Unable to fetch data."
      sys.exit()


repoId = raw_input('Input Repository Id: ')

#verify repo id
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
   print "Error: unable to fetch data"
   sys.exit()

#counts number of issues from the repo with repo_id
countQuery = "SELECT count(*) FROM issues WHERE repo_id = '%s'" % (repoId)
issueNum = 0

try:
   cursor.execute(countQuery)
   # Fetch the rows
   results = cursor.fetchall()
   for row in results:
      issueNum = row[0]
      
      print("Number of issues: %d" % (issueNum) )
except:
    print "Error: unable to fetch data"

#counts the number of issues without comments
commentQuery = "SELECT count(*) FROM issues LEFT JOIN issue_comments ON issues.id = issue_comments.issue_id WHERE issue_comments.issue_id IS NULL AND issues.repo_id = '%s';" % (repoId)


try:
   cursor.execute(commentQuery)
   # Fetch the rows
   results = cursor.fetchall()
   for row in results:
      commNum = row[0]
      print("Number of issues without comments: %d" % (commNum) )
except:
   print "Error: unable to fetch data"

#counts then number of issues that are closed
closedQuery = "SELECT DISTINCT count(id) FROM issues INNER JOIN issue_events ON issues.id = issue_events.issue_id WHERE action = 'closed'AND issues.repo_id = '%s';" % (repoId)

try:
   cursor.execute(closedQuery)
   # Fetch the rows
   results = cursor.fetchall()
   for row in results:
      closeNum = row[0]
      print("Number of open issues: %d" % (issueNum - closeNum) )
except:
   print "Error: unable to fetch data"

#counts the number of bugs
bugQuery = "select count(*) from issues inner join issue_labels on issues.id = issue_labels.issue_id inner join repo_labels on issue_labels.label_id = repo_labels.id  where name = 'bug' AND issues.repo_id = '%s'" % (repoId)
try:
   cursor.execute(bugQuery)
   # Fetch the rows
   results = cursor.fetchall()
   for row in results:
      bugNum = row[0]
      print("Number of bugs: %d" % ( bugNum) )
except:
   print "Error: unable to fetch data"



#  disconnect from server
db.close()
