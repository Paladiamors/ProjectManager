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
        self.items = 0
    
    def setItemDataMap(self, dataMap):
        self.itemDataMap = dataMap
        self.items = len(dataMap)
        
    def addData(self, rowData):
        self.itemDataMap[self.items] = rowData
        self.items += 1
    
    def removeData(self, idKey):
        self.itemDataMap.pop(idKey)
        