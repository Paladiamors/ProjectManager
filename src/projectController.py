'''
Created on Jul 7, 2013

@author: justinyho

interface to the database for the creation of tasks and etc
'''

from model import getConnection
from datetime import datetime

today = datetime.today

class ProjectInterface:
    """
    Interface to the ProjectTable
    """
    def __init__(self, testMode = False):
        
        self.conn = getConnection(testMode)
    
    def addProject(self, projectName, projectDetails):
        """
        adds a project into the project table
        """
        self.conn.execute("""insert into Projects (projectName, projectDetails, creationDate)
        values (?,?,?)""", (projectName, projectDetails, today()))
        self.conn.commit()
        
    def updateProject(self, projectId, projectName = None, projectDetails = None, creationDate = None, completionDate = None):
        """
        can be used to update the projectName, projectDetail or creationDate of a project
        selection of what project to update is done through the projectId.
        I make the assumption that the projectIds is made available to the user before hand
        """

        colDict = {"projectName": projectName,
                   "projectDetails": projectDetails,
                   "creationDate": creationDate,
                   "completionDate": completionDate}
        
        colNames = [key for key in colDict.keys() if colDict[key] is not None] #filtering for non None values
        values = [colDict[colName] for colName in colNames]
        values.append(projectId) #appending the projectId to the end of this
        
        cols = {"cols" : ",".join(["%s=?" % colName for colName in colNames])}
        sqlTemplate = """update projects set %(cols)s where id=?"""
        self.conn.execute(sqlTemplate % cols, values)
        self.conn.commit()
        
    def deleteProject(self, projectId):
        """
        deletes a project from the project table by the project id
        
        If a project is deleted, then tasks related to the project should be deleted
        """
        
        self.conn.execute("delete from projects where id=?", (projectId,))
        self.conn.execute("delete from tasks where projectId=?", (projectId,))
        self.conn.commit()
        
    
    def getActiveProjects(self):
        """
        goes to the database and returns a dictList of values for all active projects
        """
        cols = ["id", "projectName", "projectDetails", "creationDate", "completionDate"]
        results = self.conn.execute("select %s from projects where completionDate is null" % ",".join(cols)).fetchall()
        resultDict = [{col:value for col,value in zip(cols,rowData)} for rowData in results]
        return resultDict
    
    def getCompletedProjects(self):
        """
        returns the list of completed projects and returns a dictList of them
        """
        cols = ["id", "projectName", "projectDetails", "creationDate", "completionDate"]
        results = self.conn.execute("select %s from projects where completionDate is not null" % ",".join(cols)).fetchall()
        resultDict = [{col:value for col,value in zip(cols,rowData)} for rowData in results]
        return resultDict
    
class TaskInterface:
    """
    interface to the task table
    """
    def __init__(self, testMode = False):
        self.conn = getConnection(testMode)
    
    def addTask(self, taskName, taskDetails, projectId = None, startDate = None):
        """
        adds a task to the task table
        taskName = name of task
        taskDetails = details of task
        projectId = id of project to associate to (optional)
        startDate = when the task it to be started (optional)
        """
        
        cols = ["taskName", "taskDetails"]
        values = [taskName, taskDetails]
        
        #adding creation date
        cols.append("creationDate")
        values.append(today())
        
        if projectId:
            cols.append("projectId")
            values.append(projectId)
        if startDate:
            cols.append("startDate")
            values.append(startDate)

        self.conn.execute("""insert into tasks (%s) values (%s) """ % (",".join(cols), ",".join(["?"]*len(cols))), values)
        self.conn.commit()
        
    def updateTask(self, taskId, taskName = None, taskDetails = None, projectId = None, startDate = None, completionDate = None):

        colDict = {"taskName": taskName,
                   "taskDetails": taskDetails,
                   "startDate": startDate,
                   "projectId": projectId,
                   "completionDate": completionDate}
        
        colNames = [key for key in colDict.keys() if key is not None] #filtering for non None values
        values = [colDict[colName] for colName in colNames]
        values.append(projectId) #appending the projectId to the end of this
        
        cols = {"cols" : ",".join(["%s=?" % colName for colName in colNames])}
        sqlTemplate = """update tasks %(cols)s where id=?"""
        self.conn.execute(sqlTemplate % cols, values)
        self.conn.commit()
        
    def deleteTask(self, taskId):
        """
        deletes a task by taskId
        """
        
        self.conn.execute("delete from tasks where taskId=?", (taskId))
        self.conn.commit()

    def getActiveTasks(self):
        """
        goes to the database and returns a dictList of values for all active projects
        """
        cols = ["taskName", "taskDetails", "creationDate", "startDate", "completionDate", "projectId"]
        results = self.conn.execute("select %s from tasks where completionDate is null" % ",".join(cols)).fetchall()
        resultDict = [{col:value for col,value in zip(cols,rowData)} for rowData in results]
        return resultDict
    
    def getCompletedTasks(self):
        """
        returns the list of completed tasks and returns a dictList of them
        """
        cols = ["taskName", "taskDetails", "creationDate", "startDate", "completionDate", "projectId"]
        results = self.conn.execute("select %s from tasks where completionDate is not null" % ",".join(cols)).fetchall()
        resultDict = [{col:value for col,value in zip(cols,rowData)} for rowData in results]
        return resultDict                