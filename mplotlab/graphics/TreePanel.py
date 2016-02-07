# -*-coding:Utf-8 -*

import wx
from mplotlab import App
from mplotlab.models import Slide
from mplotlab.models import AbcModel

class TreePanel(wx.TreeCtrl):
    def __init__(self,parent,configPanel):        
        wx.TreeCtrl.__init__(self,parent, -1, wx.Point(0, 0), wx.Size(160, 250),
                       wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
    
    
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_REPORT_VIEW, wx.ART_OTHER, wx.Size(16,16)))
        imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16,16)))
        self.AssignImageList(imglist)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self)
        
        self.__modelSel = None
        self.__configPanel = configPanel

    def OnSelChanged(self,event):
        item = event.GetItem()
        a = self.GetItemData(item).GetData()
        if isinstance(a,AbcModel):
            self.__modelSel = a
            self.__configPanel.updatePage(self.__modelSel)
    
    def getSlideSelected(self):
        it = self.GetSelection()
        if not it.IsOk():
            return
        k = 0
        sliceSel = None
        while k < 5:
            sliceSel = self.GetItemPyData(it)
            if isinstance(sliceSel,Slide):
                break
            else:
                it = self.GetItemParent(it)
            k +=1
            
        if k < 5:
            return sliceSel
            

    def updateTree(self):
        self.DeleteAllItems()
        root = self.AddRoot("container",data=wx.TreeItemData(self))
        for slide in App().mainWin.getContainer().getSlides():
            it = self.AppendItem(root, slide.get_name(), 0,data=wx.TreeItemData(slide))
            if slide == self.__modelSel: self.SelectItem(it)
               
            for projection in slide.get_projections():
                itt = self.AppendItem(it, projection.get_name(), 0,data=wx.TreeItemData(projection))
                if projection == self.__modelSel: self.SelectItem(itt)
                
                for collection in projection.get_collections():
                    ittt = self.AppendItem(itt, collection.get_name(), 1,data=wx.TreeItemData(collection))
                    if collection == self.__modelSel: self.SelectItem(ittt)
                    
                    for variable in [collection.get_X(),collection.get_Y()]:
                        itttt = self.AppendItem(ittt, variable.get_name(), 1,data=wx.TreeItemData(variable))
                        if variable == self.__modelSel: self.SelectItem(itttt)
                        
                        for source in [variable.get_source()]:
                            ittttt = self.AppendItem(itttt, source.get_name(), 1,data=wx.TreeItemData(source))
                            if source == self.__modelSel: self.SelectItem(ittttt)
                        
                        