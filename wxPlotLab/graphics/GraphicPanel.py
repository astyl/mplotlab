# -*-coding:Utf-8 -*

import wx
import matplotlib
from wxPlotLab.graphics.GraphicCtlr import GraphicCtlr
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as CanvasPanel
from matplotlib.figure import Figure
from figureFactory import buildFigure

class GraphicPanel(wx.Panel):
    def __init__(self,*args,**kwargs):
        wx.Panel.__init__(self,*args,**kwargs)
        
        # CANVAS & FIGURE MATPLOTLIB
        self.__figure = Figure()
        self.__canvas = CanvasPanel(self, -1, self.__figure)

        # SLIDE (MODEL)
        self.__slide = None
        
        # GRAPHIC CONTROL
        self.__graphicCtrl = GraphicCtlr(self.GetParent(),self.__canvas)
        
        # RESIZE
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.__canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(sizer)
        self.Fit()   
        self.Show()

    def draw(self):
        self.__canvas.draw()
                
    def OnPaint(self, event):
        self.draw()
    
    def getCanvas(self):
        return self.__canvas
    
    def getFigure(self):
        return self.__figure
    
    def getGraphicCtrl(self):
        return self.__graphicCtrl
    
    def getSlide(self):
        return self.__slide
    
    def setSlide(self,slide):
        self.__slide = slide
    
    def build(self,*args,**kwargs):
        self.__figure.clear()
        if self.__slide is None:
            return
        
        buildFigure(self.__figure,self.__slide)


