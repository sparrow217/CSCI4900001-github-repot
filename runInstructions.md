- On a system with lunux
  With 70+ gigs of free space
  
- run the following to install necessary python modules: sudo apt-get install python2.7-mysqldb
- to install MySQL, run the following in the terminal: 
- sudo apt-get install mysql-server
- sudo apt-get update
- sudo apt-get upgrade

The code is setup to use a public version of the database, to use your own database run the following:

- Download the database mysql dump  (2013-10-12) from http://ghtorrent.org/downloads.html 
- Extract the database dump .gz
- After running the MySQL installation and extracting the database commands run the following command: 
- mysql -u root -p
- When prompted create a username and password
- Once logged into MySQL, create a new database and table
- Exit MySQL and enter the following command where username is the username you created, file.sql is the extracted mysql dump file, and  database_name is the name of the database that you created: 
- mysql -u username -p database_name < file.sql
  This may take several hours
- After running the previous command, the database will be copied to local ubuntu instance in VMWare. 

If you did not setup your own database continue here:

- copy or save the file issues.py from the repository CSCI4900001-github-repot on GitHub( https://github.com/sparrow217/CSCI4900001-github-repot). The location of the issues.py file on GitHub is CSCI4900001-github-repot/issues/
- Take the previously copied/saved issues.py file and copy it to the VMWare Ubuntu VMware instance desktop.
- Change issues.py to use the usename and password you used for the database
- Then run the following commands on the Ubuntu terminal 
- python ./issues.py




