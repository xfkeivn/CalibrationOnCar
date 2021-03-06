# -*- coding: utf-8 -*- 
import wx
import MainFrame
import utilities
from utilities import gLogger
from utilities import *
import devices
import re
from  calibsettingdlg import AutoCalibSettingDlg
import os
import sys
import yaml
import threading
ANTENNA_LIST = ['IN1','IN2','IN3','FL','FR','TR']
RSSI_VAL_TYPE = ['RSSI','NXP','H']
CURRENT_RANGE = range(50,1050,50)
# Implementing MainFame
count = 0
(RecordRFResponseEvt, EVT_RECORD_RF_RESPONSE) = wx.lib.newevent.NewEvent()
class CalibrateOnCarFrame( MainFrame.MainFame ):
    def __init__( self, parent ):
        MainFrame.MainFame.__init__( self, parent )
        self.m_data_antenna.AppendItems([str(i) for i in ANTENNA_LIST])
        self.m_data_antenna.SetSelection(0)
        self.initLoglistctrl()
        self.monitorenable = False;
        self.current_config={}
        self.current_row_index = 0
        for antenna in ANTENNA_LIST:
            cur_value = getattr(self,"m_%s_Current_Value"%(antenna))
            threshold_radio = getattr(self,"m_%s_Threshold"%(antenna));
            threshold_radio.SetItemLabel(0,"RSSI-Float")
            threshold_radio.SetItemLabel(1,'NXP-Data')
            threshold_radio.SetItemLabel(2,"H(nT)")
            result = getattr(self,"m_%s_RESULT"%(antenna))
            result.SetBitmapLabel(wx.Bitmap(r"img/grey.png"))
            threshold_radio.Bind( wx.EVT_RADIOBOX, self.OnThresholdTypeRadio )
            threshold_radio.SetSelection(0)
            threshold_radio.SetName("m_%s_Threshold"%(antenna))
            if cur_value:
                cur_value.SetInitialSize((40,-1))
                cur_value.AppendItems([str(i) for i in CURRENT_RANGE])
                cur_value.SetInitialSize((70,-1))
                cur_value.SetSelection(11)         #初始化列表值
            for type in RSSI_VAL_TYPE:
                rssi_value = getattr(self,"m_%s_%s"%(antenna,type))
                rssi_value.SetInitialSize((70,-1))
            antenna_check = getattr(self,"m_%s_Check"%(antenna))
            #antenna_check.SetValue(1)     #set default antenna select
            antenna_check.Bind( wx.EVT_CHECKBOX, self.OnCheckAntenna )
        self.m_data_Current_value.AppendItems([str(i) for i in CURRENT_RANGE])
        self.m_data_Current_value.SetSelection(11)  #初始化列表值
       
        self.m_fob_number.SetValue('0')
        self.m_battery_value.SetValue('0')
        
        self.Fit()
        self.Bind(utilities.EVT_UPDATE_APPENDLOGITEM, self.log)
        self.rfmonitor = devices.RFReceiver()
        self.rfmonitor.RegisterObserver(self)
        self.startperiodictrigger = False
        self.timer = None
        self.init_monitor_table()
        gLogger.SetTarget(self)        
        self.SetAllResult(-1)
        self.Bind(EVT_RECORD_RF_RESPONSE, self.UpdateResult)
        self.m_scrolledWindow2.Layout()
        self.m_scrolledWindow2.FitInside()
        self.m_lock.Disable()
        self.m_unlock.Disable()
        self.m_trunk.Disable()
    def init_monitor_table(self):
        COLUMN_NAME=[u"Fob号",u"X坐标",u"Y坐标",u"Z坐标",u"IN1",u"IN2",u"IN3",u"FL",u"FR",u"TR"]
        for i,name in enumerate(COLUMN_NAME):
            self.m_monitor_result_table.SetColLabelValue(i,name);
            self.m_monitor_result_table.SetColSize(i,50);
        self.m_monitor_result_table.SetColLabelSize(20)
        self.m_monitor_result_table.SetRowLabelSize(60)
    def OnThresholdTypeRadio(self,event):
        name = event.GetEventObject().GetName()
        print name
        selection = event.GetEventObject().GetSelection()
        p = re.compile(r"m_(.*)_Threshold")
        type = p.match(name).group(1)
        self.updateThresholdSelction(type,selection)
      
    def InsertIntoTable(self,response):
        
        size = self.m_monitor_result_table.GetNumberRows()
        batteryvalue = str(response['battery'])
        fob_id= str(response['fob_id'])
        self.m_battery_value.SetValue(batteryvalue)
        fob_number = str(response['fob_number'])
        self.m_fob_number.SetValue(fob_number)
        lf1_rssi= response['LF1_RSSI']
        lf2_rssi= response['LF2_RSSI']
        lf3_rssi =  response['LF3_RSSI']
        lf_array = [(lf1_rssi),(lf2_rssi),(lf3_rssi)]
        lf_array_afater_format = ["%.4f"%(lfvalue) for lfvalue in lf_array]
        self.m_monitor_result_table.SetCellValue(self.current_row_index,0,fob_number)
        if not self.startperiodictrigger:
            self.m_monitor_result_table.SetCellValue(self.current_row_index,1,self.m_pos_x.GetValue())
            self.m_monitor_result_table.SetCellValue(self.current_row_index,2,self.m_pos_y.GetValue())
            self.m_monitor_result_table.SetCellValue(self.current_row_index,3,self.m_pos_z.GetValue())
        lf_count = 0
        offset = 4
        for i,antennatype in enumerate(ANTENNA_LIST):
            if self.current_config["%s_Checked"%(antennatype)]:
                if lf_count < len(lf_array):
                    self.m_monitor_result_table.SetCellValue(self.current_row_index,offset+i,lf_array_afater_format[lf_count])
                    lf_count+=1
        self.current_row_index+=1
        if self.current_row_index > 5:
            self.m_monitor_result_table.AppendRows(1)
            self.m_monitor_result_table.ScrollLines(1)    
            
    def updateThresholdSelction(self,type,selection):
        if selection == 1:
            getattr(self,"m_%s_threshold_value"%(type)).Hide()
            getattr(self,"m_%s_NXP_H"%(type)).Show()
            getattr(self,"m_%s_NXP_L"%(type)).Show()
        else:
            getattr(self,"m_%s_threshold_value"%(type)).Show()
            getattr(self,"m_%s_NXP_H"%(type)).Hide()
            getattr(self,"m_%s_NXP_L"%(type)).Hide()
        getattr(self,"m_%s_NXP_H"%(type)).GetSizer()    
        self.m_scrolledWindow3.Layout()
        #self.m_scrolledWindow3.Refresh()
        self.m_scrolledWindow3.FitInside()
        
        

            
        
    def initLoglistctrl(self):
        self.m_info_list.InsertColumn(0, "LEVEL",width = 100)
        self.m_info_list.InsertColumn(1, "MESSAGE", width = 1500)
    def OnCheckAntenna(self,event):
        antennatype = event.GetEventObject().GetLabel()
        enable = event.IsChecked()
        self.UpdateCheckStatus(antennatype, enable)
    def UpdateCheckStatus(self,antennatype,enable):
        
        cur_value = getattr(self,"m_%s_Current_Value"%(antennatype))
        threshold_type = getattr(self,"m_%s_Threshold"%(antennatype))
        threshold_value = getattr(self,"m_%s_threshold_value"%(antennatype))
        getattr(self,"m_%s_NXP_H"%(antennatype)).Enable(enable)
        getattr(self,"m_%s_NXP_L"%(antennatype)).Enable(enable)
        result = getattr(self,"m_%s_RESULT"%(antennatype))
        for type in RSSI_VAL_TYPE:
                rssi_value = getattr(self,"m_%s_%s"%(antennatype,type))
                rssi_value.Enable(enable)
        result.SetBitmapLabel(wx.Bitmap(r"img/grey.png"))
        result.Enable(enable)
        threshold_value.Enable(enable)
        threshold_type.Enable(enable)
        cur_value.Enable(enable)
        
    # Handlers for MainFame events.
    def OnTriggerLFSend( self, event ):
        # TODO: Implement OnTriggerLFSend
        pass
    

    def DoDeviceInit(self):
        try:
            self.rfmonitor.Disconnect()
            self.rfmonitor.Connect()
            gLogger.LogInfo("RF Receiver is connected ...")
            
        except Exception as err:
            gLogger.LogError("The Device Init failed, the resaon is %s"%err)   
    def onToolClicked( self, event ):
        # TODO: Implement onToolClicked
        eventid = event.GetId()
        if eventid == MainFrame.TOOL_ID_CONFIG:
            diaglog = AutoCalibSettingDlg(self)
            diaglog.ShowModal()
        if eventid == MainFrame.TOOL_ID_DEVICE_INIT:
            self.DoDeviceInit()
        if eventid == MainFrame.TOOL_ID_START_TRACE:
            self.MonitorRFResponse()
        if eventid == MainFrame.TOOL_ID_SAVE:
            self.SaveData()
        if eventid == MainFrame.TOOL_ID_CLEAR:
            self.ClearData()
    def SaveData(self):
        dlg = wx.FileDialog(
                        self, message="Save file as ...", defaultDir=os.getcwd(), 
            defaultFile="", wildcard=utilities.wildcard_csv, style=wx.SAVE
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            lines = []
            rowsize = 0
            colsize = 0
            rowsize = self.m_monitor_result_table.GetNumberRows()
            colsize = self.m_monitor_result_table.GetNumberCols()
            self.GridToLines(self.m_monitor_result_table,rowsize, colsize, lines)    
            f = open(path,'w')
            f.writelines(lines)
            f.close()
    def GridToLines(self,grid, rowsize, colsize, lines):
        head = ['FobNumber','X','Y','Z','IN1','IN2','IN3','FL','FR','TR']
        head = ",".join(head) + "\n"
        lines.append(head)
        for row in range(0, rowsize):
            line = grid.GetCellValue(row, 0)
            for col in range(1, colsize):
                value = grid.GetCellValue(row, col)
                value = value.replace(',', '')
                line = line + ',' + str(value)
            lines.append(line+"\n")

    def ClearData(self): 
        self.m_monitor_result_table.ClearGrid()
        if self.current_row_index > 5:
            self.m_monitor_result_table.DeleteRows(6,self.current_row_index-5)
        self.current_row_index = 0
    def log(self, evt):
        content = evt.log_content
        type = evt.log_type
        coloroflog = wx.DEFAULT;
        leveloflog = "INFO"
        if type == utilities.LOG_TYPE_WARN:
            coloroflog = wx.BLUE
            leveloflog = "WARN"
        elif type == utilities.LOG_TYPE_INFO:
            coloroflog = wx.BLACK;
            leveloflog = "INFO"
        elif type == utilities.LOG_TYPE_ERROR:
            coloroflog = wx.RED;
            leveloflog = "ERROR"
        elif type == utilities.LOG_TYPE_MSG:
            coloroflog = wx.BLACK;
            leveloflog = "MSG"
        index = self.m_info_list.InsertStringItem(sys.maxint,str(leveloflog))
        item = self.m_info_list.GetItem(index)
        item.SetTextColour(coloroflog)
        
        self.m_info_list.SetItem(item)
        self.m_info_list.SetStringItem(index, 1, str(content))
        self.m_info_list.ScrollLines(1)
    
    def FormatConfig(self):
        config = {}
        config['DataAntennaIndex'] = self.m_data_antenna.GetSelection()
        config['DataAnatennaCurIndex'] = self.m_data_Current_value.GetSelection()
        config['IN1_Checked'] = self.m_IN1_Check.IsChecked()
        config['IN2_Checked'] = self.m_IN2_Check.IsChecked()
        config['IN3_Checked'] = self.m_IN3_Check.IsChecked()
        config['FL_Checked'] = self.m_FL_Check.IsChecked()
        config['FR_Checked'] = self.m_FR_Check.IsChecked()
        config['TR_Checked'] = self.m_TR_Check.IsChecked()
        
        config['IN1_Current_Index'] = self.m_IN1_Current_Value.GetSelection()
        config['IN2_Current_Index'] = self.m_IN2_Current_Value.GetSelection()
        config['IN3_Current_Index'] = self.m_IN3_Current_Value.GetSelection()
        config['FL_Current_Index'] = self.m_FL_Current_Value.GetSelection()
        config['FR_Current_Index'] = self.m_FR_Current_Value.GetSelection()
        config['TR_Current_Index'] = self.m_TR_Current_Value.GetSelection()
        
        config['IN1_Threshold_Type_Index'] = self.m_IN1_Threshold.GetSelection();
        config['IN2_Threshold_Type_Index'] = self.m_IN2_Threshold.GetSelection();
        config['IN3_Threshold_Type_Index'] = self.m_IN3_Threshold.GetSelection();
        config['FL_Threshold_Type_Index'] = self.m_FL_Threshold.GetSelection();
        config['FR_Threshold_Type_Index'] = self.m_FR_Threshold.GetSelection();
        config['TR_Threshold_Type_Index'] = self.m_TR_Threshold.GetSelection();
        
        config['IN1_threshold_value'] = self.m_IN1_threshold_value.GetValue()
        config['IN2_threshold_value'] = self.m_IN2_threshold_value.GetValue()
        config['IN3_threshold_value'] = self.m_IN3_threshold_value.GetValue()
        config['FL_threshold_value'] = self.m_FL_threshold_value.GetValue()
        config['FR_threshold_value'] = self.m_FR_threshold_value.GetValue()
        config['TR_threshold_value'] = self.m_TR_threshold_value.GetValue()
        for type in ANTENNA_LIST:
            config['%s_Threshold_NXP_H'%(type)] = getattr(self,"m_%s_NXP_H"%(type)).GetValue()
            config['%s_Threshold_NXP_L'%(type)] = getattr(self,"m_%s_NXP_L"%(type)).GetValue()
        
        
      
        return config
        
        
    def InitConfig(self,config):   
        self.m_data_antenna.Select(config['DataAntennaIndex'])
        self.m_data_Current_value.Select(config['DataAnatennaCurIndex'])
        self.m_IN1_Check.SetValue(config['IN1_Checked'])
        self.m_IN2_Check.SetValue(config['IN2_Checked'])
        self.m_IN3_Check.SetValue(config['IN3_Checked'])
        self.m_FL_Check.SetValue(config['FL_Checked'])
        self.m_FR_Check.SetValue(config['FR_Checked'])
        self.m_TR_Check.SetValue(config['TR_Checked'])
        
        for type in ANTENNA_LIST:
            self.UpdateCheckStatus(type,config["%s_Checked"%(type)])
            self.updateThresholdSelction(type,config['%s_Threshold_Type_Index'%(type)])
            getattr(self,"m_%s_NXP_H"%(type)).SetValue(config['%s_Threshold_NXP_H'%(type)])
            getattr(self,"m_%s_NXP_L"%(type)).SetValue(config['%s_Threshold_NXP_L'%(type)])
        
        self.m_IN1_Current_Value.SetSelection( config['IN1_Current_Index'])
        self.m_IN2_Current_Value.SetSelection( config['IN2_Current_Index'])
        self.m_IN3_Current_Value.SetSelection( config['IN3_Current_Index'])
        self.m_FL_Current_Value.SetSelection( config['FL_Current_Index'])
        self.m_FR_Current_Value.SetSelection( config['FR_Current_Index'])
        self.m_TR_Current_Value.SetSelection( config['TR_Current_Index'])
        
        self.m_IN1_Threshold.SetSelection(config['IN1_Threshold_Type_Index']);
        self.m_IN2_Threshold.SetSelection(config['IN2_Threshold_Type_Index']);
        self.m_IN3_Threshold.SetSelection(config['IN3_Threshold_Type_Index']);
        self.m_FL_Threshold.SetSelection(config['FL_Threshold_Type_Index']);
        self.m_FR_Threshold.SetSelection(config['FR_Threshold_Type_Index']);
        self.m_TR_Threshold.SetSelection(config['TR_Threshold_Type_Index']);
        self.m_IN1_threshold_value.SetValue(config['IN1_threshold_value'] )
        self.m_IN2_threshold_value.SetValue(config['IN2_threshold_value'] )
        self.m_IN3_threshold_value.SetValue(config['IN3_threshold_value'] )
        
        self.m_FL_threshold_value.SetValue(config['FL_threshold_value'] )
        self.m_FR_threshold_value.SetValue(config['FR_threshold_value'] )
        self.m_TR_threshold_value.SetValue(config['TR_threshold_value'] )
 
    def OnOpenConfig( self, event ):
        
        dlg = wx.FileDialog(self, message="Choose a file", defaultDir=os.getcwd(), defaultFile="", wildcard=utilities.wildcard, 
            style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            try:
                self.stream = file(dlg.GetPath(),"r")
                yamlconfig =  yaml.load(self.stream)
                self.InitConfig(yamlconfig)
            except Exception as err:
                gLogger.LogError(err)
        self.SetAllResult(-1)
    def newResponse(self,newresponse):
        evt = RecordRFResponseEvt(data = newresponse)
        wx.PostEvent(self,evt)    
    
    
    def SetAntennaResult(self,antenna,actual_rssi,actual_rssi_nxp):
        antennaresult = getattr(self,"m_%s_RESULT"%(antenna))
        index = self.current_config['%s_Threshold_Type_Index'%(antenna)]
        rssivalue = 0.0;
        actual_rssi=float(actual_rssi)
        if index == 0:
           rssivalue = float(self.current_config['%s_threshold_value'%(antenna)])
        elif index == 1:
           m2 =int(self.current_config['%s_Threshold_NXP_H'%(antenna)])
           exp =int(self.current_config['%s_Threshold_NXP_L'%(antenna)])
           rssivalue = self.rfmonitor.RSSICalculate(0, m2, exp)
        elif index == 2:
           gLogger.LogWarn("NOT VALID NOW H(nt) setting for threshold, the RSSI is default to 0")
        getattr(self,"m_%s_RSSI"%(antenna)).SetValue("%.4f"%(actual_rssi))
        getattr(self,"m_%s_NXP"%(antenna)).SetValue("%s:%s"%(str(actual_rssi_nxp[0]),str(actual_rssi_nxp[1]))) 
        result = (rssivalue < actual_rssi);           
        if result:
             antennaresult.SetBitmapLabel(wx.Bitmap("img/green.png"))
        else:
             antennaresult.SetBitmapLabel(wx.Bitmap("img/red.png"))
        return result
    def OnClose(self,event):
        if self.timer:
            self.timer.cancel()

        self.rfmonitor.EnableMonitor(False)
        self.rfmonitor.Disconnect()
        event.Skip()
    def OnThreasholdEnable(self,event):
        config = self.FormatConfig()
        self.current_config = config
        gLogger.LogInfo("Configurate the RSSI Threshold succesfully  .. ")
        
    def onMenuSelection(self,event):
        eventid = event.GetId()
        if eventid == MainFrame.MENU_ID_EXIT:
            if self.timer:
                self.timer.cancel()
            wx.Exit()
        if eventid == MainFrame.MENU_ID_CLEAR_LOG:
            self.OnClearLog()
    def OnClearLog(self):
        self.m_info_list.DeleteAllItems()           
    def SetAllResult(self,result):
        if result == 1:
            self.m_result_label.SetLabel(u"车内");
            self.m_result.SetBackgroundColour( wx.GREEN)
        elif result == 0:
            self.m_result_label.SetLabel(u"车外")
            self.m_result.SetBackgroundColour(wx.RED)
        else:
            self.m_result_label.SetLabel(u"未检测")
            self.m_result.SetBackgroundColour(wx.WHITE)
        self.m_result.Refresh()
    def OnTriggerOnce(self,event):
        try:
            #self.SetAllResult(False)
            #self.SetAntennaResult('IN2',True)
            self.rfmonitor.SendAuth()
            pass
        except Exception as err:
            gLogger.LogError(err)
            
    def StartTriggerTimer(self):
        #self.rfmonitor.SendAuth()
       
        #COLUMN_NAME=[u"Fob号",u"X坐标",u"Y坐标",u"Z坐标",u"IN1",u"IN2",u"IN3",u"FL",u"FR",u"TR"]
        #THIS PART IS FOR TEST, JUST REMOVE IT 
        self.rfmonitor.SendAuth()
        
        if  self.startperiodictrigger:
            self.timer = threading.Timer(int(self.m_trigger_period.GetValue()),self.StartTriggerTimer)
            self.timer.start()
        
    def OnTriggerOnTime(self,event):
        try:
            if self.startperiodictrigger == False:
                self.m_lf_period_send.SetLabel(u"停止周期触发")
                self.m_lf_once_send.Disable()
                self.startperiodictrigger = True
                self.StartTriggerTimer()
            else:
                self.startperiodictrigger =False 
                self.timer.cancel()
                self.m_lf_period_send.SetLabel(u"开始周期触发")
                self.m_lf_once_send.Enable()

        except Exception as err:
            gLogger.LogError(err);
    def UpdateResult(self,event): 
        datas = event.data
        try:
            if datas['RESPONSE_TYPE'] == 'RSSI':
                if self.current_config == {}:
                    gLogger.LogError(u"配置未使能")
                else:
                    self.UpdateResultIndicator(datas)
                    self.InsertIntoTable(datas)
            if datas['RESPONSE_TYPE'] == 'RKESHORT':
                self.UpdateShortRKE(datas)
            if datas['RESPONSE_TYPE'] == 'RKELONG':
                self.UpdateLongRKE(datas)
                
        except Exception as err:
            gLogger.LogError(err)
    def UpdateRKEButton(self,cid):
        if cid == 0x01:
            self.m_lock.Enable()
        elif cid == 0x02:
            self.m_unlock.Enable()
        elif cid == 0x4:
            self.m_trunk.Enable()
        threading.Timer(0.04,self.OnRkeTimeout).start()
    def OnRkeTimeout(self):
        self.m_lock.Disable()
        self.m_unlock.Disable()
        self.m_trunk.Disable()
    def UpdateShortRKE(self,response):
        self.m_rke_ide.SetValue(str(response['IDE']))
        self.m_battery_value.SetValue(str(response['battery']))
        self.m_fob_number.SetValue(str(response['fob_number']))
        self.UpdateRKEButton(response['BUTTON'])
    def UpdateLongRKE(self,response):
        self.m_rke_ide.SetValue(str(response['IDE']))
        self.m_fob_number.SetValue(str(response['fob_number']))
        self.m_battery_value.SetValue(str(response['battery']))
        self.m_SI_value.SetValue(str(response['SI']))
        self.UpdateRKEButton(response['BUTTON'])
    def UpdateResultIndicator(self,response):
        lf1_rssi= response['LF1_RSSI']
        lf2_rssi= response['LF2_RSSI']
        lf3_rssi= response['LF3_RSSI']
        lf1_m=response['LF1_M'] 
        lf1_exp = response['LF1_EXP'] 
        lf2_m=response['LF2_M'] 
        lf2_exp=response['LF2_EXP'] 
        lf3_m=response['LF3_M'] 
        lf3_exp=response['LF3_EXP'] 
        lf_array = [str(lf1_rssi),str(lf2_rssi),str(lf3_rssi)]
        lf_nxp_array=[(lf1_m,lf1_exp),(lf2_m,lf2_exp),(lf3_m,lf3_exp)]
        lf_count = 0
        final_result = False
        for i,antennatype in enumerate(ANTENNA_LIST):
            if self.current_config["%s_Checked"%(antennatype)]:
                if lf_count < len(lf_array):
                    antennaresult = self.SetAntennaResult(ANTENNA_LIST[i],lf_array[lf_count],lf_nxp_array[lf_count])
                    if antennaresult:
                        final_result = True
                    lf_count+=1
        self.SetAllResult(final_result)
    def OnSaveConfig( self, event ):
        dlg = wx.FileDialog(self,message="Choose a directory",defaultDir=os.getcwd(),style = wx.FD_SAVE,wildcard=utilities.wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            dirpath = dlg.GetPath()
            try:
                 self.stream = file(dlg.GetPath(),"w")
                 yaml.dump(self.FormatConfig(),self.stream,default_flow_style=False)
            except Exception as err:
                gLogger.LogError(err)
    def MonitorRFResponse(self):
        success = self.rfmonitor.EnableMonitor(not self.monitorenable)
        if success:
            self.monitorenable = not self.monitorenable;
            if not self.monitorenable:
                self.m_toolbar.SetToolNormalBitmap(MainFrame.TOOL_ID_START_TRACE,wx.Bitmap( r"img/start_monitoring.png", wx.BITMAP_TYPE_ANY ))
            else:
                self.m_toolbar.SetToolNormalBitmap(MainFrame.TOOL_ID_START_TRACE,wx.Bitmap( r"img/Stop.png", wx.BITMAP_TYPE_ANY ))
       
    
    def OnConfigSet( self, event ):
        config = self.FormatConfig()
        self.rfmonitor.Config(config)
        self.current_config = config