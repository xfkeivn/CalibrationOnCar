from utilities import gLogger;
import visa;
import serialcommunication
from setting import YamlConfig;
import threading;
import utilities
from utilities import *
import serialcommunication
import crcmod
import time
START_MONITOR_ON_REQ=[0xB2,0x03,0x2,0x35,0x01,0x38]
START_MONITOR_OFF_REQ=[0xB2,0x03,0x2,0x35,0x00,0x37]
START_MONIOR_POSITIVE_RESP = [0xB2,0x03,0x82,0x35,0x00,0x37]

GAIN_TABLE_RANGE={0x8:"Range0",0x4:"Range1",0x0:"Range2",0x2:"Range3",0xE:"Limiter"}
GAIN_TABLE_MUL= {0x8:(2**-6),0x4:(2**-3),0x0:1,0x2:(2**3),0xE:(2**16)}
GAINPeak = {0x8:42,0x4:5.3,0x0:0.668,0x2:0.083,0xE:None}

BATTERY_TABLE=[1.9,1.99,2.08,2.17,2.26,2.35,2.44,2.53,2.63,2.71,2.80,2.89,2.98,3.07,3.16,3.25]

class MonitorThread(threading.Thread):
    def __init__(self,parent):
        threading.Thread.__init__(self)
        self.m_stop = False
        self.parent = parent;
        
    def run(self): 
        while not self.m_stop:
            self.job()
    def job(self):
        #Getting from the serialobj
        datas = self.parent.communicator.MonitorResponse()
        
        if len(datas):
            self.parent.NewResponse(datas)
            
           
    def stop(self):
        self.m_stop = True
        self.join(2000)
        
class RFReceiver():
    def __init__(self):
        self.communicator = serialcommunication.SerialCommunication()
        self.yaml = YamlConfig().GetYaml()
        self.m_monitor_thread = None;
        self.observers = []
        self.waveformtype=None;
    def SetResponseType(self,waveformtype):
        self.waveformtype = waveformtype;
    def RegisterObserver(self,observer):
        self.observers.append(observer)
    def Disconnect(self):
        self.communicator.CloseSerial()    
    def Connect(self):
        baudrate = self.yaml[YamlConfig.RF_CARD_BAUDRATE];
        comport = self.yaml[YamlConfig.RF_CARD_COM_PORT];
        if not self.communicator.OpenSerial(comport, baudrate):
            raise Exception("Connect to Com port %s failed"%comport);
    def FormatConfigFrame(self,config):
        frame = [0xB2,12,0x03,0x36]
        frame.append(config['DataAntennaIndex']+1)
        frame.append(config['DataAnatennaCurIndex']+1)
        for antenna in ANTENNA_LIST: 
            if not config['%s_Checked'%(antenna)]:
                frame.append(0)
            else:
                frame.append(config['%_Current_Index'%(antenna)])
        #reserved
        frame.append(0)
        frame.append(0)
        checksum = sum(frame[2:-1])% 0x100
        frame.append(checksum)
        return frame
    def Config(self,config):
        try:
            if not self.communicator.IsPortOk:
                gLogger.LogError("Configuration failed, the port is not opened, please init device first ..")
                return False
            responsedatas = self.communicator.RequestAndResponse(self.FormatConfigFrame(config))
            if len(responsedatas) == 8 and responsedatas[2] == 0x83 and responsedatas[4:7]==[0x41,0x43,0x4B]:
                gLogger.LogInfo("Configurate the LF succesfully  .. ")
            else:
                gLogger.LogError("Error:%s"%responsedatas)
        except Exception as err:
            gLogger.LogError(err)   
            return False    
                
        return True
    
    def SendAuth(self):
        frame = [0xB2,0x0F,0x01,0x36,0x03,0x8D,0XB5,0x0A,0x79,0x01,0xE4,0x4E,0xF2,0x5A,0xC0,0x51,0x09]
        actual_checksum = sum(frame[2:-1])% 0x100
        frame.append(actual_checksum)
        self.communicator.WriteBytes(frame)

    def FormatDataToFrame(self,datas):
        #Check the Serial data format
        if datas[0]!= 0xB2 or datas[2]!=0xC2 or datas[3]!=0x35:
            raise Exception("START KEYWORD ERROR, [0]%X, [2]%X,[3]%X"%(datas[0],datas[2],datas[3]))
        datalen = datas[1];
        if len(datas) != datalen + 3:
            raise Exception("The length of frame is %d, but the dlc is %d, not match .."%(len(datas),datalen))
        actual_checksum = sum(datas[2:-1])% 0x100
        if  actual_checksum != datas[-1]:
            raise Exception("The CheckSum of the frame not match, the actual is %X, but the expected is %X"%(actual_checksum,datas[-1]))
        validpart = datas[4:]
        #=======================================================================
        # crc8_func = crcmod.predefined.mkPredefinedCrcFun('crc-8');
        # crc_data=""
        # for i in validpart[:-1]:
        #    crc_data+=chr(i)
        # crc = crc8_func(crc_data)
        #      
        # if validpart[-1] != crc:
        #    raise Exception("The CRC of RF response data is invalid,actual value is %X, but expected is %X"%(validpart[-1],crc))
        #=======================================================================
        return validpart
    
    def RSSICalculate(self,m1,m2,exp):
        MaskTable = [0x80,0x40,0x20,0x10,0x08,0x04,0x02,0x01]*2
        if m1 > 0xFF or m2 >0xFF or exp > 0xFF:
            raise Exception("Value not valid, m1,m2,m3 should be < 0xff, but actual is %x, %x, %x")%(m1,m2,exp)
        sign = 0;
        if exp>=0x80:
            exp = exp - 0xff -1;
        if m2>=0x80:
            sign = 1;
        m2 = m2 & 0x7F;
        temp=0
        val = float(2**-1)
        for i in range (1,16):
            if i<=7:
                temp = m2;
            else:
                temp = m1;
            val+=((temp&MaskTable[i]) and 1)*2**(-1*(i+1))
        val=val*(2**exp);
        if sign == 1:
            val = 0x00-val;        
        return val;
  
    def FormatRFResponse(self,datas):
        response={}
        data1 = datas[0]
        if (data1 & 0x0F) != 0x3:
            raise Exception ("Function code is not 3h,but is %d"%(data1&0x0F))
        UID = data1&0xF0
        data2 = datas[1]
        batteryindex = data2 & 0xF0
        batteryvalue = BATTERY_TABLE[batteryindex]
        response['battery'] = batteryvalue
        response['fob_id'] = UID
        response['fob_number']=0
        response['LF1_RSSI'] = self.RSSICalculate(0,datas[8],datas[9])
        response['LF2_RSSI'] = self.RSSICalculate(0,datas[10],datas[11])
        response['LF3_RSSI'] = self.RSSICalculate(0,datas[12],datas[13])
        
        
        return response
    def NewResponse(self,datas):
        try:
            validpart = self.FormatDataToFrame(datas) 
            responseframe = self.FormatRFResponse(validpart)
            for observer in self.observers:
                observer.newResponse(responseframe)
        except Exception as err:
            gLogger.LogError(err)
    def EnableMonitor(self,enable = True):
        try:
            if not self.communicator.IsPortOk:
                gLogger.LogError("Enable/Disable Monitor RF failed, the port is not opened, please init device first ..")
                return False
            if enable:
                responsedatas = self.communicator.RequestAndResponse(START_MONITOR_ON_REQ)
                if len(responsedatas) == 6 and responsedatas[2] == 0x82:
                    gLogger.LogInfo("MONITOR RF ON  .. ")
                    self.m_monitor_thread = MonitorThread(self)
                    self.m_monitor_thread.start();
                    return True
                else:
                    gLogger.LogError("Start Monitor on  Error:%s"%responsedatas)
                    
            else:
                self.m_monitor_thread.isAlive() and self.m_monitor_thread.stop();
                self.m_monitor_thread = None;
                responsedatas = self.communicator.RequestAndResponse(START_MONITOR_OFF_REQ)
                if len(responsedatas) == 6 and responsedatas[2] == 0x82:
                    gLogger.LogInfo("Monitor RF OFF..")
                    return True
                else:
                    gLogger.LogError("Monitor off  Error:%s"%responsedatas)
        
        except Exception as err:
            gLogger.LogError(err)       
                
        return False
                           