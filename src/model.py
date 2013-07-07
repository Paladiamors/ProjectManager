'''
Created on Jul 6, 2013

@author: justinyho
'''

import sqlite3
from config import configDict

conn = sqlite3.connect(configDict["dbPath"], detect_types=sqlite3.PARSE_DECLTYPES)

#creating model for the database here

#Projects can have tasks and information associated to them
#not sure if they should be in the same table just yet, but let's keep them separate for now

#project table: contains details about created projects
#id = id of the project
#projectName = name of the project
#projectDetails = details of the project
#createdDate = date of creation of the project
#completedDate = to be filled when the project has been completed

conn.execute("""create table if not exists projects(
id integer primary key autoincrement,
projectName text,
projectDetails text,
createdDate timestamp,
completedDate timestamp
)""")


#the task table is used to store a variety of tasks associated to a project
conn.execute("""create table if not exists tasks(
id integer primary key autoincrement,
projectId integer,
taskName text,
taskDetails text,
createdDate timestamp,
startDate timestamp,
completedDate timestamp)""")

def getConnection():
    """
    Returns the connection to the database
    """
    return conn
