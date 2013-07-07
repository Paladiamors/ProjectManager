'''
Created on Jul 7, 2013

@author: justin
'''

import unittest
import config
import projectController
import sys
import os
import datetime

sys.path.append(config.basePath)

class ProjectInterfaceTest(unittest.TestCase):
    
    def setUp(self):
        self.projectInterface = projectController.ProjectInterface(testMode = True)
        
    def test_addProject(self):
        """
        Testing addition of a project
        """
        self.projectInterface.addProject("Project1", "firstProject")
        id, projectName, projectDetails, createdDate, completionDate =  self.projectInterface.conn.execute("select * from projects").fetchone()
        
        self.assert_((1, "Project1", "firstProject", None) == (id, projectName, projectDetails, completionDate))
    
    def test_updateProject(self):
        """
        Testing updating of a project
        """
        self.projectInterface.addProject("Project1", "firstProject")
        self.projectInterface.updateProject(1, "ProjectX", "projectXDetails")
        id, projectName, projectDetails, createdDate, completionDate =  self.projectInterface.conn.execute("select * from projects").fetchone()
        self.assert_((1, "ProjectX", "projectXDetails", None) == (id, projectName, projectDetails, completionDate))
    
    def test_deleteProject(self):
        
        self.projectInterface.addProject("Project1", "firstProject")
        self.projectInterface.deleteProject(1)
        results =  self.projectInterface.conn.execute("select * from projects").fetchall()
        self.assert_(not results)

    def test_deleteProject2(self):
        """
        Testing removal of a task linked to a project     
        """
        self.projectInterface.addProject("Project1", "firstProject")
        self.taskInterface = projectController.TaskInterface(testMode = True)
        self.taskInterface.addTask("TestTask", "someTask", 1)
        self.taskInterface.addTask("TestTask", "another task")
        
        self.projectInterface.deleteProject(1)
        results =  self.projectInterface.conn.execute("select * from projects").fetchall()
        self.assert_(not results)
        
        tasks = self.taskInterface.conn.execute("select * from tasks").fetchall()
        self.assert_(len(tasks) == 1, "error, wrong number of tasks found")
    
    def test_getActiveProjects(self):
        self.projectInterface.addProject("Project1", "firstProject")
        self.projectInterface.addProject("Project2", "secondProject")
        self.projectInterface.updateProject(2, completionDate = datetime.datetime.today())
        
        results = self.projectInterface.getActiveProjects()
        
        self.assert_(len(results) == 1, "number of result should be 1")
        
        result = results[0]
        id = result["id"]
        projectName = result["projectName"]
        projectDetails = result["projectDetails"]
        completionDate = result["completionDate"]
        self.assert_((1, "Project1", "firstProject", None) == (id, projectName, projectDetails, completionDate))
    
    def test_getCompletedProjects(self):
        
        completionDate_orig = datetime.datetime.today()
        self.projectInterface.addProject("Project1", "firstProject")
        self.projectInterface.addProject("Project2", "secondProject")
        self.projectInterface.updateProject(2, completionDate = completionDate_orig)
        
        results = self.projectInterface.getCompletedProjects()
        
        self.assert_(len(results) == 1, "number of result should be 1")

        result = results[0]
        id = result["id"]
        projectName = result["projectName"]
        projectDetails = result["projectDetails"]
        completionDate = result["completionDate"]
        self.assert_((2, "Project2", "secondProject", completionDate_orig) == (id, projectName, projectDetails, completionDate))
    
    def tearDown(self):
        
        if os.path.exists(config.configDict["test_dbPath"]):
            print "deleting testDatabase"
            os.remove(config.configDict["test_dbPath"])
            
