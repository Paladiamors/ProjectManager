'''
Created on Jul 11, 2013

@author: justinyho
'''

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime

Base = declarative_base()

class Project(Base):
    
    __tablename__ = 'Projects'
    
    id = Column(Integer, primary_key=True)
    projectName = Column(String)
    projectDetails = Column(String)
    creationDate = Column(DateTime)
    completeDate = Column(DateTime)
    
    def __init__(self, projectName, projectDetails):
        
        self.projectName = projectName
        self.projectDetails = projectDetails
        self.creationDate = datetime.datetime.today()
        
    def setComplete(self, date = None):
        if not date:
            date = datetime.datetime.today()
            
        self.completionDate = date
        
class Tasks(Base):
    
    __tablename__ = 'Tasks'
    
    id = Column(Integer, primary_key = True)
    taskName = Column(String)
    taskDetails = Column(String)
    #add projectId here later
    creationDate = Column(DateTime)
    completeDate = Column(DateTime)

def getSession(connString):
    """
    connString used to connect to a database
    returns a Session factory to create sessions
    
    connString can be like: 'sqlite:///:memory:'
    """
    engine = create_engine(connString, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    
    return Session