# -*-coding:Utf-8 -*

from wx.py.shell import Shell
import __init__

class ShellPanel(Shell):
    
    def __init__(self,parent):
        #introText="""We could use ipython ?"""
        Shell.__init__(self,parent,introText="")
    
    def refreshLocals(self):
        self.interp.locals.update(__init__.__dict__)