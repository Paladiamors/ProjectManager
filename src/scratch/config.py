'''
Created on Jul 6, 2013

@author: justinyho
'''

import os

configDict = {}

basePath = os.path.split(__file__)[0] #gets the basePath 
configDict["dbPath"] = os.path.join(basePath, "./data.db")
configDict["test_dbPath"] = os.path.join(basePath, "./test_data.db")