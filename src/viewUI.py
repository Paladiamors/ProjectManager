'''
Created on Aug 10, 2013

@author: justinyho
'''

from UI import MyFrame2
from model import getSession, Idea, Project, Task
from UI.treeListCtrl import TreeListCtrl
from UI.ListCtrl import ListCtrl
import wx
from model import Idea, Project, Task 
import traceback, sys
from config import configDict

debugMode = True

if debugMode:
    configDict["dbPath"] = "sqlite:///:memory:"
    
def show_error():
    message = ''.join(traceback.format_exception(*sys.exc_info()))
    dialog = wx.MessageDialog(None, message, 'Error!', wx.OK|wx.ICON_ERROR)
    dialog.ShowModal()
    
class MainFrame(MyFrame2):
    
    def __init__(self, parent):
        MyFrame2.__init__ ( self, parent)
        Session = getSession(configDict["dbPath"])
        self.session = Session()
        self.ideaListCols = ["Title", "Create Date", "Start Date"]
        self.initControls()
        
    def initControls(self):
        
        #populating the idea list here
        self.ideaList.Destroy()
        self.ideaList = ListCtrl( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON|wx.LC_REPORT )
        self.bSizer20.Add( self.ideaList, 1, wx.EXPAND, 0 )
        
        self.ideaList.AddColumns(self.ideaListCols)
        self.ideaList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onSelectItem )
        self.addIdeaButton.Bind( wx.EVT_BUTTON, self.onAddIdea )
        
        ideas = self.session.query(Idea).all()
        
    def populateData(self):
        """
        populates data for the class
        """
        
        def _getIdeas():
            ideas = self.session.query(Idea).all()
            
            
            projects = self.session.query(Project).all()
            tasks = self.session.query(Task).all()
            
            
    def onAddIdea(self, event):
        
        newData = ["New Idea", #title
                   None, #creationDate
                   None, #completion date
                   None, #start date
                   "", #Details
                   Idea(), #a new idea
                   False] #modified flag
        
        
        self.ideaList.AddRow(newData)
        self.Refresh()
        
        
        
    def onSelectItem(self, event):
        """
        when an idea is selected the data panel on the right needs to be updated
        """
        
        #TODO: Really clunky
        selection = self.ideaList.GetFirstSelected()
        itemID = self.ideaList.GetItemData(selection)
        data = self.ideaList.itemDataMap[itemID]
        title = data[0]
        createDate = data[1] if data[1] else wx.DateTime()
        completeDate = data[2] if data[2] else wx.DateTime()
        startDate = data[3] if data[3] else wx.DateTime()
        details = data[4]
        
        
        self.ideaTitleTextBox.SetValue(title)
        self.ideaDetailsTextBox.SetValue(details)
        self.ideaCreateDate.SetValue(createDate)
        self.ideaCompleteDate.SetValue(completeDate)
        self.ideaStartDate.SetValue(startDate)
        
    def onIdeaTitleUpdate(self, event):
        
        selection = self.ideaList.GetFirstSelected()
        self.ideaList.SetStringItem(selection, 0, self.ideaTitleTextBox.GetValue())

def main():
    app = wx.App()
    try:
        frame = MainFrame(None)
        frame.Show()
        app.MainLoop()
    except:
        show_error()

if __name__ == '__main__':
    main()