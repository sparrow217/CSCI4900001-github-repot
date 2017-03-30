System Description and Development Environment 

The purpose of the application is to help gather data to support
GH Health and Sustainability. We have also identified what development environment and
systems will be associated with the application. 

The Community Health and Sustainability application will pull data from the Github public event timeline.
Specifically, the application pulls data about issues stored on GHTorrent. The issues
the application will focus on gathering are the following: 
- total number of issues
- the number of open issues
- the number of open issues with no comments from a maintainer. 
- if an issue is an issue, and not a TODO item.  

The development environment that will be used for developing the applicaiton is a unix/linux environment. The application will use MySQL version 	5.7.17 relational database management system to store data that is extracted from GHTorrent. The application will be hosted on a
Ubuntu server instance provided by Anvil. The application will use Python version 2.7.12 to handle the data on the
backend and  will return a JSON that will contain the data. 
