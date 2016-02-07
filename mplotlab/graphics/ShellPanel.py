# -*-coding:Utf-8 -*

from wx.py.shell import Shell
from mplotlab import App

class ShellPanel(Shell):
    
    def __init__(self,parent):
        #introText="""We could use ipython ?"""
        Shell.__init__(self,parent,introText="")

    def refreshLocals(self,**dlocals):
        dlocals["app"]=App()
        dlocals["win"]=App().GetTopWindow()
        self.interp.locals.update(dlocals)
