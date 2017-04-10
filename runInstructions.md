- Download the database mysql dump  (2013-10-12) from http://ghtorrent.org/downloads.html 
- Extract the database dump .gz file using 7zip
- Then  move the resulting mysql-2013-10-12.sql file to vmware ubuntu intstance (drag and drop onto vmware desktop)
- Download Ubuntu iso file 16.04.2 
- Download VMWare WorkStation 12  https://my.vmware.com/en/web/vmware/info/slug/desktop_end_user_computing/vmware_workstation_pro/12_0  
- Open VMWare and click player--->file-->new virtual machine 
- The wizard will install Ubuntu
- Once ubuntu is installed on  VMWare, open the Ubuntu Terminal
- run the following to install necessary python modules: sudo apt-get install python2.7-mysqldb
- to install MySQL, run the following in the terminal: 
- sudo apt-get update
- sudo apt-get install mysql-server-5.5
- sudo apt-get update
- After running the MySQL installation commands run the following command: 
- mysql -u root -p
- When prompted create a username and password 
- Once logged into MySQL, create a new database and table
- Exit MySQL and enter the following command where username is the username you created, file.sql is the extracted mysql dump file, and  database_name is the name of the database that you created: 
- mysql -u username -p database_name < file.sql 
- After running the previous command, the database will be copied to local ubuntu instance in VMWare. 
- Then run the follwoing: pip install numpy 
- Then run the follwoing : pip install tensorflow 
- copy or save the file issues.py from the repository CSCI4900001-github-repot on GitHub( https://github.com/sparrow217/CSCI4900001-github-repot). The location of the issues.py file on GitHub is CSCI4900001-github-repot/issues/
- Take the previously copied/saved issues.py file and copy it to the VMWare Ubuntu VMware instance desktop. 
- Then run the following commands on the Ubuntu terminal 
- chmod 777 issues.py
- python ./issues.py




