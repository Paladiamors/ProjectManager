'''
Created on Aug 5, 2013

@author: justin
'''
import wx, wx.lib.customtreectrl, wx.gizmos
try:
    import treemixin 
except ImportError:
    from wx.lib.mixins import treemixin

overview = treemixin.__doc__


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

class TreeModel(object):
    ''' TreeModel holds the domain objects that are shown in the different
    tree controls. Each domain object is simply a two-tuple consisting of
    a label and a list of child tuples, i.e. (label, [list of child tuples]). 
    '''
    def __init__(self, *args, **kwargs):
        self.items = []
        self.itemCounter = 0
        super(TreeModel, self).__init__(*args, **kwargs)

    def GetItem(self, indices):
        text, children = 'Hidden root', self.items
        for index in indices:
            text, children = children[index]
        return text, children

    def GetText(self, indices):
        return self.GetItem(indices)[0]

    def GetChildren(self, indices):
        return self.GetItem(indices)[1]

    def GetChildrenCount(self, indices):
        return len(self.GetChildren(indices))

    def SetChildrenCount(self, indices, count):
        children = self.GetChildren(indices)
        while len(children) > count:
            children.pop()
        while len(children) < count:
            children.append(('item %d'%self.itemCounter, []))
            self.itemCounter += 1

    def MoveItem(self, itemToMoveIndex, newParentIndex):
        itemToMove = self.GetItem(itemToMoveIndex)
        newParentChildren = self.GetChildren(newParentIndex)
        newParentChildren.append(itemToMove)
        oldParentChildren = self.GetChildren(itemToMoveIndex[:-1])
        oldParentChildren.remove(itemToMove)


class DemoTreeMixin(treemixin.VirtualTree, treemixin.DragAndDrop, 
                    treemixin.ExpansionState):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('treemodel')
        self.log = kwargs.pop('log')
        super(DemoTreeMixin, self).__init__(*args, **kwargs)
        self.CreateImageList()

    def CreateImageList(self):
        size = (16, 16)
        self.imageList = wx.ImageList(*size)
        for art in wx.ART_FOLDER, wx.ART_FILE_OPEN, wx.ART_NORMAL_FILE:
            self.imageList.Add(wx.ArtProvider.GetBitmap(art, wx.ART_OTHER, 
                                                        size))
        self.AssignImageList(self.imageList)

    def OnGetItemText(self, indices):
        return self.model.GetText(indices)

    def OnGetChildrenCount(self, indices):
        return self.model.GetChildrenCount(indices)

    def OnGetItemFont(self, indices):
        # Show how to change the item font. Here we use a small font for
        # items that have children and the default font otherwise.
        if self.model.GetChildrenCount(indices) > 0:
            return wx.SMALL_FONT
        else:
            return super(DemoTreeMixin, self).OnGetItemFont(indices)

    def OnGetItemTextColour(self, indices):
        # Show how to change the item text colour. In this case second level
        # items are coloured red and third level items are blue. All other
        # items have the default text colour.
        if len(indices) % 2 == 0:
            return wx.RED
        elif len(indices) % 3 == 0:
            return wx.BLUE
        else:
            return super(DemoTreeMixin, self).OnGetItemTextColour(indices)

    def OnGetItemBackgroundColour(self, indices):
        # Show how to change the item background colour. In this case the
        # background colour of each third item is green.
        if indices[-1] == 2:
            return wx.GREEN
        else: 
            return super(DemoTreeMixin, 
                         self).OnGetItemBackgroundColour(indices)

    def OnGetItemImage(self, indices, which):
        # Return the right icon depending on whether the item has children.
        if which in [wx.TreeItemIcon_Normal, wx.TreeItemIcon_Selected]:
            if self.model.GetChildrenCount(indices):
                return 0
            else:
                return 2
        else:
            return 1

    def OnDrop(self, dropTarget, dragItem):
        dropIndex = self.GetIndexOfItem(dropTarget)
        dropText = self.model.GetText(dropIndex)
        dragIndex = self.GetIndexOfItem(dragItem)
        dragText = self.model.GetText(dragIndex)
        self.log.write('drop %s %s on %s %s'%(dragText, dragIndex,
            dropText, dropIndex))
        self.model.MoveItem(dragIndex, dropIndex)
        self.GetParent().RefreshItems()


class VirtualTreeListCtrl(DemoTreeMixin, wx.gizmos.TreeListCtrl):
    def __init__(self, *args, **kwargs):
        kwargs['style'] = wx.TR_DEFAULT_STYLE | wx.TR_FULL_ROW_HIGHLIGHT
        super(VirtualTreeListCtrl, self).__init__(*args, **kwargs)
        self.AddColumn('Column 0')
        self.AddColumn('Column 1')

    def OnGetItemText(self, indices, column=0):
        # Return a different label depending on column.
        return '%s, column %d'%\
            (super(VirtualTreeListCtrl, self).OnGetItemText(indices), column)

    def GetIndicesOfSelectedItems(self):

        if self.GetSelections():
            return [self.GetIndexOfItem(item) for item in self.GetSelections()]
        else:
            return [()]

    def RefreshItems(self):

        self.RefreshItems()
        self.UnselectAll()
        

class TreeNotebook(wx.Notebook):
    def __init__(self, *args, **kwargs):
        treemodel = kwargs.pop('treemodel')
        log = kwargs.pop('log')
        super(TreeNotebook, self).__init__(*args, **kwargs)
        self.trees = []
        for class_, title in [(VirtualTreeListCtrl, 'TreeListCtrl')]:
            tree = class_(self, treemodel=treemodel, log=log)
            self.trees.append(tree)
            self.AddPage(tree, title)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)

    def OnPageChanged(self, event):
        oldTree = self.GetPage(event.OldSelection)
        newTree = self.GetPage(event.Selection)
        newTree.RefreshItems()
        newTree.SetExpansionState(oldTree.GetExpansionState())
        event.Skip()

    def GetIndicesOfSelectedItems(self):
        tree = self.trees[self.GetSelection()]
        if tree.GetSelections():
            return [tree.GetIndexOfItem(item) for item in tree.GetSelections()]
        else:
            return [()]

    def RefreshItems(self):
        tree = self.trees[self.GetSelection()]
        tree.RefreshItems()
        tree.UnselectAll()


class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        super(TestPanel, self).__init__(parent)
        self.treemodel = TreeModel()
        self.CreateControls()
        self.LayoutControls()

    def CreateControls(self):
        self.notebook = TreeNotebook(self, treemodel=self.treemodel, 
                                     log=self.log)
        self.label = wx.StaticText(self, label='Number of children: ')
        self.childrenCountCtrl = wx.SpinCtrl(self, value='0', max=10000)
        self.button = wx.Button(self, label='Update children')
        self.button.Bind(wx.EVT_BUTTON, self.OnEnter)

    def LayoutControls(self):
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        options = dict(flag=wx.ALIGN_CENTER_VERTICAL|wx.ALL, border=2)
        hSizer.Add(self.label, **options)
        hSizer.Add(self.childrenCountCtrl, 2, **options)
        hSizer.Add(self.button, **options)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.EXPAND)
        sizer.Add(hSizer, 0, wx.EXPAND)
        self.SetSizer(sizer)

    def OnEnter(self, event):
        indicesList = self.notebook.GetIndicesOfSelectedItems()
        newChildrenCount = self.childrenCountCtrl.GetValue()
        for indices in indicesList:
            text = self.treemodel.GetText(indices)
            oldChildrenCount = self.treemodel.GetChildrenCount(indices)
            self.log.write('%s %s now has %d children (was %d)'%(text, indices,
                newChildrenCount, oldChildrenCount))
            self.treemodel.SetChildrenCount(indices, newChildrenCount)
        self.notebook.RefreshItems()


def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win


if __name__ == '__main__':
    import sys, os, run
    run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])

