# -*-coding:Utf-8 -*

import wx

class TreePanel(wx.TreeCtrl):

    def __init__(self,parent):
        wx.TreeCtrl.__init__(self,parent, -1, wx.Point(0, 0), wx.Size(160, 250),
                       wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
    
    
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_REPORT_VIEW, wx.ART_OTHER, wx.Size(16,16)))
        imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16,16)))
        self.AssignImageList(imglist)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self)
        
        self.__mainWin = parent
        self.__artistSel = None
        
    def getArtistSel(self):
        return self.__artistSel
        
    def OnSelChanged(self,event):
        item = event.GetItem()
        self.__artistSel = self.GetItemData(item).GetData()
        self.__mainWin.updatePageConfig()
        
    def updateTree(self):
        self.DeleteAllItems()
        from __init__ import figure
        
        
        root = self.AddRoot("%s"%figure,data=wx.TreeItemData(figure))
        if figure == self.__artistSel: self.SelectItem(root)

        for axes in figure.axes:
            it = self.AppendItem(root, "%s"%axes, 0,data=wx.TreeItemData(axes))
            if axes == self.__artistSel: self.SelectItem(it)
            for line in axes.lines:
                itt = self.AppendItem(it, "%s"%line, 1,data=wx.TreeItemData(line))
                if line == self.__artistSel: self.SelectItem(itt)

        import matplotlib.axes
        matplotlib.axes.Axes