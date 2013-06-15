

# uncomment the following to use wx rather than wxagg
#matplotlib.use('WX')
#from matplotlib.backends.backend_wx import FigureCanvasWx as FigureCanvas

# comment out the following to use wx rather than wxagg


import wx.lib.newevent
import os

import logging
import time

from setting import YamlConfig
(AppendLogItem, EVT_UPDATE_APPENDLOGITEM) = wx.lib.newevent.NewEvent()
ANTENNA_LIST = ['IN1','IN2','IN3','FL','FR','TR']
RSSI_VAL_TYPE = ['RSSI','NXP','H']
CURRENT_RANGE = range(50,1050,50)
#WAVEFORM FORMAT DEFINITION
SECTION = 'WAVEFORM_PARA'
KEY_FREQUENCY_KHZ='FREQUENCY_KHZ'
KEY_PREMABLE='PREMABLE'
KEY_SYNC='SYNC'
KEY_DATA='DATA'
KEY_TAIL_CARRIER_MS='TAIL_CARRIER_MS'
KEY_WF_TYPE = "KEY_WF_TYPE"

#logging type
LOG_TYPE_INFO = 1
LOG_TYPE_WARN = 2
LOG_TYPE_ERROR = 3
LOG_TYPE_MSG = 4


REMARK = "REMARK"
VPPOUTMV = "VPPOUTMV"
TRIGGER_PERIOD = "TRIGGER_PERIOD"
OUTPUT_LOAD_Z = "OUTPUT_LOAD"

WAVEFORM_CALCULATE_INPUT_VOLTAGE = "CALCULATE_INPUT_VOLTAGE"
WAVEFORM_CALIB       = "CALIBRATE"



# Implementing MainFame
wildcard = "yaml(*.yaml)|*.yaml|"     \
           "All files (*.*)|*.*"

wildcard_csv = "CalibrationData(*.csv)|*.csv|"     \
           "All files (*.*)|*.*"


class CalToolLog:
    def __init__(self):
        self.logbox = None
        YamlConfig().LoadConfig()
        path = YamlConfig().GetYaml()["SAVE_DIR"]
        if not os.path.exists(path):
            os.makedirs(path)
        logging.basicConfig(filename = os.path.join(path, 'log_%s.txt'%time.strftime("%Y_%m_%d_%H_%M_%S", time.gmtime())), level = logging.DEBUG, filemode = 'w', format = '%(asctime)s - %(levelname)s: %(message)s')  
         
    def SetTarget(self,logbox):
        self.logbox = logbox
        
    def LogInfo(self,content):
        info = "%s" % (content)
        evt = AppendLogItem(log_content = content,log_type = LOG_TYPE_INFO )
        wx.PostEvent(self.logbox, evt)
        logging.log(logging.INFO,info)
        #self.logbox.log(info,0)
    def LogError(self,content):
        info = "%s" % (content)
        evt = AppendLogItem(log_content = content,log_type = LOG_TYPE_ERROR )
        wx.PostEvent(self.logbox, evt)
        logging.log(logging.ERROR,info)
    def LogWarn(self,content):
        evt = AppendLogItem(log_content = content,log_type = LOG_TYPE_WARN )
        wx.PostEvent(self.logbox, evt)
        info = "%s" % (content)
        logging.log(logging.WARN,info)
    def LogMsg(self,content):
        evt = AppendLogItem(log_content = content,log_type = LOG_TYPE_MSG )
        wx.PostEvent(self.logbox, evt)
        info = "%s" % (content)
        logging.log(logging.INFO,info)
        #self.logbox.log(info,1)
        
gLogger = CalToolLog()