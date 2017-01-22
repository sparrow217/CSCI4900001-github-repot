# CSCI4900001-github-repot
Spring2017

#This is our readme for our project.

The Django web framework is used in the project to leverage quick development and the third party packages available.

Python requirements are kept in the requirements.txt file, and is generated using `pip freeze > requirements.txt`.

Python 3.5 is recommended for this setup.  It can be downloaded and installed at [python.org](python.org).

###Development Environment
A Unix dev environment is recommend because the setup instructions provided are known to work in these environments using a bash terminal.  The instructions may work in a Windows bash terminal but have not been tested.  Sqlite3 is used as a lightwieght DBMS for development, and will need to be installed.

###Production Environment
A Linux production environment is recommmended, and Ubuntu version 12 and greater is prefered.  A database will be needed and configuration for the database will need to be provided.  Postegres is the preferred DBMS.

###Development setup

Developers develop on many projects, and each project has it's own dependancies or deps.  
For this reason, a virtual environment is created on the developer's machine in order to isolate Python dependancies between projects.  
Virtualenv and virtualenvwrapper are used to create and maintain the environment and need to be installed in the base Python using the pip command line tool.  
An expalnation of how to install pip is [here](https://pip.pypa.io/en/stable/installing/), but if you can run `which pip` and see a result, you have pip installed.  
To install virtualenv and virtualenvwrapper use:
  `pip install virtualenv virtualenvwrapper`
and wait for a success message.
Some environment variables need to be set and is expelained [here](http://virtualenvwrapper.readthedocs.io/en/latest/install.html), but a bare bones setting is:
- Open up your .bash_profile or .bashrc
- Add the following lines:
   `export WORKON_HOME=$HOME/.envs
   source <(echo which virtualenvwrapper.sh)
   ` 
- Run `source ~/.bash_profile` or `source ~/.bashrc` depending on what file you edited and verify no errors.
Once this is configured, you are able to run commands such as `mkvirtualenv`, and `workon` with no errors (maybe a usage message).
To create a virtualenv for our project:
- Run `which python3` and copy the output
- Run `mkvirtualenv <virtualenv name> -p <paste output of previous command>`.  The name of the virtualenv is of your choosing.
If this is successful, you will see the command prompt change to begin with `(<virtualenv name>)`.  You are now working inside your virtualenv and running `which python` should result to a path in your `~/.envs` folder.
To stop using the virtualenv, run `deactivate`.
To start using the virtualenv, run `workon <virtualenv name>`.
From inside the virtualenv and in the project root folder, run `pip install requirements.txt` to install the deps from the file.
Once successful, run `cd project` to change dir and `python manage.py migrate` to create the database and all the default tables.
Run `python manage.py runserver` to start the built in dev server, and navigate a browser to [http://localhost:8000](http://localhost:8000) to view the index page.   


####Some common commands to help determine what python is being used
- `which python` or `which python3`
  - Shows path python version.
- `python --version` 
  - Show current version of Python used by the command line command.
