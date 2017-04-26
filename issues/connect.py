#!/usr/bin/python

import MySQLdb

host = "opendata.missouri.edu"
user = "msr"
paswd = "ghtorrent"
database = "msr"

# Opens database connection
def connection():
    return MySQLdb.connect(host,user,paswd,database)
