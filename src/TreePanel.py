# -*-coding:Utf-8 -*

import wx
class TreePanel(wx.TreeCtrl):

    def __init__(self,parent):
        wx.TreeCtrl.__init__(self,parent, -1, wx.Point(0, 0), wx.Size(160, 250),
                       wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
    
        root = self.AddRoot("wxPlotLab")
        items = []
    
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, wx.Size(16,16)))
        imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16,16)))
        self.AssignImageList(imglist)
    
        items.append(self.AppendItem(root, "Item 1", 0))
        items.append(self.AppendItem(root, "Item 2", 0))
        items.append(self.AppendItem(root, "Item 3", 0))
        items.append(self.AppendItem(root, "Item 4", 0))
        items.append(self.AppendItem(root, "Item 5", 0))
    
        for ii in xrange(len(items)):
        
            id = items[ii]
            self.AppendItem(id, "Subitem 1", 1)
            self.AppendItem(id, "Subitem 2", 1)
            self.AppendItem(id, "Subitem 3", 1)
            self.AppendItem(id, "Subitem 4", 1)
            self.AppendItem(id, "Subitem 5", 1)
        
        self.Expand(root)