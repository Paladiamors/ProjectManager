'''
Created on Aug 10, 2013

@author: justinyho
'''

from UI import MyFrame2
from model import getSession, Idea, Project, Task
from UI.treeListCtrl import TreeListCtrl
from UI.ListCtrl import ListCtrl
from ObjectListView import ObjectListView, ColumnDefn
import wx
from model import Idea, Project, Task 
import traceback, sys
from config import configDict
import common

debugMode = False

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
        self.ideaList = ObjectListView( self.m_panel15, style = wx.LC_REPORT )
        self.bSizer20.Add( self.ideaList, 1, wx.EXPAND, 0 )
        
        
        dateConverter = lambda date: date.strftime("%Y-%m-%d") if date else ""
#         self.ideaList.AddColumns(self.ideaListCols)
        self.ideaList.SetColumns([
            ColumnDefn("Title", "left", 100, "ideaTitle"),
            ColumnDefn("Create Date", "left", 150, "creationDate", stringConverter = "%Y-%m-%d"),
            ColumnDefn("Completion Date", "left", 150, "completeDate", stringConverter = dateConverter)
        ])
        
        self.ideaList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onSelectItem )
        self.addIdeaButton.Bind( wx.EVT_BUTTON, self.onAddIdea )
        
        #adding data into the idea list
        ideas = self.session.query(Idea).all()
        self.ideaList.AddObjects(ideas)
        
    def populateData(self):
        """
        populates data for the class
        """
        
        def _getIdeas():
            ideas = self.session.query(Idea).all()
            
            
            projects = self.session.query(Project).all()
            tasks = self.session.query(Task).all()
            
            
    def onAddIdea(self, event):

#         self.ideaList.SetColumns([
#             ColumnDefn("Title", "left", 100, "ideaTitle"),
#             ColumnDefn("Create Date", "left", 150, "creationDate"),
#             ColumnDefn("Completion Date", "left", 150, "completeDate"),
#         ])        
        newIdea = Idea(ideaTitle = "New Idea", ideaDetails = "",
                       completeDate = None)
       
        self.ideaList.AddObject(newIdea)
        self.ideaList.AutoSizeColumns()
        self.session.add(newIdea)
        
        
        
    def onSelectItem(self, event):
        """
        when an idea is selected the data panel on the right needs to be updated
        """
        
        #TODO: Really clunky
        
        data = self.ideaList.GetSelectedObject()
        title = data.ideaTitle
        details = data.ideaDetails
        createDate = common.py2wxDatetime(data.creationDate)
        completeDate = common.py2wxDatetime(data.completeDate) if data.completeDate else wx.DateTime()
        startDate = common.py2wxDatetime(data.startDate) if data.startDate else wx.DateTime()
        

#         selection = self.ideaList.GetFirstSelected()
#         itemID = self.ideaList.GetItemData(selection)
#         data = self.ideaList.itemDataMap[itemID]
#         title = data[0]
#         createDate = data[1] if data[1] else wx.DateTime()
#         completeDate = data[2] if data[2] else wx.DateTime()
#         startDate = data[3] if data[3] else wx.DateTime()
#         details = data[4]
        
        
        self.ideaTitleTextBox.SetValue(title)
        self.ideaDetailsTextBox.SetValue(details)
        self.ideaCreateDate.SetValue(createDate)
        self.ideaCompleteDate.SetValue(completeDate)
        self.ideaStartDate.SetValue(startDate)
        
    def onIdeaTitleUpdate(self, event):
        
        data = self.ideaList.GetSelectedObject()
        
        ideaTitle = self.ideaTitleTextBox.GetValue()        
        data.ideaTitle = ideaTitle
        self.ideaList.RefreshObject(data)
#        Old way of doing this, without the OLV 
#         selection = self.ideaList.GetFirstSelected()
#         self.ideaList.SetStringItem(selection, 0, self.ideaTitleTextBox.GetValue())
        
    def onIdeaDetailsUpdate(self, event):


        data = self.ideaList.GetSelectedObject()
        
        ideaDetails = self.ideaDetailsTextBox.GetValue()        
        data.ideaDetails = ideaDetails
        self.ideaList.RefreshObject(data)
                
#         selection = self.ideaList.GetFirstSelected()
#         self.ideaList.SetStringItem(selection, 0, self.ideaTitleTextBox.GetValue())

    def onUpdateIdeaStartDate(self, event):
        """
        updates the data object with the new value
        """
        print "updating start date"
        data = self.ideaList.GetSelectedObject()
        
        print "current start date", data.startDate
        date = self.ideaStartDate.GetValue()
        data.startDate = common.wx2pyDatetime(date)

        print "new startDate", data.startDate
        print "old startDate", self.ideaList.GetSelectedObject().startDate

    def onUpdateIdeaCreateDate(self, event):

        """
        updates the data object with the new value
        """
        print "updating start date"
        data = self.ideaList.GetSelectedObject()
        
        print "current start date", data.creationDate
        date = self.ideaCreateDate.GetValue()
        data.creationDate = common.wx2pyDatetime(date)

        print "new startDate", data.creationDate
        print "old startDate", self.ideaList.GetSelectedObject().creationDate

    def onUpdateIdeaCompleteDate(self, event):

        """
        updates the data object with the new value
        """
        print "updating complete date"
        data = self.ideaList.GetSelectedObject()
        
        print "current complete date", data.completeDate
        date = self.ideaCompleteDate.GetValue()
        data.completeDate = common.wx2pyDatetime(date)

        print "new completeDate", data.completeDate
        print "old completeDate", self.ideaList.GetSelectedObject().completeDate
        
        self.ideaList.RefreshObject(data)
    
    def SaveData(self, event):
        """
        saves data on exit
        """
        self.session.commit()
        self.Destroy()
        
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