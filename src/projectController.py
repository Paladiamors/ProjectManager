'''
Created on Jul 7, 2013

@author: justinyho

interface to the database for the creation of tasks and etc
'''

from model import getConnection
from datetime.datetime import today
conn = getConnection()

class ProjectInterface:
    """
    Interface to the ProjectTable
    """
    def __init__(self):
        pass
    
    def addProject(self, projectName, projectDetails):
        """
        adds a project into the project table
        """
        conn.execute("""insert into Projects (projectName, projectDetails, creationDate)
        values (?,?,?)""", (projectName, projectDetails, today()))
        conn.commit()
        
    def updateProject(self, projectId, projectName = None, projectDetail = None, creationDate = None, completionDate = None):
        """
        can be used to update the projectName, projectDetail or creationDate of a project
        selection of what project to update is done through the projectId.
        I make the assumption that the projectIds is made available to the user before hand
        """

        colDict = {"projectName": projectName,
                   "projectDetail": projectDetail,
                   "creationDate": creationDate,
                   "completionDate": creationDate}
        
        colNames = [key for key in colDict.keys() if key is not None] #filtering for non None values
        values = [colDict[colName] for colName in colNames]
        values.append(projectId) #appending the projectId to the end of this
        
        cols = {"cols" : ",".join(["%s=?" % colName for colName in colNames])}
        sqlTemplate = """update projects %(cols)s where id=?"""
        conn.execute(sqlTemplate % cols, values)
        conn.commit()
        
    def deleteProject(self, projectId):
        """
        deletes a project from the project table by the project id
        
        If a project is deleted, then tasks related to the project should be deleted
        """
        
        conn.execute("delete from projects where id=?", (projectId))
        conn.execute("delete from tasks where projectId=?", (projectId))
        conn.commit()
        
    
    def getActiveProjects(self):
        """
        goes to the database and returns a dictList of values for all active projects
        """
        cols = ["projectName", "projectDetails", "creationDate", "completedDate"]
        results = conn.execute("select %s from projects where completedDate is null" % ",".join(cols)).fetchall()
        resultDict = [{col:value for col,value in zip(cols,rowData)} for rowData in results]
        return resultDict
    
    def getCompletedProjects(self):
        """
        returns the list of completed projects and returns a dictList of them
        """
        cols = ["projectName", "projectDetails", "creationDate", "completedDate"]
        results = conn.execute("select %s from projects where completedDate is not null" % ",".join(cols)).fetchall()
        resultDict = [{col:value for col,value in zip(cols,rowData)} for rowData in results]
        return resultDict
    
class TaskInterface:
    """
    interface to the task table
    """
    def __init__(self):
        pass
    
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
        if projectId:
            cols.append("projectId")
            values.append(projectId)
        if startDate:
            cols.append("startDate")
            values.append(startDate)

        conn.execute("""insert into tasks (%s) values (%s) """ % (",".join(cols), ",".join(["?"]*len(cols))), cols)
        conn.commit()
        
    def updateTask(self, taskId, taskName = None, taskDetails = None, projectId = None, startDate = None, completionDate = None):