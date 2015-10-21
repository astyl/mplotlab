# -*-coding:Utf-8 -*

import wx
import matplotlib
from matplotlib.lines import Line2D
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as CanvasPanel
from matplotlib.figure import Figure

class GraphicPanel(wx.Panel):
    def __init__(self,*args,**kwargs):
        wx.Panel.__init__(self,*args,**kwargs)
        
        # CANVAS & FIGURE MATPLOTLIB
        self.__figure = Figure()
        self.__canvas = CanvasPanel(self, -1, self.__figure)

        # SLIDE
        self.__slide = None
        
        # RESIZE
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.__canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(sizer)
        self.Fit()   
        self.Show()
        
    def OnPaint(self, event):
        self.drawSlide()
    
    def getCanvas(self):
        return self.__canvas
    
    def getFigure(self):
        return self.__figure
    
    def buildSlide(self,*args,**kwargs):
        if kwargs.has_key("slide"):
            self.__slide = kwargs.pop("slide")
        self.__figure.clear()
        
        ### TO BE REFACTORED WITH A GREAT FIGURE FACTORY 
        # Slide
        title = self.__slide.get_title()
        projections = self.__slide.get_projections()
        
        self.__figure.suptitle(title)
        self.__figure.abcModel = self.__slide
        
        # Projection
        for i,projection in enumerate(projections):
            collections = projection.get_collections()
            xlabel = projection.get_xlabel()
            ylabel = projection.get_ylabel()
            xlim = projection.get_xmin(),projection.get_xmax()
            ylim = projection.get_ymin(),projection.get_ymax()
            
            axes = self.__figure.add_subplot(len(projections),1,i+1)
            axes.set_xlabel(xlabel)
            axes.set_ylabel(ylabel)
            axes.set_xlim(xlim)
            axes.set_ylim(ylim)

            axes.abcModel = projection
            
            for collection in collections:
                # Collection
                X = collection.get_X().get_data()
                Y = collection.get_Y().get_data()
                pL = ["color","linestyle"]
                kw = { k: collection.getAttr(k) \
                                            for k in pL} 
                
                line = Line2D(X,Y,**kw)
                axes.add_line(line)
                
                line.abcModel = collection
                
                
        ### 
    def drawSlide(self):
        self.__canvas.ClearBackground()
        self.__canvas.draw()
    