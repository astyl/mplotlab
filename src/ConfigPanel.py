# -*-coding:Utf-8 -*

import wx
import wx.propgrid as wxpg
from ArtistProperties import artistParams
from __init__ import log

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
        self.__mainWin = parent
        self.__artistSel = None
                        
        # CFG
        self.but.Bind( wx.EVT_BUTTON, self.updateFigure )
        self.pg.SetExtraStyle(wxpg.PG_EX_HELP_AS_TOOLTIPS)
#         self.pg.RegisterEditor(TrivialPropertyEditor)
#         self.pg.RegisterEditor(SampleMultiButtonEditor)
#         self.pg.RegisterEditor(LargeImageEditor)
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
        if self.__artistSel is None:
            return
        
        values = self.pg.GetPropertyValues()
        for param in self.__params:
            name = param[0]
            setter = "set_%s"%name
            
            setterFn = getattr(self.__artistSel,setter)
            if name in values.keys():
                value = values[name]
                ## To be handled by custom property 
                if "color" in name:
                    r,g,b = value.Get()
                    value = r/255.,g/255.,b/255.
                ### 
                setterFn(value)
         
        self.__mainWin.draw()
        
    def updatePage(self,artist):
        if artist is None:
            self.txt.SetLabel("")
            return
    
        txtLabel = "%s"%artist
        self.txt.SetLabel(txtLabel)
        log.info(txtLabel)
            
        self.__artistSel = artist

        if self.pg.GetPageCount()>0:
            self.pg.RemovePage(0)
        self.pg.AddPage(txtLabel)        
        
        self.__params = []
        for artistClass,params in artistParams.items():
            if isinstance(artist,artistClass):
                self.__params.extend(params)
                
        for param in self.__params:
            name, propertyClass= param
            getter = "get_%s"%name
            
            getterFn = getattr(artist,getter)
            value=getterFn()
            ## To be handled by custom property 
            if "alpha" == name and value is None:
                value = 1.0
            
            if "color" in name:
                from matplotlib.colors import ColorConverter
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