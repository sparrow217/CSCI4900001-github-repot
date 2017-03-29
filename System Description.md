Xavier Yelder/Jackson Urrutia 

Internet Systems Development 

Dr. Matt Germonprez 

February 22, 2017 

System Description and Development Environment 

The purpose of the application Jackson and I are developing is to help gather data to support
GH Health and Sustainability. We have also identified what development environment and
systems will be associated with the application. 

For the Community Health and Sustainability application Jackson and I will create, we
decided to focus on obtaining data from GHTorrent about the Github public event timeline.
Specifically, we are going to obtain data pertaining to issues stored on GHTorrent. The issues
our application will focus on gathering are the total number of issues, the number of open
issues, and the number of open issues with no comments from a maintainer. The decision for
our application to focus on gathering the previously mentioned issues was made to
provide useful statistics about an aggregate of issues on GitHub that are not being addressed
by maintainers.  Our application will also attempt to determine whether an issue is an
issue, and not a TODO item.  After discussing the function of the application, we have
established the development environment and systems.

A task for us was to find the best suited development environment and systems to
incorporate into our application. After doing research on various technologies, we were able to
reach a decision about the environment we will be developing the application in and the
systems which will support its functionality. The development environment we will be using is a
unix/linux environment. Also we will be using the MySQL relational database management
system to store data that is extracted from GHTorrent. The application will be hosted on a
Ubuntu server instance provided by Anvil. We will be using Python to handle the data on the
backend and we will return a CSV file that will contain the data. 
