# CSCI4900001-github-repot
Spring2017

#This is our readme for our project.

Requirements are kept in requirements.md.

Python 3.5 is recommended for this project.  It can be downloaded and installed at [python.org](python.org).

###Description
For the Community Health and Sustainability application Jackson and I will create, we decided to focus on obtaining data from GHTorrent about the Github public event timeline. Specifically, we are going to obtain data pertaining to issues stored on GHTorrent. The issues our application will focus on gathering are the total number of issues, the number of open issues, and the number of open issues with no comments from a maintainer. The decision for our application to focus on gathering the previously mentioned issues was made in an effort to provide useful statistics about an aggregate of issues on GitHub that are not being addressed by maintainers.  Our application will also attempt to determine whether an issue is actually an issue, and not a TODO item.  After discussing the function of the application, we have established the development environment and systems.

The Community Health and Sustainability application will pull data from the Github public event timeline.
Specifically, the application pulls data about issues stored on GHTorrent. The issues
the application will focus on gathering are the following: 
- Total number of issues
- The number of open issues
- The number of open issues with no comments from a maintainer. 
- Number of Bugs 


###Development Environment
A Linux dev environment is recommended because the setup instructions provided are known to work in these environments using a bash terminal.  The instructions may work in a Windows bash terminal but have not been tested. 
- MySQL database version 5.7.17 will be used to store data within our development environment
- Python version 2.7.12 to handle the data on the backend


###Production Environment
A Linux production environment is recommmended, and Ubuntu version 12 and greater is prefered.  A database will be needed and configuration for the database will need to be provided.
- MySQL version 5.7.17 is the preferred DBMS.
- Python version 2.7.12 is the used Version.

- Dependencies
  MySQL v. 5.7+
  Python v. 2.7.*
  MyS QLdb for python 2.7
  
###Production setup
The app is not ready for production yet so this part is incomplete.

###Technologies used:
The development environment we will be using is a unix/linux environment. We will use the GHTorrent dump to create a Mysql database. The application run on Ubuntu. We will be using Python to handle the data on the backend.

##Use Case
Title: Get Metric
Primary Actor: A User
Goal in Context: Get issue metrics that include total number of issues, number of open issues, number of issues without comments, and number of issues that are bugs
Stakeholders: User
Precondition: The database has the repository
Main Success Scenario: The user gets the metric data for the repository
Failed End Conditions: Could not retrieve metrics
Trigger: runnning program

##Contributing
This project is not accepting contributions at this time as the project is in early stages of development.

###License 
This project is licensed under the terms of the MIT license.
