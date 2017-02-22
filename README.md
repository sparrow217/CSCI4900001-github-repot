# CSCI4900001-github-repot
Spring2017

#This is our readme for our project.

Python requirements are kept in the requirements.txt file, and this file is generated using `pip freeze > requirements.txt`.

Python 3.5 is recommended for this project.  It can be downloaded and installed at [python.org](python.org).

###Description
For the Community Health and Sustainability application Jackson and I will create, we decided to focus on obtaining data from GHTorrent about the Github public event timeline. Specifically, we are going to obtain data pertaining to issues stored on GHTorrent. The issues our application will focus on gathering are the total number of issues, the number of open issues, and the number of open issues with no comments from a maintainer. The decision for our application to focus on gathering the previously mentioned issues was made in an effort to provide useful statistics about an aggregate of issues on GitHub that are not being addressed by maintainers.  Our application will also attempt to determine whether an issue is actually an issue, and not a TODO item.  After discussing the function of the application, we have established the development environment and systems.


###Development Environment
A Unix dev environment is recommended because the setup instructions provided are known to work in these environments using a bash terminal.  The instructions may work in a Windows bash terminal but have not been tested.  MySQL database will be used to store data within our development environment 


###Production Environment
A Linux production environment is recommmended, and Ubuntu version 12 and greater is prefered.  A database will be needed and configuration for the database will need to be provided.  MySQL is the preferred DBMS.


###Production setup
The app is not ready for production yet so this part is incomplete.

###Technologies used:
The development environment we will be using is a unix/linux environment. Also we will be using the MySQL relational database management system to store data that is extracted from GHTorrent. The application will be hosted on a server instance provided by Amazon Web Services (AWS). We will be using Python to handle the data on the backend and we will return a CSV file that will contain the data. 


###License 
This project is licensed under the terms of the MIT license.
