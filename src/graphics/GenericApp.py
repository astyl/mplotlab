# -*-coding:Utf-8 -*

from MainWin import MainWin
import wx

class GenericApp(wx.App):

    def __init__(self,*args,**kwargs):
        wx.App.__init__(self,*args,**kwargs)
        self.mainWin = MainWin()
        self.SetTopWindow(self.mainWin)
        self.mainWin.Show()
    
    def run(self):
        self.MainLoop()
    

        