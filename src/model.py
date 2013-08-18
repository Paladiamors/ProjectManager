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

class Idea(Base):
    
    __tablename__ = 'Ideas'
    
    id = Column(Integer, primary_key=True)
    ideaTitle = Column(String)
    ideaDetails = Column(String)
    creationDate = Column(DateTime)
    startDate = Column(DateTime)
    completeDate = Column(DateTime)

    mapping = {"Title" : ideaTitle,
               "Details" : ideaDetails,
               "Creation Date": creationDate,
               "Completion Date": completeDate}
    
    def __init__(self, **kwargs):
        """
        Overloaded version to add a default creation date
        """
        
        Base.__init__(self, **kwargs)
        
        if "creationDate" not in kwargs:
            self.creationDate = datetime.datetime.today()
        
    def setComplete(self, date = None):
        if not date:
            date = datetime.datetime.today()
            
        self.completionDate = date

    def getCols(self, colList):
        """
        colList = a list of columns to be selected out of the class
        """
        
        return [self.mapping[colName] for colName in colList]
    
class Project(Base):
    
    __tablename__ = 'Projects'
    
    id = Column(Integer, primary_key=True)
    projectTitle = Column(String)
    projectDetails = Column(String)
    creationDate = Column(DateTime)
    startDate = Column(DateTime)
    completeDate = Column(DateTime)
    
    tasks = relationship("Task", backref = "Projects")

    mapping = {"Title" : projectTitle,
               "Details" : projectDetails,
               "Creation Date": creationDate,
               "Start Date": startDate,
               "Completion Date": completeDate}
    
    def __init__(self, **kwargs):
        """
        Overloaded version to add a default creation date
        """
        
        Base.__init__(self, **kwargs)
        
        if "creationDate" not in kwargs:
            self.creationDate = datetime.datetime.today()
        
    def setComplete(self, date = None):
        if not date:
            date = datetime.datetime.today()
            
        self.completionDate = date
        
class Task(Base):
    
    __tablename__ = 'Tasks'
    
    id = Column(Integer, primary_key = True)
    taskTitle = Column(String)
    taskDetails = Column(String)
    creationDate = Column(DateTime)
    scheduleDate = Column(DateTime)
    startDate = Column(DateTime)
    completeDate = Column(DateTime)
    
    projectId = Column(Integer, ForeignKey("Projects.id"))

    mapping = {"Title" : taskTitle,
               "Details" : taskDetails,
               "Creation Date": creationDate,
               "Start Date": startDate,
               "Completion Date": completeDate}
    
    def __init__(self, **kwargs):
        """
        Overloaded version to add a default creation date
        """
        
        Base.__init__(self, **kwargs)
        
        if "creationDate" not in kwargs:
            self.creationDate = datetime.datetime.today()

    def setComplete(self, date = None):
        if not date:
            date = datetime.datetime.today()    
            
            
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


if __name__ == "__main__":
    
    from config import configDict
    Session = getSession(configDict["test"])
    session = Session()
    
    p1 = Project(projectTitle = "project1", projectDetails = "some details")
    p2 = Project(projectTitle = "project2", projectDetails = "some details")
    
    t1 = Task(taskTitle = "Task1", taskDetails = "task detail")
    t2 = Task(taskTitle = "Task2", taskDetails = "task detail")
    t3 = Task(taskTitle = "Task3", taskDetails = "task detail")
    
    p1.tasks = [t1,t2]
    p2.tasks.append(t3)
    
    session.add(p1)
    session.add(p2)
    session.commit()
    results = session.query(Task).filter(Task.projectId == 1).all()
    print results
    
    print
    results = session.query(Task).join(Project).all()
    print results

    