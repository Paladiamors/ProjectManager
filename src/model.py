'''
Created on Jul 6, 2013

@author: justinyho
'''

import sqlite3
from config import configDict

def getConnection(testMode = False):
    
    if not testMode:
        dbPath = configDict["dbPath"]
    else:
        dbPath = configDict["test_dbPath"]

    conn = sqlite3.connect(dbPath, detect_types=sqlite3.PARSE_DECLTYPES)
    
    #creating model for the database here
    
    #Projects can have tasks and information associated to them
    #not sure if they should be in the same table just yet, but let's keep them separate for now
    
    #project table: contains details about created projects
    #id = id of the project
    #projectName = name of the project
    #projectDetails = details of the project
    #creationDate = date of creation of the project
    #completionDate = to be filled when the project has been completed
    
    conn.execute("""create table if not exists projects(
    id integer primary key autoincrement,
    projectName text,
    projectDetails text,
    creationDate timestamp,
    completionDate timestamp
    )""")
    
    
    #the task table is used to store a variety of tasks associated to a project
    conn.execute("""create table if not exists tasks(
    id integer primary key autoincrement,
    projectId integer,
    taskName text,
    taskDetails text,
    creationDate timestamp,
    startDate timestamp,
    completionDate timestamp)""")

    return conn