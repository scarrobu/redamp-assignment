-> See also notes in this README.

# Task 
Your task is to implement a command line application that will process and store
malicious IOCs from all specified data sources on the Internet into a database.

## Prerequisites
Python 3.10.4, SQLAlchemy 2.0.22, requests 2.31.0

## Install 
Need to install SQLAlchemy and requests

## Usage
```
usage:

Start with:
    python main.py init  --  to create db

then:
    python main.py load  --  to download data from web sources

and finally:
    python main.py fill  --  to fill DB with transformed data
```

This download the data, create database file (initial is sqlite named "malicious_IOC.db" in my_app/ directory).
Engine can be changed on file create_db.py on line 30.
I tested posgres with my PGAdmin.

### Notes
Second branch named over-time exist in this repository.
On this branch i have code that i worked on after submiting code in master branch.
Added few error handling, file ans folder exist checks or change code to achieve high pylint score

Third branch named testing existt in this repository.
On this branch i try use pytest for some tests, after submiting code in master branch.
I have no experiences with testing until now, this is my first test casses.
I decides to use pytest and am triyng to learn from documentation.
For now i have implemented test for exist dirs and data files and funciton open_file test.
