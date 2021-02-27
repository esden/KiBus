# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 20 2021)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from wx.lib.agw.ultimatelistctrl import ULC_REPORT, UltimateListCtrl
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
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.net_list = UltimateListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT,agwStyle=ULC_REPORT )
		bSizer5.Add( self.net_list, 1, wx.ALL|wx.EXPAND, 5 )

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
		self.gnet_list.SetColLabelSize( 30 )
		self.gnet_list.SetColLabelValue( 0, u"Net" )
		self.gnet_list.SetColLabelValue( 1, u"Len" )
		self.gnet_list.SetColLabelValue( 2, u"dMed" )
		self.gnet_list.SetColLabelValue( 3, u"dMax" )
		self.gnet_list.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gnet_list.AutoSizeRows()
		self.gnet_list.EnableDragRowSize( True )
		self.gnet_list.SetRowLabelSize( 0 )
		self.gnet_list.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gnet_list.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer5.Add( self.gnet_list, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.chk_cont = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Continuous refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.chk_cont, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.lbl_refresh_time = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Refresh time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl_refresh_time.Wrap( -1 )

		bSizer2.Add( self.lbl_refresh_time, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer2, 0, wx.EXPAND, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_refresh = wx.Button( self.m_panel1, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btn_refresh, 0, wx.ALL, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_ok = wx.Button( self.m_panel1, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btn_ok, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer5.Add( bSizer3, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer5 )
		self.m_panel1.Layout()
		bSizer5.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.net_list.Bind( wx.EVT_LIST_COL_CLICK, self.sort_items )
		self.net_list.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.item_selected )
		self.net_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.item_selected )
		self.net_list.Bind( wx.EVT_LIST_KEY_DOWN, self.delete_items )
		self.chk_cont.Bind( wx.EVT_CHECKBOX, self.cont_refresh_toggle )
		self.btn_refresh.Bind( wx.EVT_BUTTON, self.on_btn_refresh )
		self.btn_ok.Bind( wx.EVT_BUTTON, self.on_btn_ok )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def sort_items( self, event ):
		event.Skip()

	def item_selected( self, event ):
		event.Skip()


	def delete_items( self, event ):
		event.Skip()

	def cont_refresh_toggle( self, event ):
		event.Skip()

	def on_btn_refresh( self, event ):
		event.Skip()

	def on_btn_ok( self, event ):
		event.Skip()


