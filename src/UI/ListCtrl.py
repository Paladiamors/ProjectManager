'''
Created on Aug 13, 2013

@author: justinyho
'''

import  wx
import  wx.lib.mixins.listctrl  as  listmix

class ListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

        self.itemDataMap = {}
        self.itemCounter = 0
        self.numCols = 0
    
    def SetItemDataMap(self, dataMap):
        self.itemDataMap = dataMap
        self.items = len(dataMap)
        
    def AddData(self, rowData):
        self.itemDataMap[self.items] = rowData
        self.items += 1
    
    def RemoveData(self, idKey):
        self.itemDataMap.pop(idKey)
    
    def AddColumns(self, columns):
        """
        adds columns into the list control
        """
        
        #TODO: Hacky, does not account for when AddColumns is called twice
        for index,header in zip(range(self.numCols, len(columns)), columns):
            self.InsertColumn(index, header)        
        
        #autosizing the columns but the last one
        #for index in range(self.numCols, len(columns)-1):
        #    self.SetColumnWidth(index, wx.LIST_AUTOSIZE)

        self.numCols += len(columns)
                              
    def AddRow(self, rowList, rowIndex = None):
        """
        rowList is a list of string values to be added into the ListCtrl
        We keep a copy of the original data in the itemDataMap and use that data
        to do the sorting while just manipulating what is shown in the ListControl
        """
        
        if not rowIndex:
            rowIndex = self.GetItemCount()
        colIndicies = range(self.numCols)
        
        for colIndex in colIndicies:
            #if the object is the first in the row
            if colIndex == 0:
                self.InsertStringItem(rowIndex,str(rowList[colIndex]))
            else: #otherwise use this command
                self.SetStringItem(rowIndex,colIndex, str(rowList[colIndex]))
        
        self.itemDataMap[self.itemCounter] = rowList
        self.SetItemData(rowIndex, self.itemCounter)
        self.itemCounter += 1
        
       