'''
Created on Aug 8, 2013

@author: justin
'''
import wx
import sys
import traceback

import wx, wx.lib.customtreectrl, wx.gizmos
try:
    import treemixin 
except ImportError:
    from wx.lib.mixins import treemixin

overview = treemixin.__doc__

def show_error():
    message = ''.join(traceback.format_exception(*sys.exc_info()))
    dialog = wx.MessageDialog(None, message, 'Error!', wx.OK|wx.ICON_ERROR)
    dialog.ShowModal()

class TreeListCtrl(treemixin.VirtualTree, treemixin.DragAndDrop, 
                    treemixin.ExpansionState, wx.gizmos.TreeListCtrl):

    '''holds the domain objects that are shown in the different
    tree controls. Each domain object is simply a two-tuple consisting of
    a label and a list of child tuples, i.e. ([list of labels], [list of child tuples]). 
    '''    
    
    def __init__(self, *args, **kwargs):
        self.items = []
        self.itemCounter = 0
        kwargs['style'] = wx.TR_DEFAULT_STYLE | wx.TR_FULL_ROW_HIGHLIGHT
        super(TreeListCtrl, self).__init__(*args, **kwargs)
        
        self.AddColumn('Column 0')
        self.AddColumn('Column 1')
        self.AddColumn('Column 2')

        self.AddChild((), ["value1", "value2", "value3"])
        self.AddChild((), ["value8", "value2", "value3"])
        self.AddChild((1,), ["value7", "value5", "value6"])
        self.AddChild((1,), ["value4", "value5", "value6"])
        self.RefreshItems()
    
    #Helper functions
    def GetItem(self, indices):
        text, children = 'Hidden root', self.items
        for index in indices:
            text, children = children[index]
        return text, children

    def GetText(self, indices, column):
        return self.GetItem(indices)[0][column]

    def GetChildren(self, indices):
        return self.GetItem(indices)[1]

    def GetChildrenCount(self, indices):
        return len(self.GetChildren(indices))

    def AddChild(self, indicies, labels):
        """
        Adds a child to the tree
        """
        self.GetChildren(indicies).append((labels, []))
    
    def RemoveChild(self, indicies):
        """
        Removes a child from the tree
        """
        pass

    #For moving items around
    def MoveItem(self, itemToMoveIndex, newParentIndex):
        itemToMove = self.GetItem(itemToMoveIndex)
        newParentChildren = self.GetChildren(newParentIndex)
        newParentChildren.append(itemToMove)
        oldParentChildren = self.GetChildren(itemToMoveIndex[:-1])
        oldParentChildren.remove(itemToMove)
    #overloading for virtual tree
    def OnGetItemText(self, indices, column=0):
        return self.GetText(indices, column)

    def OnGetChildrenCount(self, indices):
        return self.GetChildrenCount(indices)

    #Overloading for drag and drop
    def OnDrop(self, dropTarget, dragItem):
        dropIndex = self.GetIndexOfItem(dropTarget)
        #dropText = self.GetText(dropIndex,0)
        dragIndex = self.GetIndexOfItem(dragItem)
        #dragText = self.GetText(dragIndex)

        self.MoveItem(dragIndex, dropIndex)
        self.RefreshItems()


# class VirtualTreeListCtrl(DemoTreeMixin, wx.gizmos.TreeListCtrl):
#     def __init__(self, *args, **kwargs):
#         kwargs['style'] = wx.TR_DEFAULT_STYLE | wx.TR_FULL_ROW_HIGHLIGHT
#         super(VirtualTreeListCtrl, self).__init__(*args, **kwargs)
#         self.AddColumn('Column 0')
#         self.AddColumn('Column 1')
#         self.AddColumn('Column 2')
# 
#         self.model.AddChild((), ["value1", "value2", "value3"])
#         self.model.AddChild((), ["value1", "value2", "value3"])
#         self.model.AddChild((1,), ["value4", "value5", "value6"])
#         self.model.AddChild((1,), ["value4", "value5", "value6"])
#         self.RefreshItems()
# #     def OnGetItemText(self, indices, column=0):
# #         # Return a different label depending on column.
# #         return '%s, column %d'%\
# #             (super(VirtualTreeListCtrl, self).OnGetItemText(indices), column)
# 
#     def GetIndicesOfSelectedItems(self):
# 
#         if self.GetSelections():
#             return [self.GetIndexOfItem(item) for item in self.GetSelections()]
#         else:
#             return [()]
        
class Frame ( wx.Frame ):
    
    def __init__( self, parent, title ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        MainSizer = wx.BoxSizer( wx.VERTICAL )
        
        TopSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        TopLeftSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.index = 0 
        
        #self.TestControl = wxP.ListCtrl( self, style = wx.LC_REPORT|wx.LC_EDIT_LABELS )
        self.TestControl = TreeListCtrl(self)
        TopLeftSizer.Add( self.TestControl, 1, wx.ALL|wx.EXPAND, 5 )

        #self.InitializeControl()
        
        
        TopSizer.Add( TopLeftSizer, 1, wx.EXPAND, 5 )
        
        TopRightSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"AddRow", wx.DefaultPosition, wx.DefaultSize, 0 )
        TopRightSizer.Add( self.m_button1, 0, wx.ALL, 1 )
        self.m_button1.Bind(wx.EVT_BUTTON, self.onAddRow)
        
        self.m_button2 = wx.Button( self, wx.ID_ANY, u"DeleteRow", wx.DefaultPosition, wx.DefaultSize, 0 )
        TopRightSizer.Add( self.m_button2, 0, wx.ALL, 1 )
        self.m_button2.Bind(wx.EVT_BUTTON, self.onDeleteRow)
        
        self.m_button3 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        TopRightSizer.Add( self.m_button3, 0, wx.ALL, 1 )
        
        
        TopSizer.Add( TopRightSizer, 0, wx.EXPAND, 5 )
        
        
        MainSizer.Add( TopSizer, 1, wx.EXPAND, 5 )
        
        BottomSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        BottomSizer.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        MainSizer.Add( BottomSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( MainSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
    
    def InitializeControl(self):
        
        for x in range(4):
            self.TestControl.AddRow(["Row %s" % x, "Some value", "Another Value"])
            self.index += 1
        
        self.TestControl.AutoSizeCols()
    
    def onAddRow(self, event):
        self.TestControl.AddRow(["Row %s" % self.index, "Some value", "Another Value"])
        self.index += 1
    
    def onDeleteRow(self, event):
        self.TestControl.DeleteItem(self.TestControl.GetFirstSelected())
    
    def __del__( self ):
        pass
    


def main():
    app = wx.App()
    try:
        frame = Frame(None, "Test Application")
        frame.Show()
        app.MainLoop()
    except:
        show_error()

if __name__ == '__main__':
    main()