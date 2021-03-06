"""Subclass of SettingDiaglog, which is generated by wxFormBuilder."""

import wx
import MainFrame
from setting import YamlConfig
from utilities import gLogger
import time
# Implementing SettingDiaglog
class AutoCalibSettingDlg( MainFrame.SettingDiaglog ):
	def __init__( self, parent ):
		MainFrame.SettingDiaglog.__init__( self, parent )
		self.m_comport_list.AppendItems(["COM%d"%(com) for com in range(100)])
		self.m_baudrate_list.AppendItems(['9600','38400','115200'])
		self.yaml = YamlConfig().GetYaml()
	def OnSaveButtonClick(self,event):
		self.yaml['RF_CARD_BAUDRATE'] = self.m_baudrate_list.GetItems()[self.m_baudrate_list.GetSelection()]
		self.yaml['RF_CARD_COM_PORT'] = self.m_comport_list.GetItems()[self.m_comport_list.GetSelection()]
		self.yaml['SAVE_DIR'] = self.m_logfile_dirpick.GetTextCtrlValue()
		YamlConfig().SaveConfig()
	def OnInitDialog(self,event):
		self.m_auinotebook.SetSelection(0)
		try:
			baudrate = self.yaml['RF_CARD_BAUDRATE']
			comport = self.yaml['RF_CARD_COM_PORT']
			savedir = self.yaml['SAVE_DIR']
			self.m_logfile_dirpick.GetTextCtrl().SetValue(savedir)
			for index, itemstr in enumerate(self.m_baudrate_list.GetItems()):
				if itemstr == baudrate:
					self.m_baudrate_list.SetSelection(index)
					break;
			for index, itemstr in enumerate(self.m_comport_list.GetItems()):
				if itemstr == comport:
					self.m_comport_list.SetSelection(index)
					break;
		except Exception as err:
			gLogger.LogError(err)
		
		