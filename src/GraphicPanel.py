# -*-coding:Utf-8 -*

import wx
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as CanvasPanel
from matplotlib.figure import Figure

class GraphicPanel(wx.Panel):
    def __init__(self,*args,**kwargs):
        wx.Panel.__init__(self,*args,**kwargs)
        
        # CANVAS & FIGURE MATPLOTLIB
        self.__figure = Figure()
        self.__canvas = CanvasPanel(self, -1, self.__figure)

        # RESIZE
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.__canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(sizer)
        self.Fit()   
        self.Show()
        
    def OnPaint(self, event):
        self.__canvas.draw()
    
    def getCanvas(self):
        return self.__canvas
    
    def getFigure(self):
        return self.__figure
    
    def draw(self,*args,**kwargs):
        self.__canvas.draw()
    