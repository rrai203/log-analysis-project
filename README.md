# Log Analysis Project

Its a internal reporting tool which uses information from database understand user activity.The database contain news article and server log of the website,by using this information we can analyse user activity.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Software You need to install

```
GIT BASH
VIRTUAL BOX
VAGRANT
```

### Installing

A step by step series of examples that tell you how to get a development env running

STEPS TO INSTALL GIT BASH
 
1.Download the setup from following link
```
git clone https://github.com/git/git 
```
2.Run the setup file perform installation

STEP TO INSTALL VIRTUAL BOX & VAGRANT

1.Download setup from following link according to your platform
```
https://www.virtualbox.org/wiki/Downloads
```
2.Run the setup and install,Don't run the program after installation.

3.Download Vagrant setup and perform installation 
```
https://www.vagrantup.com/downloads.html 
```
NOTE:For windows user if an error occurs
```The Windows Installer Service Could Not Be Accessed---
   then perform sfc /scannow from command prompt
```
4.Navigate to vagrant directory type
```vagrant up```
This installs the linux system onto your virtual system

5. After the system is installed we have to login
```vagrant ssh```
this logs you into your virtual system.

6.change directory to your vagrant folder by 
```cd /vagrant```

Now you are fully setup and Ready to go.


## Running the program

1.Once logged in using vagrant,run 
```python Summary.py```

2.It takes some time and displays the output 
```LOG ANALYSIS

Popular Article Of All Time

Candidate is jerk, alleges rival  --------  338647  views
Bears love berries, alleges bear  --------  253801  views
Bad things gone, say good people  --------  170098  views

Popular Authors Of All Time

Ursula La Multa  --------  507594  views
Rudolf von Treppenwitz  --------  423457  views
Anonymous Contributor  --------  170098  views

Request leading to more than 1% error

2016-07-17  --------  2.300%
```

### Testing queries

1.queries operation can be performed in PostgreSQL

```
psql -d news
```
2.enter the SQL query to perform search and press enter.
3.to exit press ctrl+d 