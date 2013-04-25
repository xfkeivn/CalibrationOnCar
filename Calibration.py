'''
Created on 2012-10-20

@author: Administrator
'''
import CalibrateOnCarFrame;
import wx;
class App(wx.App):
    def OnInit(self):
        frame = CalibrateOnCarFrame.CalibrateOnCarFrame(None)
        self.SetTopWindow(frame)
        frame.Maximize()
        frame.Show()
        return True
app = App(0)
app.MainLoop()