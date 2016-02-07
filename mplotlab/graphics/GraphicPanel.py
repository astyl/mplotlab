# -*-coding:Utf-8 -*
import matplotlib
matplotlib.use('WXAgg')
import wx
from matplotlib.backends.backend_wxagg import \
                    FigureCanvasWxAgg as CanvasPanel
from matplotlib.figure import Figure
from GraphicCtlr import GraphicCtlr
from mplotlab.mpl_builders.mpl_figures import buildFigure

class GraphicPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        
        # CANVAS & FIGURE MATPLOTLIB
        self.__figure = Figure()
        self.__canvas = CanvasPanel(self, -1, self.__figure)

        # SLIDE (MODEL)
        self.__slide = None
        
        # GRAPHIC CONTROL
        self.__graphicCtrl = GraphicCtlr(self.__canvas)
        
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
        if not self.__slide is None:
            buildFigure(self.__figure,self.__slide)

    def control(self):
        self.__graphicCtrl.control()
