# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 897,609 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook2 = wx.Notebook( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.IdeaPanel = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter4 = wx.SplitterWindow( self.IdeaPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter4.Bind( wx.EVT_IDLE, self.m_splitter4OnIdle )
		
		self.m_panel15 = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.ideaList = wx.ListCtrl( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON|wx.LC_REPORT )
		bSizer20.Add( self.ideaList, 1, wx.EXPAND, 0 )
		
		
		self.m_panel15.SetSizer( bSizer20 )
		self.m_panel15.Layout()
		bSizer20.Fit( self.m_panel15 )
		self.IdeaInputPanel = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel17 = wx.Panel( self.IdeaInputPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.AddGrowableCol( 1 )
		fgSizer3.AddGrowableRow( 1 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText8 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		fgSizer3.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.ideaTitleTextBox = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.ideaTitleTextBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Details", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer3.Add( self.m_staticText9, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.ideaDetailsTextBox = wx.TextCtrl( self.m_panel17, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
		fgSizer3.Add( self.ideaDetailsTextBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer22.Add( fgSizer3, 1, wx.EXPAND, 0 )
		
		fgSizer4 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.sLabel_creationDate = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Creation Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sLabel_creationDate.Wrap( -1 )
		fgSizer4.Add( self.sLabel_creationDate, 0, wx.ALL, 5 )
		
		self.sLabel_startDate = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sLabel_startDate.Wrap( -1 )
		fgSizer4.Add( self.sLabel_startDate, 0, wx.ALL, 5 )
		
		self.sLabel_completeDate = wx.StaticText( self.m_panel17, wx.ID_ANY, u"Complete Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sLabel_completeDate.Wrap( -1 )
		fgSizer4.Add( self.sLabel_completeDate, 0, wx.ALL, 5 )
		
		self.ideaCreateDate = wx.DatePickerCtrl( self.m_panel17, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer4.Add( self.ideaCreateDate, 0, wx.ALL, 5 )
		
		self.ideaStartDate = wx.DatePickerCtrl( self.m_panel17, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer4.Add( self.ideaStartDate, 0, wx.ALL, 5 )
		
		self.ideaCompleteDate = wx.DatePickerCtrl( self.m_panel17, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_ALLOWNONE|wx.DP_DEFAULT )
		fgSizer4.Add( self.ideaCompleteDate, 0, wx.ALL, 5 )
		
		
		bSizer22.Add( fgSizer4, 0, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.hideCompletedIdea_cb = wx.CheckBox( self.m_panel17, wx.ID_ANY, u"Hide Completed", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.hideCompletedIdea_cb, 0, wx.ALIGN_CENTER, 5 )
		
		self.addIdeaButton = wx.Button( self.m_panel17, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.addIdeaButton, 0, wx.ALL, 5 )
		
		self.saveIdeaButton = wx.Button( self.m_panel17, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.saveIdeaButton, 0, wx.ALL, 5 )
		
		self.deleteIdeaButton = wx.Button( self.m_panel17, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.deleteIdeaButton, 0, wx.ALL, 5 )
		
		
		bSizer22.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		
		self.m_panel17.SetSizer( bSizer22 )
		self.m_panel17.Layout()
		bSizer22.Fit( self.m_panel17 )
		bSizer21.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.IdeaInputPanel.SetSizer( bSizer21 )
		self.IdeaInputPanel.Layout()
		bSizer21.Fit( self.IdeaInputPanel )
		self.m_splitter4.SplitVertically( self.m_panel15, self.IdeaInputPanel, 0 )
		bSizer19.Add( self.m_splitter4, 1, wx.EXPAND, 5 )
		
		
		self.IdeaPanel.SetSizer( bSizer19 )
		self.IdeaPanel.Layout()
		bSizer19.Fit( self.IdeaPanel )
		self.m_notebook2.AddPage( self.IdeaPanel, u"Ideas", False )
		self.ProjectPanel = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter8 = wx.SplitterWindow( self.ProjectPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter8.Bind( wx.EVT_IDLE, self.m_splitter8OnIdle )
		
		self.m_panel30 = wx.Panel( self.m_splitter8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer42 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_treeCtrl2 = wx.TreeCtrl( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer42.Add( self.m_treeCtrl2, 1, wx.EXPAND, 5 )
		
		
		self.m_panel30.SetSizer( bSizer42 )
		self.m_panel30.Layout()
		bSizer42.Fit( self.m_panel30 )
		self.IdeaInputPanel1 = wx.Panel( self.m_splitter8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer211 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel171 = wx.Panel( self.IdeaInputPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer221 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer31 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer31.AddGrowableCol( 1 )
		fgSizer31.AddGrowableRow( 1 )
		fgSizer31.SetFlexibleDirection( wx.BOTH )
		fgSizer31.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText81 = wx.StaticText( self.m_panel171, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		fgSizer31.Add( self.m_staticText81, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.titleTextBox = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer31.Add( self.titleTextBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText91 = wx.StaticText( self.m_panel171, wx.ID_ANY, u"Details", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		fgSizer31.Add( self.m_staticText91, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.detailsTextBox = wx.TextCtrl( self.m_panel171, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
		fgSizer31.Add( self.detailsTextBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer221.Add( fgSizer31, 1, wx.EXPAND, 0 )
		
		fgSizer41 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer41.SetFlexibleDirection( wx.BOTH )
		fgSizer41.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.sLabel_creationDate1 = wx.StaticText( self.m_panel171, wx.ID_ANY, u"Creation Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sLabel_creationDate1.Wrap( -1 )
		fgSizer41.Add( self.sLabel_creationDate1, 0, wx.ALL, 5 )
		
		self.sLabel_startDate1 = wx.StaticText( self.m_panel171, wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sLabel_startDate1.Wrap( -1 )
		fgSizer41.Add( self.sLabel_startDate1, 0, wx.ALL, 5 )
		
		self.sLabel_completeDate1 = wx.StaticText( self.m_panel171, wx.ID_ANY, u"Complete Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sLabel_completeDate1.Wrap( -1 )
		fgSizer41.Add( self.sLabel_completeDate1, 0, wx.ALL, 5 )
		
		self.ProjectCreateDate = wx.DatePickerCtrl( self.m_panel171, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer41.Add( self.ProjectCreateDate, 0, wx.ALL, 5 )
		
		self.projectStartDate = wx.DatePickerCtrl( self.m_panel171, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		fgSizer41.Add( self.projectStartDate, 0, wx.ALL, 5 )
		
		self.projectCompleteDate = wx.DatePickerCtrl( self.m_panel171, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_ALLOWNONE|wx.DP_DEFAULT )
		fgSizer41.Add( self.projectCompleteDate, 0, wx.ALL, 5 )
		
		
		bSizer221.Add( fgSizer41, 0, wx.EXPAND, 5 )
		
		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.hideCompletedProject_cb = wx.CheckBox( self.m_panel171, wx.ID_ANY, u"Hide Completed", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer241.Add( self.hideCompletedProject_cb, 0, wx.ALIGN_CENTER, 5 )
		
		self.addProjectButton = wx.Button( self.m_panel171, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer241.Add( self.addProjectButton, 0, wx.ALL, 5 )
		
		self.saveProjectButton = wx.Button( self.m_panel171, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer241.Add( self.saveProjectButton, 0, wx.ALL, 5 )
		
		self.deleteProjectButton = wx.Button( self.m_panel171, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer241.Add( self.deleteProjectButton, 0, wx.ALL, 5 )
		
		
		bSizer221.Add( bSizer241, 0, wx.EXPAND, 5 )
		
		
		self.m_panel171.SetSizer( bSizer221 )
		self.m_panel171.Layout()
		bSizer221.Fit( self.m_panel171 )
		bSizer211.Add( self.m_panel171, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.IdeaInputPanel1.SetSizer( bSizer211 )
		self.IdeaInputPanel1.Layout()
		bSizer211.Fit( self.IdeaInputPanel1 )
		self.m_splitter8.SplitVertically( self.m_panel30, self.IdeaInputPanel1, 0 )
		bSizer41.Add( self.m_splitter8, 1, wx.EXPAND, 5 )
		
		
		self.ProjectPanel.SetSizer( bSizer41 )
		self.ProjectPanel.Layout()
		bSizer41.Fit( self.ProjectPanel )
		self.m_notebook2.AddPage( self.ProjectPanel, u"Projects", True )
		self.TodoPanel = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook2.AddPage( self.TodoPanel, u"Todo", False )
		
		bSizer18.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel11.SetSizer( bSizer18 )
		self.m_panel11.Layout()
		bSizer18.Fit( self.m_panel11 )
		bSizer17.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer17 )
		self.Layout()
		self.m_menubar = wx.MenuBar( 0 )
		self.FileMenu = wx.Menu()
		self.New = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileMenu.AppendItem( self.New )
		
		self.Open = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileMenu.AppendItem( self.Open )
		
		self.Save = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileMenu.AppendItem( self.Save )
		
		self.Quit = wx.MenuItem( self.FileMenu, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileMenu.AppendItem( self.Quit )
		
		self.m_menubar.Append( self.FileMenu, u"File" ) 
		
		self.HelpMenu = wx.Menu()
		self.About_mi = wx.MenuItem( self.HelpMenu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.HelpMenu.AppendItem( self.About_mi )
		
		self.m_menubar.Append( self.HelpMenu, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ideaList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onSelectItem )
		self.hideCompletedIdea_cb.Bind( wx.EVT_CHECKBOX, self.onHideCompleteIdea )
		self.addIdeaButton.Bind( wx.EVT_BUTTON, self.OnAddIdea )
		self.saveIdeaButton.Bind( wx.EVT_BUTTON, self.onSaveIdea )
		self.deleteIdeaButton.Bind( wx.EVT_BUTTON, self.onDeleteIdea )
		self.hideCompletedProject_cb.Bind( wx.EVT_CHECKBOX, self.onHideCompleteProject )
		self.addProjectButton.Bind( wx.EVT_BUTTON, self.onAddProject )
		self.saveProjectButton.Bind( wx.EVT_BUTTON, self.onSaveProject )
		self.deleteProjectButton.Bind( wx.EVT_BUTTON, self.onDeleteProject )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSelectItem( self, event ):
		event.Skip()
	
	def onHideCompleteIdea( self, event ):
		event.Skip()
	
	def OnAddIdea( self, event ):
		event.Skip()
	
	def onSaveIdea( self, event ):
		event.Skip()
	
	def onDeleteIdea( self, event ):
		event.Skip()
	
	def onHideCompleteProject( self, event ):
		event.Skip()
	
	def onAddProject( self, event ):
		event.Skip()
	
	def onSaveProject( self, event ):
		event.Skip()
	
	def onDeleteProject( self, event ):
		event.Skip()
	
	def m_splitter4OnIdle( self, event ):
		self.m_splitter4.SetSashPosition( 0 )
		self.m_splitter4.Unbind( wx.EVT_IDLE )
	
	def m_splitter8OnIdle( self, event ):
		self.m_splitter8.SetSashPosition( 0 )
		self.m_splitter8.Unbind( wx.EVT_IDLE )
	

