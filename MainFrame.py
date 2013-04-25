# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.aui

MENU_ID_CLEAR_LOG = 1000
MENU_ID_EXIT = 1001
TOOL_ID_CONFIG = 1002
TOOL_ID_DEVICE_INIT = 1003
TOOL_ID_START_TRACE = 1004
TOOL_ID_SAVE = 1005
TOOL_ID_CLEAR = 1006

###########################################################################
## Class MainFame
###########################################################################

class MainFame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PEPS整车低频标定工具", pos = wx.DefaultPosition, size = wx.Size( 1144,862 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_outer_splitter = wx.SplitterWindow( self.m_main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_outer_splitter.SetSashGravity( 0 )
		self.m_outer_splitter.Bind( wx.EVT_IDLE, self.m_outer_splitterOnIdle )
		self.m_outer_splitter.SetMinimumPaneSize( 100 )
		
		self.m_top_panel = wx.Panel( self.m_outer_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_top_panel_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_content_split = wx.SplitterWindow( self.m_top_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_content_split.Bind( wx.EVT_IDLE, self.m_content_splitOnIdle )
		self.m_content_split.SetMinimumPaneSize( 500 )
		
		self.m_scrolledWindow3 = wx.ScrolledWindow( self.m_content_split, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), wx.HSCROLL|wx.SUNKEN_BORDER|wx.VSCROLL )
		self.m_scrolledWindow3.SetScrollRate( 5, 5 )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"触发控制" ), wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText13 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"触发周期(s)      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer8.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_trigger_period = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_trigger_period, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_lf_period_send = wx.Button( self.m_scrolledWindow3, wx.ID_ANY, u"开始周期触发", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_lf_period_send, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer6.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText251 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"钥匙位置坐标", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText251.Wrap( -1 )
		bSizer36.Add( self.m_staticText251, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer36.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_pos_x = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer36.Add( self.m_pos_x, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer36.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_pos_y = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer36.Add( self.m_pos_y, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText27 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"Z", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		bSizer36.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_pos_z = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer36.Add( self.m_pos_z, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_lf_once_send = wx.Button( self.m_scrolledWindow3, wx.ID_ANY, u"单次触发", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer36.Add( self.m_lf_once_send, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer6.Add( bSizer36, 0, wx.EXPAND, 5 )
		
		sbSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		bSizer7.Add( sbSizer1, 0, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"配置" ), wx.VERTICAL )
		
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"数据天线" ), wx.HORIZONTAL )
		
		self.m_staticText28 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"数据天线选择", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		sbSizer5.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_data_antennaChoices = []
		self.m_data_antenna = wx.Choice( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_data_antennaChoices, 0 )
		self.m_data_antenna.SetSelection( 0 )
		sbSizer5.Add( self.m_data_antenna, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.m_scrolledWindow3, wx.ID_ANY, u"数据天线电流值", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		sbSizer5.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_data_Current_valueChoices = []
		self.m_data_Current_value = wx.Choice( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_data_Current_valueChoices, 0 )
		self.m_data_Current_value.SetSelection( 0 )
		sbSizer5.Add( self.m_data_Current_value, 1, wx.ALL, 5 )
		
		bSizer38.Add( sbSizer5, 0, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"载波天线" ), wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 5, 6, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_IN1_Check = wx.CheckBox( self.m_scrolledWindow3, wx.ID_ANY, u"IN1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IN1_Check.SetValue(True) 
		fgSizer2.Add( self.m_IN1_Check, 0, wx.ALL, 5 )
		
		self.m_IN2_Check = wx.CheckBox( self.m_scrolledWindow3, wx.ID_ANY, u"IN2", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_IN2_Check, 0, wx.ALL, 5 )
		
		self.m_IN3_Check = wx.CheckBox( self.m_scrolledWindow3, wx.ID_ANY, u"IN3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_IN3_Check.SetValue(True) 
		fgSizer2.Add( self.m_IN3_Check, 0, wx.ALL, 5 )
		
		self.m_FL_Check = wx.CheckBox( self.m_scrolledWindow3, wx.ID_ANY, u"FL", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_FL_Check, 0, wx.ALL, 5 )
		
		self.m_FR_Check = wx.CheckBox( self.m_scrolledWindow3, wx.ID_ANY, u"FR", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_FR_Check, 0, wx.ALL, 5 )
		
		self.m_TR_Check = wx.CheckBox( self.m_scrolledWindow3, wx.ID_ANY, u"TR", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_TR_Check, 0, wx.ALL, 5 )
		
		m_IN1_Current_ValueChoices = []
		self.m_IN1_Current_Value = wx.Choice( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_IN1_Current_ValueChoices, 0 )
		self.m_IN1_Current_Value.SetSelection( 0 )
		fgSizer2.Add( self.m_IN1_Current_Value, 1, wx.ALL, 5 )
		
		m_IN2_Current_ValueChoices = []
		self.m_IN2_Current_Value = wx.Choice( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_IN2_Current_ValueChoices, 0 )
		self.m_IN2_Current_Value.SetSelection( 0 )
		fgSizer2.Add( self.m_IN2_Current_Value, 0, wx.ALL, 5 )
		
		m_IN3_Current_ValueChoices = []
		self.m_IN3_Current_Value = wx.Choice( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_IN3_Current_ValueChoices, 0 )
		self.m_IN3_Current_Value.SetSelection( 0 )
		fgSizer2.Add( self.m_IN3_Current_Value, 0, wx.ALL, 5 )
		
		m_FL_Current_ValueChoices = []
		self.m_FL_Current_Value = wx.Choice( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_FL_Current_ValueChoices, 0 )
		self.m_FL_Current_Value.SetSelection( 0 )
		fgSizer2.Add( self.m_FL_Current_Value, 0, wx.ALL, 5 )
		
		m_FR_Current_ValueChoices = []
		self.m_FR_Current_Value = wx.Choice( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_FR_Current_ValueChoices, 0 )
		self.m_FR_Current_Value.SetSelection( 0 )
		fgSizer2.Add( self.m_FR_Current_Value, 0, wx.ALL, 5 )
		
		m_TR_Current_ValueChoices = []
		self.m_TR_Current_Value = wx.Choice( self.m_scrolledWindow3, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_TR_Current_ValueChoices, 0 )
		self.m_TR_Current_Value.SetSelection( 0 )
		fgSizer2.Add( self.m_TR_Current_Value, 0, wx.ALL, 5 )
		
		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"IN1 Threshold" ), wx.VERTICAL )
		
		m_IN1_ThresholdChoices = [ u"RSSI", u"NXP ", u"H" ]
		self.m_IN1_Threshold = wx.RadioBox( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_IN1_ThresholdChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_IN1_Threshold.SetSelection( 1 )
		sbSizer61.Add( self.m_IN1_Threshold, 0, wx.ALL, 5 )
		
		self.m_IN1_threshold_value = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		sbSizer61.Add( self.m_IN1_threshold_value, 0, wx.ALL, 5 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_IN1_NXP_H = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_IN1_NXP_H.Hide()
		
		bSizer26.Add( self.m_IN1_NXP_H, 0, wx.ALL, 5 )
		
		self.m_IN1_NXP_L = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_IN1_NXP_L.Hide()
		
		bSizer26.Add( self.m_IN1_NXP_L, 0, wx.ALL, 5 )
		
		sbSizer61.Add( bSizer26, 1, wx.EXPAND, 5 )
		
		fgSizer2.Add( sbSizer61, 1, wx.EXPAND, 5 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"IN2 threshold" ), wx.VERTICAL )
		
		m_IN2_ThresholdChoices = [ u"RSSI", u"NXP ", u"H" ]
		self.m_IN2_Threshold = wx.RadioBox( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_IN2_ThresholdChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_IN2_Threshold.SetSelection( 0 )
		sbSizer9.Add( self.m_IN2_Threshold, 0, wx.ALL, 5 )
		
		self.m_IN2_threshold_value = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		sbSizer9.Add( self.m_IN2_threshold_value, 0, wx.ALL, 5 )
		
		bSizer261 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_IN2_NXP_H = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_IN2_NXP_H.Hide()
		
		bSizer261.Add( self.m_IN2_NXP_H, 0, wx.ALL, 5 )
		
		self.m_IN2_NXP_L = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_IN2_NXP_L.Hide()
		
		bSizer261.Add( self.m_IN2_NXP_L, 0, wx.ALL, 5 )
		
		sbSizer9.Add( bSizer261, 1, wx.EXPAND, 5 )
		
		fgSizer2.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"IN3 threshold" ), wx.VERTICAL )
		
		m_IN3_ThresholdChoices = [ u"RSSI", u"NXP ", u"H" ]
		self.m_IN3_Threshold = wx.RadioBox( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_IN3_ThresholdChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_IN3_Threshold.SetSelection( 0 )
		sbSizer10.Add( self.m_IN3_Threshold, 0, wx.ALL, 5 )
		
		self.m_IN3_threshold_value = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		sbSizer10.Add( self.m_IN3_threshold_value, 0, wx.ALL, 5 )
		
		bSizer262 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_IN3_NXP_H = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_IN3_NXP_H.Hide()
		
		bSizer262.Add( self.m_IN3_NXP_H, 0, wx.ALL, 5 )
		
		self.m_IN3_NXP_L = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_IN3_NXP_L.Hide()
		
		bSizer262.Add( self.m_IN3_NXP_L, 0, wx.ALL, 5 )
		
		sbSizer10.Add( bSizer262, 1, wx.EXPAND, 5 )
		
		fgSizer2.Add( sbSizer10, 1, wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"FL threshold" ), wx.VERTICAL )
		
		m_FL_ThresholdChoices = [ u"RSSI", u"NXP ", u"H" ]
		self.m_FL_Threshold = wx.RadioBox( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_FL_ThresholdChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_FL_Threshold.SetSelection( 1 )
		sbSizer11.Add( self.m_FL_Threshold, 0, wx.ALL, 5 )
		
		self.m_FL_threshold_value = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		sbSizer11.Add( self.m_FL_threshold_value, 0, wx.ALL, 5 )
		
		bSizer263 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_FL_NXP_H = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_FL_NXP_H.Hide()
		
		bSizer263.Add( self.m_FL_NXP_H, 0, wx.ALL, 5 )
		
		self.m_FL_NXP_L = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_FL_NXP_L.Hide()
		
		bSizer263.Add( self.m_FL_NXP_L, 0, wx.ALL, 5 )
		
		sbSizer11.Add( bSizer263, 1, wx.EXPAND, 5 )
		
		fgSizer2.Add( sbSizer11, 1, wx.EXPAND, 5 )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"FR threshold" ), wx.VERTICAL )
		
		m_FR_ThresholdChoices = [ u"RSSI", u"NXP ", u"H" ]
		self.m_FR_Threshold = wx.RadioBox( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_FR_ThresholdChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_FR_Threshold.SetSelection( 0 )
		sbSizer12.Add( self.m_FR_Threshold, 0, wx.ALL, 5 )
		
		self.m_FR_threshold_value = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		sbSizer12.Add( self.m_FR_threshold_value, 0, wx.ALL, 5 )
		
		bSizer264 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_FR_NXP_H = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_FR_NXP_H.Hide()
		
		bSizer264.Add( self.m_FR_NXP_H, 0, wx.ALL, 5 )
		
		self.m_FR_NXP_L = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_FR_NXP_L.Hide()
		
		bSizer264.Add( self.m_FR_NXP_L, 0, wx.ALL, 5 )
		
		sbSizer12.Add( bSizer264, 1, wx.EXPAND, 5 )
		
		fgSizer2.Add( sbSizer12, 1, wx.EXPAND, 5 )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow3, wx.ID_ANY, u"TR threshold" ), wx.VERTICAL )
		
		m_TR_ThresholdChoices = [ u"RSSI", u"NXP ", u"H" ]
		self.m_TR_Threshold = wx.RadioBox( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_TR_ThresholdChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_TR_Threshold.SetSelection( 0 )
		sbSizer13.Add( self.m_TR_Threshold, 0, wx.ALL, 5 )
		
		self.m_TR_threshold_value = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		sbSizer13.Add( self.m_TR_threshold_value, 0, wx.ALL, 5 )
		
		bSizer265 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_TR_NXP_H = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_TR_NXP_H.Hide()
		
		bSizer265.Add( self.m_TR_NXP_H, 0, wx.ALL, 5 )
		
		self.m_TR_NXP_L = wx.TextCtrl( self.m_scrolledWindow3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_TR_NXP_L.Hide()
		
		bSizer265.Add( self.m_TR_NXP_L, 0, wx.ALL, 5 )
		
		sbSizer13.Add( bSizer265, 1, wx.EXPAND, 5 )
		
		fgSizer2.Add( sbSizer13, 1, wx.EXPAND, 5 )
		
		sbSizer6.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_config = wx.Button( self.m_scrolledWindow3, wx.ID_ANY, u"打开配置", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.m_config, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_save_config = wx.Button( self.m_scrolledWindow3, wx.ID_ANY, u"配置保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.m_save_config, 0, wx.ALL, 5 )
		
		self.m_load_config = wx.Button( self.m_scrolledWindow3, wx.ID_ANY, u"配置使能", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer46.Add( self.m_load_config, 0, wx.ALL, 5 )
		
		sbSizer6.Add( bSizer46, 0, wx.EXPAND, 5 )
		
		bSizer38.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer3.Add( bSizer38, 0, wx.EXPAND, 5 )
		
		bSizer7.Add( sbSizer3, 0, wx.EXPAND, 5 )
		
		self.m_scrolledWindow3.SetSizer( bSizer7 )
		self.m_scrolledWindow3.Layout()
		self.m_panel10 = wx.Panel( self.m_content_split, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow2, wx.ID_ANY, u"结果显示" ), wx.VERTICAL )
		
		bSizer43 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_result = wx.Panel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		self.m_result.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )
		
		bSizer48 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer48.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_result_label = wx.StaticText( self.m_result, wx.ID_ANY, u"车内", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_result_label.Wrap( -1 )
		bSizer48.Add( self.m_result_label, 0, wx.ALL, 5 )
		
		
		bSizer48.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_result.SetSizer( bSizer48 )
		self.m_result.Layout()
		bSizer48.Fit( self.m_result )
		bSizer43.Add( self.m_result, 1, wx.EXPAND |wx.ALL, 5 )
		
		sbSizer7.Add( bSizer43, 0, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 6, 7, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText32 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"天线", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		fgSizer3.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"IN1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		fgSizer3.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"IN2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer3.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText43 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"IN3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		fgSizer3.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText44 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"FL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		fgSizer3.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText45 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"FR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		fgSizer3.Add( self.m_staticText45, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText46 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"TR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		fgSizer3.Add( self.m_staticText46, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText33 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"车内外", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		fgSizer3.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_IN1_RESULT = wx.BitmapButton( self.m_scrolledWindow2, wx.ID_ANY, wx.Bitmap( u"img/green.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer3.Add( self.m_IN1_RESULT, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_IN2_RESULT = wx.BitmapButton( self.m_scrolledWindow2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer3.Add( self.m_IN2_RESULT, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_IN3_RESULT = wx.BitmapButton( self.m_scrolledWindow2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer3.Add( self.m_IN3_RESULT, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_FL_RESULT = wx.BitmapButton( self.m_scrolledWindow2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer3.Add( self.m_FL_RESULT, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_FR_RESULT = wx.BitmapButton( self.m_scrolledWindow2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer3.Add( self.m_FR_RESULT, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_TR_RESULT = wx.BitmapButton( self.m_scrolledWindow2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		fgSizer3.Add( self.m_TR_RESULT, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText261 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"RSSI-Float", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText261.Wrap( -1 )
		fgSizer3.Add( self.m_staticText261, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_IN1_RSSI = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		fgSizer3.Add( self.m_IN1_RSSI, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_IN2_RSSI = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_IN2_RSSI, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_IN3_RSSI = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_IN3_RSSI, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_FL_RSSI = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_FL_RSSI, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_FR_RSSI = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_FR_RSSI, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_TR_RSSI = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_TR_RSSI, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText35 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"NXP-Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		fgSizer3.Add( self.m_staticText35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_IN1_NXP = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_IN1_NXP, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_IN2_NXP = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_IN2_NXP, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_IN3_NXP = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_IN3_NXP, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_FL_NXP = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_FL_NXP, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_FR_NXP = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_FR_NXP, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_TR_NXP = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_TR_NXP, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"H(nT) ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer3.Add( self.m_staticText36, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_IN1_H = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_IN1_H, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_IN2_H = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_IN2_H, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_IN3_H = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_IN3_H, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_FL_H = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_FL_H, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_FR_H = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_FR_H, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_TR_H = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_TR_H, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer7.Add( fgSizer3, 0, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer7.Add( bSizer34, 1, wx.EXPAND, 5 )
		
		self.m_scrolledWindow2.SetSizer( sbSizer7 )
		self.m_scrolledWindow2.Layout()
		sbSizer7.Fit( self.m_scrolledWindow2 )
		bSizer21.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel101 = wx.Panel( self.m_panel10, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.STATIC_BORDER|wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self.m_panel101, wx.ID_ANY, wx.Bitmap( u"img/naen3.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_bitmap3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer121 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel101, wx.ID_ANY, u"钥匙信息" ), wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText37 = wx.StaticText( self.m_panel101, wx.ID_ANY, u"UID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		fgSizer4.Add( self.m_staticText37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_key_uid = wx.TextCtrl( self.m_panel101, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_key_uid, 0, wx.ALL, 5 )
		
		self.m_key_battery = wx.StaticText( self.m_panel101, wx.ID_ANY, u"Battery", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_key_battery.Wrap( -1 )
		fgSizer4.Add( self.m_key_battery, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl48 = wx.TextCtrl( self.m_panel101, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_textCtrl48, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self.m_panel101, wx.ID_ANY, u"Fob Num", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		fgSizer4.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.m_fob_number = wx.TextCtrl( self.m_panel101, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_fob_number, 0, wx.ALL, 5 )
		
		sbSizer121.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		bSizer33.Add( sbSizer121, 1, wx.EXPAND, 5 )
		
		self.m_panel101.SetSizer( bSizer33 )
		self.m_panel101.Layout()
		bSizer33.Fit( self.m_panel101 )
		bSizer21.Add( self.m_panel101, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel10.SetSizer( bSizer21 )
		self.m_panel10.Layout()
		bSizer21.Fit( self.m_panel10 )
		self.m_content_split.SplitVertically( self.m_scrolledWindow3, self.m_panel10, 564 )
		m_top_panel_sizer.Add( self.m_content_split, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_top_panel.SetSizer( m_top_panel_sizer )
		self.m_top_panel.Layout()
		m_top_panel_sizer.Fit( self.m_top_panel )
		self.m_bottom_panel = wx.Panel( self.m_outer_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_info_list = wx.ListCtrl( self.m_bottom_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SUNKEN_BORDER )
		self.m_info_list.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.m_info_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bottom_panel.SetSizer( bSizer3 )
		self.m_bottom_panel.Layout()
		bSizer3.Fit( self.m_bottom_panel )
		self.m_outer_splitter.SplitHorizontally( self.m_top_panel, self.m_bottom_panel, 406 )
		mainsizer.Add( self.m_outer_splitter, 1, wx.EXPAND, 5 )
		
		self.m_main_panel.SetSizer( mainsizer )
		self.m_main_panel.Layout()
		mainsizer.Fit( self.m_main_panel )
		bSizer1.Add( self.m_main_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( wx.MB_DOCKABLE )
		self.m_menu_file = wx.Menu()
		self.m_menu_clear_log = wx.MenuItem( self.m_menu_file, MENU_ID_CLEAR_LOG, u"清除日志", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menu_clear_log )
		
		self.m_file_exit_menu = wx.MenuItem( self.m_menu_file, MENU_ID_EXIT, u"退出", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_file_exit_menu.SetBitmap( wx.Bitmap( u"img/exit.png", wx.BITMAP_TYPE_ANY ) )
		self.m_menu_file.AppendItem( self.m_file_exit_menu )
		
		self.m_menubar1.Append( self.m_menu_file, u"File" ) 
		
		self.m_option_menu = wx.Menu()
		self.m_option_setting = wx.MenuItem( self.m_option_menu, wx.ID_ANY, u"帮助", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_option_menu.AppendItem( self.m_option_setting )
		
		self.m_menubar1.Append( self.m_option_menu, u" Help" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_toolbar = self.CreateToolBar( wx.TB_DOCKABLE|wx.TB_FLAT|wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_toolbar.AddLabelTool( TOOL_ID_CONFIG, u"tool", wx.Bitmap( u"img/config.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"配置", u"配置" ) 
		self.m_toolbar.AddLabelTool( TOOL_ID_DEVICE_INIT, u"tool", wx.Bitmap( u"img/device_self_test.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"初始化设备，设备自检", u"初始化设备，设备自检" ) 
		self.m_toolbar.AddSeparator()
		self.m_toolbar.AddLabelTool( TOOL_ID_START_TRACE, u"tool", wx.Bitmap( u"img/start_monitoring.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"开始监听RF回应", u"开始监听RF回应" ) 
		self.m_toolbar.AddSeparator()
		self.m_toolbar.AddLabelTool( TOOL_ID_SAVE, u"tool", wx.Bitmap( u"img/document-save.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"保存记录表格内容到指定文件", u"保存记录表格内容到指定文件" ) 
		self.m_toolbar.AddLabelTool( TOOL_ID_CLEAR, u"tool", wx.Bitmap( u"img/recycle_bin.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"清楚记录表格内容", u"清楚记录表格内容" ) 
		self.m_toolbar.AddSeparator()
		self.m_toolbar.Realize()
		
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_lf_period_send.Bind( wx.EVT_BUTTON, self.OnTriggerOnTime )
		self.m_lf_once_send.Bind( wx.EVT_BUTTON, self.OnTriggerOnce )
		self.m_config.Bind( wx.EVT_BUTTON, self.OnOpenConfig )
		self.m_save_config.Bind( wx.EVT_BUTTON, self.OnSaveConfig )
		self.m_load_config.Bind( wx.EVT_BUTTON, self.OnConfigSet )
		self.Bind( wx.EVT_MENU, self.onMenuSelection, id = self.m_menu_clear_log.GetId() )
		self.Bind( wx.EVT_MENU, self.onMenuSelection, id = self.m_file_exit_menu.GetId() )
		self.Bind( wx.EVT_MENU, self.onMenuSelection, id = self.m_option_setting.GetId() )
		self.Bind( wx.EVT_TOOL, self.onToolClicked, id = TOOL_ID_CONFIG )
		self.Bind( wx.EVT_TOOL, self.onToolClicked, id = TOOL_ID_DEVICE_INIT )
		self.Bind( wx.EVT_TOOL, self.onToolClicked, id = TOOL_ID_START_TRACE )
		self.Bind( wx.EVT_TOOL, self.onToolClicked, id = TOOL_ID_SAVE )
		self.Bind( wx.EVT_TOOL, self.onToolClicked, id = TOOL_ID_CLEAR )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnTriggerOnTime( self, event ):
		event.Skip()
	
	def OnTriggerOnce( self, event ):
		event.Skip()
	
	def OnOpenConfig( self, event ):
		event.Skip()
	
	def OnSaveConfig( self, event ):
		event.Skip()
	
	def OnConfigSet( self, event ):
		event.Skip()
	
	def onMenuSelection( self, event ):
		event.Skip()
	
	
	
	def onToolClicked( self, event ):
		event.Skip()
	
	
	
	
	
	def m_outer_splitterOnIdle( self, event ):
		self.m_outer_splitter.SetSashPosition( 406 )
		self.m_outer_splitter.Unbind( wx.EVT_IDLE )
	
	def m_content_splitOnIdle( self, event ):
		self.m_content_split.SetSashPosition( 564 )
		self.m_content_split.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class SettingDiaglog
###########################################################################

class SettingDiaglog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"设置", pos = wx.DefaultPosition, size = wx.Size( 435,323 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auinotebook = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_RF_receiver_page = wx.Panel( self.m_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText5 = wx.StaticText( self.m_RF_receiver_page, wx.ID_ANY, u"串口号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		m_comport_listChoices = []
		self.m_comport_list = wx.Choice( self.m_RF_receiver_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_comport_listChoices, 0 )
		self.m_comport_list.SetSelection( 0 )
		fgSizer2.Add( self.m_comport_list, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_RF_receiver_page, wx.ID_ANY, u"波特率", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		m_baudrate_listChoices = []
		self.m_baudrate_list = wx.Choice( self.m_RF_receiver_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_baudrate_listChoices, 0 )
		self.m_baudrate_list.SetSelection( 0 )
		fgSizer2.Add( self.m_baudrate_list, 0, wx.ALL, 5 )
		
		self.m_RF_receiver_page.SetSizer( fgSizer2 )
		self.m_RF_receiver_page.Layout()
		fgSizer2.Fit( self.m_RF_receiver_page )
		self.m_auinotebook.AddPage( self.m_RF_receiver_page, u"通讯板卡设置", False, wx.NullBitmap )
		self.m_system_setting = wx.Panel( self.m_auinotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText14 = wx.StaticText( self.m_system_setting, wx.ID_ANY, u"保存路径(日志)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer20.Add( self.m_staticText14, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_logfile_dirpick = wx.DirPickerCtrl( self.m_system_setting, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer20.Add( self.m_logfile_dirpick, 1, wx.ALL, 5 )
		
		bSizer19.Add( bSizer20, 0, wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_save_rf_response = wx.CheckBox( self.m_system_setting, wx.ID_ANY, u"实时保存标定数据到日志中", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.m_save_rf_response, 0, wx.ALL, 5 )
		
		bSizer19.Add( bSizer23, 1, wx.EXPAND, 5 )
		
		self.m_system_setting.SetSizer( bSizer19 )
		self.m_system_setting.Layout()
		bSizer19.Fit( self.m_system_setting )
		self.m_auinotebook.AddPage( self.m_system_setting, u"系统设置", False, wx.NullBitmap )
		
		bSizer9.Add( self.m_auinotebook, 1, wx.EXPAND |wx.ALL, 0 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Apply = wx.Button( self, wx.ID_APPLY )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Apply )
		m_sdbSizer1.Realize();
		bSizer9.Add( m_sdbSizer1, 0, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnInitDialog )
		self.m_sdbSizer1Apply.Bind( wx.EVT_BUTTON, self.OnSaveButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnInitDialog( self, event ):
		event.Skip()
	
	def OnSaveButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class WFGenerator
###########################################################################

class WFGenerator ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"WaveFormGeneator", pos = wx.DefaultPosition, size = wx.Size( 659,251 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText24 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Premable(H,L...)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		self.m_staticText24.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer28.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_premable = wx.TextCtrl( self.m_panel13, wx.ID_ANY, u"1010101010101010", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_premable, 1, wx.ALL, 5 )
		
		bSizer27.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText25 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Sync(H,L...)      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		self.m_staticText25.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer29.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_sync = wx.TextCtrl( self.m_panel13, wx.ID_ANY, u"111000101100110010", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.m_sync, 1, wx.ALL, 5 )
		
		bSizer27.Add( bSizer29, 0, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText31 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"WakeUp ID        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		self.m_staticText31.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer34.Add( self.m_staticText31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_wakeupid = wx.TextCtrl( self.m_panel13, wx.ID_ANY, u"0x20,0x16,0x12,0xEF", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.m_wakeupid, 1, wx.ALL, 5 )
		
		bSizer27.Add( bSizer34, 1, wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText26 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Bytes(byte,.....)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		self.m_staticText26.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer30.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_data = wx.TextCtrl( self.m_panel13, wx.ID_ANY, u"0x44,0x00,0x00,0x00,0x00,0x00", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_data, 1, wx.ALL, 5 )
		
		bSizer27.Add( bSizer30, 0, wx.EXPAND, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText27 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Frequency(KHZ) ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		self.m_staticText27.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer31.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_frequency = wx.TextCtrl( self.m_panel13, wx.ID_ANY, u"7.8125", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_frequency, 0, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Tail Carrier Time(MS)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		self.m_staticText29.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer31.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_carrier_timer = wx.TextCtrl( self.m_panel13, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_carrier_timer, 1, wx.ALL, 5 )
		
		bSizer27.Add( bSizer31, 0, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText28 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"WAVEFORMType", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		self.m_staticText28.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer32.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_waveformtypeChoices = [ u"CALCULATE_INPUT_VOLTAGE", u"CALIBRATE" ]
		self.m_waveformtype = wx.Choice( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_waveformtypeChoices, 0 )
		self.m_waveformtype.SetSelection( 0 )
		bSizer32.Add( self.m_waveformtype, 0, wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"Manchester      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		self.m_staticText30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer32.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_manchester_typeChoices = [ u"HIGH->LOW(1)", u"LOW->HIGH(1)" ]
		self.m_manchester_type = wx.Choice( self.m_panel13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_manchester_typeChoices, 0 )
		self.m_manchester_type.SetSelection( 1 )
		bSizer32.Add( self.m_manchester_type, 0, wx.ALL, 5 )
		
		bSizer27.Add( bSizer32, 0, wx.EXPAND, 5 )
		
		self.m_panel13.SetSizer( bSizer27 )
		self.m_panel13.Layout()
		bSizer27.Fit( self.m_panel13 )
		bSizer25.Add( self.m_panel13, 0, wx.EXPAND |wx.ALL, 0 )
		
		m_sdbSizer3 = wx.StdDialogButtonSizer()
		self.m_sdbSizer3OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer3.AddButton( self.m_sdbSizer3OK )
		m_sdbSizer3.Realize();
		bSizer25.Add( m_sdbSizer3, 0, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer25 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_sdbSizer3OK.Bind( wx.EVT_BUTTON, self.OnOkClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnOkClick( self, event ):
		event.Skip()
	

