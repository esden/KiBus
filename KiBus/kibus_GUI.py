# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-368-g19bcc292)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class KiBusGUI
###########################################################################

class KiBusGUI ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"KiBus", pos = wx.DefaultPosition, size = wx.Size( 446,522 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl_bus = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Bus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_bus.Wrap( -1 )

		bSizer111.Add( self.lbl_bus, 0, wx.ALL, 5 )

		choice_busChoices = []
		self.choice_bus = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_busChoices, 0 )
		self.choice_bus.SetSelection( 0 )
		bSizer111.Add( self.choice_bus, 0, wx.ALL, 5 )


		bSizer11.Add( bSizer111, 0, wx.EXPAND, 5 )

		self.gnet_list = wx.grid.Grid( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gnet_list.CreateGrid( 0, 4 )
		self.gnet_list.EnableEditing( False )
		self.gnet_list.EnableGridLines( True )
		self.gnet_list.EnableDragGridSize( True )
		self.gnet_list.SetMargins( 0, 0 )

		# Columns
		self.gnet_list.EnableDragColMove( False )
		self.gnet_list.EnableDragColSize( True )
		self.gnet_list.SetColLabelValue( 0, u"Wire" )
		self.gnet_list.SetColLabelValue( 1, u"Len" )
		self.gnet_list.SetColLabelValue( 2, u"ΔMed" )
		self.gnet_list.SetColLabelValue( 3, u"ΔMax" )
		self.gnet_list.SetColLabelSize( 30 )
		self.gnet_list.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gnet_list.AutoSizeRows()
		self.gnet_list.EnableDragRowSize( True )
		self.gnet_list.SetRowLabelSize( 0 )
		self.gnet_list.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gnet_list.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer11.Add( self.gnet_list, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )

		self.chk_cont = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Continuous refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer112.Add( self.chk_cont, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer112.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.lbl_refresh_time = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Refresh time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_refresh_time.Wrap( -1 )

		bSizer112.Add( self.lbl_refresh_time, 0, wx.ALL, 5 )


		bSizer11.Add( bSizer112, 0, wx.EXPAND, 5 )

		bSizer113 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_refresh = wx.Button( self.m_panel1, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer113.Add( self.btn_refresh, 0, wx.ALL, 5 )


		bSizer113.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_ok = wx.Button( self.m_panel1, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer113.Add( self.btn_ok, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer11.Add( bSizer113, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer11 )
		self.m_panel1.Layout()
		bSizer11.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.choice_bus.Bind( wx.EVT_CHOICE, self.on_choice_bus )
		self.gnet_list.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_grid_cell_lclick )
		self.gnet_list.Bind( wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.on_grid_label_lclick )
		self.gnet_list.Bind( wx.grid.EVT_GRID_RANGE_SELECT, self.on_grid_range_select )
		self.gnet_list.Bind( wx.EVT_KEY_DOWN, self.on_grid_key_down )
		self.chk_cont.Bind( wx.EVT_CHECKBOX, self.cont_refresh_toggle )
		self.btn_refresh.Bind( wx.EVT_BUTTON, self.on_btn_refresh )
		self.btn_ok.Bind( wx.EVT_BUTTON, self.on_btn_ok )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_choice_bus( self, event ):
		event.Skip()

	def on_grid_cell_lclick( self, event ):
		event.Skip()

	def on_grid_label_lclick( self, event ):
		event.Skip()

	def on_grid_range_select( self, event ):
		event.Skip()

	def on_grid_key_down( self, event ):
		event.Skip()

	def cont_refresh_toggle( self, event ):
		event.Skip()

	def on_btn_refresh( self, event ):
		event.Skip()

	def on_btn_ok( self, event ):
		event.Skip()


