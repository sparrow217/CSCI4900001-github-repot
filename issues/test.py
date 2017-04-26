#!/usr/bin/python

import MySQLdb


def testconnection():
    from connect import connection
    
    db = connection()

    db.close();

