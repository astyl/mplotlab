# -*-coding:Utf-8 -*

import wx

class TreePanel(wx.TreeCtrl):

    def __init__(self,parent,figure):        
        wx.TreeCtrl.__init__(self,parent, -1, wx.Point(0, 0), wx.Size(160, 250),
                       wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
    
    
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_REPORT_VIEW, wx.ART_OTHER, wx.Size(16,16)))
        imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16,16)))
        self.AssignImageList(imglist)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self)
        
        self.__figure = figure
        self.__mainWin = parent
        self.__modelSel = None
        
    def getModelSel(self):
        return self.__modelSel
        
    def OnSelChanged(self,event):
        item = event.GetItem()
        self.__modelSel = self.GetItemData(item).GetData()
        self.__mainWin.updatePageConfig()
        
    def updateTree(self):
        self.DeleteAllItems()
        slide = self.__mainWin.getCurrentSlide()
        if not slide is None:
            root = self.AddRoot(slide.get_name(),data=wx.TreeItemData(slide))
            if slide == self.__modelSel: self.SelectItem(root)
    
            for projection in slide.get_projections():
                it = self.AppendItem(root, projection.get_name(), 0,data=wx.TreeItemData(projection))
                if projection == self.__modelSel: self.SelectItem(it)
                
                for collection in projection.get_collections():
                    itt = self.AppendItem(it, collection.get_name(), 1,data=wx.TreeItemData(collection))
                    if collection == self.__modelSel: self.SelectItem(itt)