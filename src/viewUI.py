'''
Created on Aug 10, 2013

@author: justinyho
'''

from UI import MyFrame2
from model import getSession, Idea, Project, Task
from UI.treeListCtrl import TreeListCtrl
from UI.listCtrl import ListCtrl
import wx

class MainFrame(MyFrame2):
    
    def __init__(self, *args, **kwargs):
        
        self.session = getSession()
        self.ideaListCols = ["Title", "Create Date", "Start Date"]

    def initControls(self):
        
        #populating the idea list here
        self.ideaList.Destroy()
        self.ideaList = ListCtrl( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON|wx.LC_REPORT )
        self.bSizer20.Add( self.ideaList, 1, wx.EXPAND, 0 )
        
        for index,header in zip(range(len(self.ideaListCols), self.ideaListCols)):
            self.ideaList.InsertColumn(index, header)
        
        ideas = self.session.query(Idea).all()
    def populateData(self):
        """
        populates data for the class
        """
        
        def _getIdeas():
            ideas = self.session.query(Idea).all()
            
            
            projects = self.session.query(Project).all()
            tasks = self.session.query(Task).all()
            
            
            
    def onSelectItem(self, event):
        """
        when an idea is selected the data panel on the right needs to be updated
        """
        
        
        self.ideaTitleTextBox.SetValue()
        self.ideaDetailsTextBox.SetValue()
        self.ideaCreateDate.SetValue()
        self.ideaCompleteDate.SetValue()
        self.ideaStartDate.SetValue()
        
        