# -*-coding:Utf-8 -*

from GraphicPanel import GraphicPanel
from ConfigPanel import ConfigPanel
from ShellPanel import ShellPanel
from TreePanel import TreePanel

import wx.aui

# menu
ID_CreatePerspective = wx.NewId()
ID_FirstPerspective = ID_CreatePerspective+1000
ID_About = wx.NewId()

class MainWin(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 
                          title="wxPlotLab", 
                          size=(1200,675), 
                          style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER|wx.CLIP_CHILDREN)
        self.__graphicPanel = GraphicPanel(self)
        # panels
        
        self.__treePanel= TreePanel(self,self.getFigure())
        self.__configPanel= ConfigPanel(self)
        self.__shellPanel = ShellPanel(self)   
        # tell FrameManager to manage this frame        
        self._mgr = wx.aui.AuiManager()
        self._mgr.SetManagedWindow(self)
        
        self._perspectives = []
        self.n = 0
        self.x = 0
        
        # create menu
        mb = wx.MenuBar()

        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, "Exit")

        self._perspectives_menu = wx.Menu()
        self._perspectives_menu.Append(ID_CreatePerspective, "Create Perspective")
        self._perspectives_menu.AppendSeparator()
        self._perspectives_menu.Append(ID_FirstPerspective+0, "Default Startup")

        help_menu = wx.Menu()
        help_menu.Append(ID_About, "About...")
        
        mb.Append(file_menu, "File")
        mb.Append(self._perspectives_menu, "Perspectives")
        mb.Append(help_menu, "Help")
        
        self.SetMenuBar(mb)

        self.statusbar = self.CreateStatusBar(2, wx.ST_SIZEGRIP)
        self.statusbar.SetStatusWidths([-2, -3])
        self.statusbar.SetStatusText("Ready", 0)
        self.statusbar.SetStatusText("Welcome To wxPlotLab!", 1)

        # add a bunch of panes
        self._mgr.AddPane(self.__configPanel, wx.aui.AuiPaneInfo().
                          Name("configPanel").Caption("configPanelC").
                          Left().Layer(1).Position(2).CloseButton(True).MaximizeButton(True))
                      
        self._mgr.AddPane(self.__shellPanel, wx.aui.AuiPaneInfo().
                          Name("shellPanel").Caption("shellPanelC").
                          Bottom().Layer(1).Position(1).CloseButton(True).MaximizeButton(True))
    
        self._mgr.AddPane(self.__treePanel, wx.aui.AuiPaneInfo().
                      Caption("treePanel").Caption("treePanelC").
                          Left().Layer(1).Position(1).CloseButton(True).MaximizeButton(True))

        # create some center panes
        self._mgr.AddPane(self.__graphicPanel, wx.aui.AuiPaneInfo().
                          Name("html_content").Caption("graphicPanelC").
                          CenterPane().Dockable(False).CloseButton(True).MaximizeButton(True))
                                

        # make some default perspectives
        perspective_default = self._mgr.SavePerspective()
        self._perspectives.append(perspective_default)

        # "commit" all changes made to FrameManager   
        self._mgr.Update()

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        
        # menuBar
        self.Bind(wx.EVT_MENU, self.OnCreatePerspective, id=ID_CreatePerspective)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=ID_About)
        self.Bind(wx.EVT_MENU_RANGE, self.OnRestorePerspective, id=ID_FirstPerspective,
                  id2=ID_FirstPerspective+1000)
    
    
    def getCanvas(self):
        return self.__graphicPanel.getCanvas()
    
    def getFigure(self):
        return self.__graphicPanel.getFigure()

    def build(self,*a,**k):
        self.__graphicPanel.build(*a,**k)
        self.onBuild()
    
    def onBuild(self):
        self.__treePanel.updateTree()
        dlocals = {
            "app": wx.GetApp(),
            "win": self,
            "slide": self.getCurrentSlide(),
            "figure": self.getFigure(),
            "canvas": self.getCanvas(),            
        }
        self.__shellPanel.refreshLocals(dlocals)
        self.updatePageConfig()
    
    def getCurrentSlide(self):
        return self.__graphicPanel.getSlide()

    def setSlide(self,slide):
        self.__graphicPanel.setSlide(slide)

    def draw(self,*a,**k):
        self.__graphicPanel.draw(*a,**k)
        
    def updatePageConfig(self):
        self.__configPanel.updatePage(self.__treePanel.getModelSel())
        
    def getGraphicPanel(self):
        return self.__graphicPanel
    
    def getGraphicCtrl(self):
        return self.__graphicPanel.getGraphicCtrl()

    def OnClose(self, event):
        self._mgr.UnInit()
        del self._mgr
        self.Destroy()

    def OnExit(self, event):
        self.Close()

    def OnAbout(self, event):
        msg = u""" 
The MIT License (MIT)
Copyright (c) 2015 

wxPlotLab by André ASTYL
andreastyl@gmail.com
"""
        dlg = wx.MessageDialog(self, msg, "About wxPlotLab",
                               wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()        


    def OnEraseBackground(self, event):
        event.Skip()

    def OnSize(self, event):
        event.Skip()

    def OnCreatePerspective(self, event):
        dlg = wx.TextEntryDialog(self, "Enter a name for the new perspective:", "AUI Test")
        
        dlg.SetValue(("Perspective %d")%(len(self._perspectives)+1))
        if dlg.ShowModal() != wx.ID_OK:
            return
        
        if len(self._perspectives) == 0:
            self._perspectives_menu.AppendSeparator()
        
        self._perspectives_menu.Append(ID_FirstPerspective + len(self._perspectives), dlg.GetValue())
        self._perspectives.append(self._mgr.SavePerspective())

    def OnRestorePerspective(self, event):
        self._mgr.LoadPerspective(self._perspectives[event.GetId() - ID_FirstPerspective])

    def GetStartPosition(self):
        self.x = self.x + 20
        x = self.x
        pt = self.ClientToScreen(wx.Point(0, 0))
        return wx.Point(pt.x + x, pt.y + x)
