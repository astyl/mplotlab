# -*-coding:Utf-8 -*

import wx
import wx.propgrid as wxpg
from mplotlab.graphics import propertyMap
from mplotlab.utils.Logger import log
from mplotlab import App
from mplotlab.utils.abctypes import COLOR
from matplotlib.colors import ColorConverter,rgb2hex

class ConfigPanel( wx.Panel ):
    def __init__( self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        
        # Controls
        self.txt = wx.StaticText(self,-1,"")
        self.panel = wx.Panel(self,-1)
        self.pg = wxpg.PropertyGridManager(self.panel,
                        style=wxpg.PG_SPLITTER_AUTO_CENTER |
                              wxpg.PG_AUTO_SORT )
        self.but = wx.Button(self.panel,-1,"show")
        
        # DATA
        self.__modelSel = None
                        
        # CFG
        self.but.Bind( wx.EVT_BUTTON, self.updateFigure )
        self.pg.SetExtraStyle(wxpg.PG_EX_HELP_AS_TOOLTIPS)
        self.setProperties()

    def setProperties(self):
        topsizer = wx.BoxSizer(wx.VERTICAL)
        topsizer.Add(self.txt, 0, wx.EXPAND)
        topsizer.Add(self.pg, 1, wx.EXPAND)
        topsizer.Add(self.but,0,wx.EXPAND)

        self.panel.SetSizer(topsizer)
        topsizer.SetSizeHints(self.panel)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        sizer.Fit(self)
        self.Layout()
        
    def updateFigure(self,event):
        if self.__modelSel is None:
            event.Skip()  
            return
        
        for name,value in self.pg.GetPropertyValues().items():
            ## To be handled by custom property
            if name=='color':
#             if COLOR == self.__modelSel.getProperties()[name]:
                r,g,b = value.Get()
                value = r/255.,g/255.,b/255.
                value = rgb2hex(value)            
            ### 
            if isinstance(value,unicode):
                value = value.encode()
                
            getattr(self.__modelSel,"set_"+name)(value)

        App().mainWin.showSlideSel()
        
    def updatePage(self,modelSel):
        if modelSel is None:
            self.txt.SetLabel("")
            return
    
        txtLabel = "%s (%s)"% (
                    modelSel.get_name(),
                    modelSel.__class__.__name__)
        self.txt.SetLabel(txtLabel)
            
        self.__modelSel = modelSel

        if self.pg.GetPageCount()>0:
            self.pg.RemovePage(0)
        self.pg.AddPage(txtLabel)        
        
        #modelSel        
        for name, propertyKey,_,desc in modelSel.parametersInfo:
            propertyClass = propertyMap[propertyKey]            
            value=getattr(modelSel,"get_"+name)()
            
            ## To be handled by custom property 
            if "alpha" == name and value is None:
                value = 1.0
            
            if "color" == propertyKey:
                c = ColorConverter()

                if isinstance(value,(unicode,str)):
                    if "none" ==  value.lower():
                        value = None
                    else:
                        value = c.to_rgb(value)
                
                if not value is None:
                    try:
                        r,g,b = value
                    except:
                        r,g,b,_ = value
                    value = wx.Colour(r*255,g*255,b*255)
                
            ## 
            log.info("%s:%s"%(name,value))
            if not value is None:
                self.pg.Append(propertyClass(name,value=value))
            else:
                self.pg.Append(propertyClass(name))
