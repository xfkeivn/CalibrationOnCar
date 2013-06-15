'''
Created on 2012-10-20

@author: Administrator
'''
import serial;
import wx;
import time;
import threading;
import utilities
from utilities import gLogger;
    
class SerialCommunication:
    def __init__(self):
        self.serialobj = serial.Serial();
        self.IsPortOk = False
    def OpenSerial(self,port,badurate=38400,timeout = 2):
        try:
            self.serialobj.port = port;
            self.serialobj.baudrate = badurate;
            self.serialobj.timeout = timeout # 6 secnods timeout
            self.serialobj.open()
        
        except serial.SerialException as err :
            self.IsPortOk = False
            gLogger.LogError(err)
        except Exception:
            self.IsPortOk = False
            gLogger.LogError(err)
        else:
            self.IsPortOk = True
            return True
        return False
    def CloseSerial(self):
        self.serialobj.close()
        self.IsPortOk = False
    def ReadBytes(self,size):
        return self.serialobj.read(size)
    
    def ReadAllWaiting(self):
        
        return (self.serialobj.read(self.serialobj.inWaiting()))
        
    
    def WriteBytes(self,data):
        datastring = ""
        for b in data:
            datastring+=chr(b)   
        return self.serialobj.write(datastring)
    def ReadOneFrameString(self):
        start_of_frame = self.serialobj.read(1)
        remainder = ""
        if start_of_frame:
            time.sleep(0.03)
            remainder = self.ReadAllWaiting();
        return start_of_frame + remainder;
    
    def MonitorResponse(self):
        responsedatas = self.ReadOneFrameString()
        recvdatas = []
        if len(responsedatas)!=0: 
            recvdatas = [ord(i) for i in responsedatas]
            data_str = self.FormatSerialData(recvdatas)
            gLogger.LogInfo("RX %s"%data_str)
            
        return recvdatas
    def RequestAndResponse(self,request_datas):
        responsedatas=[]
        try:
            #clear the buffer
            self.ReadAllWaiting()
            gLogger.LogInfo("TX %s"%(self.FormatSerialData(request_datas)))
            #request 
            self.WriteBytes(request_datas)
            responsedatas = self.ReadOneFrameString()
            responsedatas_num = [ord(i) for i in responsedatas]
            if len(responsedatas_num)!=0: 
                recvdatas = self.FormatSerialData(responsedatas_num)
                gLogger.LogInfo("RX %s"%recvdatas)
            else:
                gLogger.LogInfo("RX %s"%"[]")
        except Exception as err:
            raise err
            
        return responsedatas_num
            
    
 
    def StringToDatBytes(self,datastr):
        return [ord(i) for i in datastr]
    def FormatSerialData(self,datas):
        #return datas
        hexstring =  [(hex(i)).upper() for i in datas]
        return hexstring
        
    

    
#===============================================================================
# def Test():
#   sc = SerialCommunication();
#   sc.OpenSerial('COM8', 115200)
#   sc.StartTestPresent(3)
#   while(True):
#       #print sc.ReadAllWaiting()
#       print sc.ReadBytes(10)
# Test()
#===============================================================================
