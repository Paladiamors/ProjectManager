'''
Created on Jul 6, 2013

@author: justinyho
'''

import os

configDict = {}

basePath = os.path.split(__file__)[0] #gets the basePath 
configDict["dbPath"] = "sqlite:///data.db"
configDict["test"] = "sqlite:///:memory:"