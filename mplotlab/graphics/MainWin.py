# -*-coding:Utf-8 -*
from GraphicBook import GraphicBook
from ConfigPanel import ConfigPanel
from ShellPanel import ShellPanel
from TreePanel import TreePanel
from mplotlab.models.Container import Container
import wx.aui,os

# menu
ID_SaveXml = wx.NewId()
ID_LoadXml = wx.NewId()
ID_CreatePerspective = wx.NewId()
ID_FirstPerspective = ID_CreatePerspective+1000
ID_About = wx.NewId()

class MainWin(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 
                          title="mplotlab", 
                          size=(1200,675), 
                          style=wx.DEFAULT_FRAME_STYLE|wx.SUNKEN_BORDER|wx.CLIP_CHILDREN)
        # model container
        self.__container = Container()
        # panels
        self.__graphicBook = GraphicBook(self)
        self.__configPanel= ConfigPanel(self)
        self.__treePanel= TreePanel(self,self.__configPanel)
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
        file_menu.Append(ID_LoadXml, "Load Xml")
        file_menu.Append(ID_SaveXml, "Save Xml")
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
        self.statusbar.SetStatusText("Welcome To mplotlab!", 1)

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
        self._mgr.AddPane(self.__graphicBook, wx.aui.AuiPaneInfo().CenterPane().
                          Name("graphicBook").Caption("graphicBookC").Center().Floatable(True)
                          .CloseButton(False).MaximizeButton(True))

        # make some default perspectives
        perspective_default = self._mgr.SavePerspective()
        self._perspectives.append(perspective_default)

        # "commit" all changes made to FrameManager   
        self._mgr.Update()

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        
        # menuBar
        self.Bind(wx.EVT_MENU, self.OnLoadXml, id=ID_LoadXml)
        self.Bind(wx.EVT_MENU, self.OnSaveXml, id=ID_SaveXml)
        self.Bind(wx.EVT_MENU, self.OnCreatePerspective, id=ID_CreatePerspective)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=ID_About)
        self.Bind(wx.EVT_MENU_RANGE, self.OnRestorePerspective, id=ID_FirstPerspective,
                  id2=ID_FirstPerspective+1000)

    def getContainer(self):
        return self.__container
 
    
    def showSlideSel(self):
        slide = self.__treePanel.getSlideSelected()
        if not slide is None:
            self.showSlide(slide)
        
    def showSlide(self,slide):
        # update Panels
        self.__treePanel.updateTree() 
        self.__graphicBook.updateBook()
        self.__shellPanel.refreshLocals(slide=slide)
        gp = self.__graphicBook.createGraphicPanel(slide)
        # show interactive figure associated 
        gp.build()    # matplotlib figure creation
        gp.draw()     # matplotlib figure draw
        gp.control()  # graphicControl enabling

    ###########################    
    ###########################    
    ###########################    
    
    def OnLoadXml(self,event):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard="All files (*.*)|*.*",
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            self.__container.flush()
            self.__container.fromxml(dlg.GetPath())
            self.showSlide(self.__container.getSlides()[0])

    def OnSaveXml(self,event):
        dlg = wx.FileDialog(
            self, message="Save file as ...", defaultDir=os.getcwd(), 
            defaultFile="", wildcard="All files (*.*)|*.*", style=wx.SAVE
            )
        if dlg.ShowModal() == wx.ID_OK:
            self.__container.toxml(dlg.GetPath())

    def OnClose(self, event):
        self._mgr.UnInit()
        del self._mgr
        self.Destroy()

    def OnExit(self, event):
        self.Close()

    def OnAbout(self, event):
        msg = u""" 
The MIT License (MIT)
Copyright (c) 2016 

mplotlab by André ASTYL
andreastyl@gmail.com
"""
        dlg = wx.MessageDialog(self, msg, "About mplotlab",
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
