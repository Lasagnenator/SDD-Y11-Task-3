# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bowling Scoring System", pos = wx.DefaultPosition, size = wx.Size( 1220,800 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"Players", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		bSizer4.Add( self.m_staticText121, 0, wx.ALL, 5 )


		bSizer4.Add( ( 80, 0), 1, wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer4.Add( self.m_staticText2, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer4.Add( self.m_staticText7, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer4.Add( self.m_staticText8, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer4.Add( self.m_staticText9, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer4.Add( self.m_staticText10, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer4.Add( self.m_staticText11, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer4.Add( self.m_staticText13, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		bSizer4.Add( self.m_staticText131, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer4, 0, wx.LEFT, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		self.m_scrolledWindow2.SetMaxSize( wx.Size( -1,580 ) )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.PlayerPanel1 = PlayerPanel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		bSizer8.Add( self.PlayerPanel1, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.PlayerPanel2 = PlayerPanel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		bSizer8.Add( self.PlayerPanel2, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.PlayerPanel3 = PlayerPanel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		bSizer8.Add( self.PlayerPanel3, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.PlayerPanel4 = PlayerPanel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		bSizer8.Add( self.PlayerPanel4, 0, wx.TOP|wx.BOTTOM|wx.LEFT|wx.EXPAND, 5 )

		self.PlayerPanel5 = PlayerPanel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		bSizer8.Add( self.PlayerPanel5, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )

		self.PlayerPanel6 = PlayerPanel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		bSizer8.Add( self.PlayerPanel6, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 5 )


		self.m_scrolledWindow2.SetSizer( bSizer8 )
		self.m_scrolledWindow2.Layout()
		bSizer8.Fit( self.m_scrolledWindow2 )
		bSizer3.Add( self.m_scrolledWindow2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 0 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

		self.m_radioBtn3 = wx.RadioButton( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn3, 0, wx.ALL, 5 )

		self.m_radioBtn4 = wx.RadioButton( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn4, 0, wx.ALL, 5 )

		self.m_radioBtn5 = wx.RadioButton( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn5, 0, wx.ALL, 5 )

		self.m_radioBtn6 = wx.RadioButton( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn6, 0, wx.ALL, 5 )

		self.m_radioBtn7 = wx.RadioButton( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn7, 0, wx.ALL, 5 )

		self.m_radioBtn8 = wx.RadioButton( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn8, 0, wx.ALL, 5 )

		self.m_radioBtn9 = wx.RadioButton( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn9, 0, wx.ALL, 5 )

		self.m_radioBtn10 = wx.RadioButton( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn10, 0, wx.ALL, 5 )

		self.m_radioBtn11 = wx.RadioButton( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn11, 0, wx.ALL, 5 )

		self.m_radioBtn12 = wx.RadioButton( self, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_radioBtn12, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.EnterButton = wx.Button( self, wx.ID_ANY, u"Enter Score", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.EnterButton, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn3.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn4.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn5.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn6.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn7.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn8.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn9.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn10.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn11.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.m_radioBtn12.Bind( wx.EVT_RADIOBUTTON, self.UpdateCurrentScoreInput )
		self.EnterButton.Bind( wx.EVT_BUTTON, self.EnterScore )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def UpdateCurrentScoreInput( self, event ):
		event.Skip()












	def EnterScore( self, event ):
		event.Skip()


###########################################################################
## Class NumberOfPlayersFrame
###########################################################################

class NumberOfPlayersFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Number of Players", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_NO_TASKBAR|wx.STAY_ON_TOP|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer176 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Number of Players", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		bSizer176.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10, 10 )
		bSizer176.Add( self.m_spinCtrl2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.OkButton = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer176.Add( self.OkButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer28.Add( bSizer176, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.SetSizer( bSizer28 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.OkButton.Bind( wx.EVT_BUTTON, self.OkButtonClicked )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OkButtonClicked( self, event ):
		event.Skip()


###########################################################################
## Class NamesOfPlayersFrame
###########################################################################

class NamesOfPlayersFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Names of Players", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.FRAME_NO_TASKBAR|wx.STAY_ON_TOP|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer177 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Names of players", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer177.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer180 = wx.BoxSizer( wx.VERTICAL )

		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer181.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_textCtrl257 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer181.Add( self.m_textCtrl257, 0, wx.ALL, 5 )


		bSizer180.Add( bSizer181, 1, wx.EXPAND, 5 )


		bSizer177.Add( bSizer180, 1, wx.EXPAND, 5 )

		self.OkButton = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer177.Add( self.OkButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer177 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.OkButton.Bind( wx.EVT_BUTTON, self.OkButtonClicked )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OkButtonClicked( self, event ):
		event.Skip()


###########################################################################
## Class PlayerPanel
###########################################################################

class PlayerPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,90 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.PlayerNameTextBox = wx.TextCtrl( self, wx.ID_ANY, u"Player 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PlayerNameTextBox.SetMaxSize( wx.Size( -1,35 ) )

		bSizer1.Add( self.PlayerNameTextBox, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		gSizer1 = wx.GridSizer( 1, 11, 0, 0 )

		self.Frame1 = SingleFramePanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 97,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.Frame1.SetMaxSize( wx.Size( 97,90 ) )

		gSizer1.Add( self.Frame1, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Frame2 = SingleFramePanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 97,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.Frame2.SetMaxSize( wx.Size( 97,90 ) )

		gSizer1.Add( self.Frame2, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Frame3 = SingleFramePanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 97,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.Frame3.SetMaxSize( wx.Size( 97,90 ) )

		gSizer1.Add( self.Frame3, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Frame4 = SingleFramePanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 97,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.Frame4.SetMaxSize( wx.Size( 97,90 ) )

		gSizer1.Add( self.Frame4, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Frame5 = SingleFramePanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 97,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.Frame5.SetMaxSize( wx.Size( 97,90 ) )

		gSizer1.Add( self.Frame5, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Frame6 = SingleFramePanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 97,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.Frame6.SetMaxSize( wx.Size( 97,90 ) )

		gSizer1.Add( self.Frame6, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Frame7 = SingleFramePanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 97,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.Frame7.SetMaxSize( wx.Size( 97,90 ) )

		gSizer1.Add( self.Frame7, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Frame8 = SingleFramePanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 97,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.Frame8.SetMaxSize( wx.Size( 97,90 ) )

		gSizer1.Add( self.Frame8, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Frame9 = SingleFramePanel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 97,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.Frame9.SetMaxSize( wx.Size( 97,90 ) )

		gSizer1.Add( self.Frame9, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Frame10 = Frame10Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 97,90 ), wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.Frame10.SetMaxSize( wx.Size( 97,90 ) )

		gSizer1.Add( self.Frame10, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Total = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,90 ), wx.TE_CENTER|wx.TE_READONLY )
		self.Total.SetMaxSize( wx.Size( 80,80 ) )

		gSizer1.Add( self.Total, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer1.Add( gSizer1, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class Frame10Panel
###########################################################################

class Frame10Panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 97,90 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 97,90 ) )
		self.SetMaxSize( wx.Size( 97,90 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.Bowl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,45 ), wx.TE_CENTER|wx.TE_READONLY )
		self.Bowl1.SetMaxSize( wx.Size( 30,45 ) )

		bSizer2.Add( self.Bowl1, 0, 0, 5 )

		self.Bowl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,45 ), wx.TE_CENTER|wx.TE_READONLY )
		self.Bowl2.SetMaxSize( wx.Size( 30,45 ) )

		bSizer2.Add( self.Bowl2, 0, 0, 5 )

		self.Bowl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,45 ), wx.TE_READONLY )
		self.Bowl3.SetMaxSize( wx.Size( 30,45 ) )

		bSizer2.Add( self.Bowl3, 0, 0, 5 )


		bSizer1.Add( bSizer2, 0, 0, 5 )

		self.SubTotal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,45 ), wx.TE_READONLY|wx.TE_RIGHT )
		self.SubTotal.SetMaxSize( wx.Size( 90,45 ) )

		bSizer1.Add( self.SubTotal, 0, 0, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class SingleFramePanel
###########################################################################

class SingleFramePanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 97,90 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 97,90 ) )
		self.SetMaxSize( wx.Size( 97,90 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.Bowl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,45 ), wx.TE_CENTER|wx.TE_READONLY )
		self.Bowl1.SetMaxSize( wx.Size( 45,45 ) )

		bSizer2.Add( self.Bowl1, 0, 0, 5 )

		self.Bowl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,45 ), wx.TE_CENTER|wx.TE_READONLY )
		self.Bowl2.SetMaxSize( wx.Size( 45,45 ) )

		bSizer2.Add( self.Bowl2, 0, 0, 5 )


		bSizer1.Add( bSizer2, 0, 0, 0 )

		self.SubTotal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,45 ), wx.TE_READONLY|wx.TE_RIGHT )
		self.SubTotal.SetMaxSize( wx.Size( 90,45 ) )

		bSizer1.Add( self.SubTotal, 0, 0, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

	def __del__( self ):
		pass


