- Download Ubuntu iso file 16.04.2 
- Download VMWare WorkStation 12  https://my.vmware.com/en/web/vmware/info/slug/desktop_end_user_computing/vmware_workstation_pro/12_0  
- Open VMWare and click player--->file-->new virtual machine 
- The wizard will install Ubuntu
  At Least 70 gigs of memory are needed.
  
- Once ubuntu is installed on  VMWare, open the Ubuntu Terminal
- run the following to install necessary python modules: sudo apt-get install python2.7-mysqldb
- to install MySQL, run the following in the terminal: 
- sudo apt-get install mysql-server
- sudo apt-get update
- sudo apt-get upgrade

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

- copy or save the file issues.py from the repository CSCI4900001-github-repot on GitHub( https://github.com/sparrow217/CSCI4900001-github-repot). The location of the issues.py file on GitHub is CSCI4900001-github-repot/issues/
- Take the previously copied/saved issues.py file and copy it to the VMWare Ubuntu VMware instance desktop.
- Change issues.py to use the usename and password you used for the database
- Then run the following commands on the Ubuntu terminal 
- python ./issues.py




