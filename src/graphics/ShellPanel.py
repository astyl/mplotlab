# -*-coding:Utf-8 -*

from wx.py.shell import Shell
import graphics

class ShellPanel(Shell):
    
    def __init__(self,parent):
        #introText="""We could use ipython ?"""
        Shell.__init__(self,parent,introText="")
    
    def refreshLocals(self):
        self.interp.locals.update(graphics.__dict__)