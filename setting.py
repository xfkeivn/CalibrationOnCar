'''
Created on 2013-1-1

@author: Administrator
'''
import yaml
import utilities

class Singleton(type):
    def __init__(cls,name,bases,dict):
        super(Singleton,cls).__init__(name,bases,dict)
        cls.instance = None
    def __call__(cls,*args,**kwargs):
        if cls.instance == None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance

class YamlConfig:
    AFG_SAMPLE_RATE = 'AFG_SAMPLE_RATE'
    AWG_VIAS_NAME = 'AWG_VIAS_NAME'
    CARRIER_FREQ = 'CARRIER_FREQ'
    RF_CARD_BAUDRATE = 'RF_CARD_BAUDRATE'
    RF_CARD_COM_PORT = 'RF_CARD_COM_PORT'
    SAVE_DIR = 'SAVE_DIR'
    __metaclass__ = Singleton
    def GetYaml(self):
        
        if self.yamlconfig != None:
            return self.yamlconfig
        else:
            raise Exception("setting file has not been loaded yet!")
    def __init__(self,filename= "setting.yaml"):
        self.filename = filename
        self.yamlconig = None
    def LoadConfig(self):
        
        self.stream = file(self.filename,"r")
        self.yamlconfig =  yaml.load(self.stream)
        
    def SaveConfig(self):
     
        self.stream = file(self.filename, 'w')
        yaml.dump(self.yamlconfig,self.stream,default_flow_style=False)
       
            
if __name__=="__main__":
    YamlConfig().LoadConfig()
    print YamlConfig().GetYaml()['CARRIER_FREQ']
    
