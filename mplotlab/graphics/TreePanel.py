# -*-coding:Utf-8 -*

import wx
from mplotlab import App
from mplotlab.models.abcmodels import AModel
from mplotlab.models.container import Container
from mplotlab.models.slides import ASlide,Slide
from mplotlab.models.projections import AProjection,Projection2D
from mplotlab.models.plotmodels import  APlotModel,Line2D
from mplotlab.models.variables import AVariable,Variable
from mplotlab.models.sources import ASource,SourceExpression, SourceSocket

class TreePanel(wx.TreeCtrl):
    def __init__(self,parent,configPanel):        
        wx.TreeCtrl.__init__(self,parent, -1, wx.Point(0, 0), wx.Size(160, 250),
                       wx.TR_DEFAULT_STYLE | wx.NO_BORDER)
    
    
        imglist = wx.ImageList(16, 16, True, 2)
        imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_REPORT_VIEW, wx.ART_OTHER, wx.Size(16,16)))
        imglist.Add(wx.ArtProvider_GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, wx.Size(16,16)))
        self.AssignImageList(imglist)
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self)
        self.Bind(wx.EVT_RIGHT_UP, self.OnRightUp,self)
        self.__modelSel = None
        self.__configPanel = configPanel

    def OnRightUp(self,event):
        it = self.GetSelection()
        if not it.IsOk():
            event.Skip()  
            return
        mdl = self.GetItemPyData(it)
        if not isinstance(mdl ,(AModel,Container)):
            event.Skip()  
            return
        menu = wx.Menu()
        if isinstance(mdl,Container):
            container=mdl
            item1 = menu.Append(wx.ID_ANY, "Create Slide")
            item2 = menu.Append(wx.ID_ANY, "Create Projection2D")
            item3 = menu.Append(wx.ID_ANY, "Create Line2D")
            item4 = menu.Append(wx.ID_ANY, "Create Variable")
            item5 = menu.Append(wx.ID_ANY, "Create Source Expression")
            item6 = menu.Append(wx.ID_ANY, "Create Source Socket")
            self.Bind(wx.EVT_MENU, lambda *a,**k:Slide(container,name="newSlide"), item1)
            self.Bind(wx.EVT_MENU, lambda *a,**k:Projection2D(container,name="newProjection"), item2)
            self.Bind(wx.EVT_MENU, lambda *a,**k:Line2D(container,name="newLine2D"), item3)
            self.Bind(wx.EVT_MENU, lambda *a,**k:Variable(container,name="newVariable"), item4)
            self.Bind(wx.EVT_MENU, lambda *a,**k:SourceExpression(container,name="newSourceExpression"), item5)
            self.Bind(wx.EVT_MENU, lambda *a,**k:SourceSocket(container,name="newSourceSocket"), item6)
        elif isinstance(mdl,APlotModel):
            item1 = menu.Append(wx.ID_ANY, "choose plotmodels")
            self.Bind(wx.EVT_MENU, self.getFnSelectModels("Variables", "getVariables", "variables", mdl), item1)
        elif isinstance(mdl,AProjection):
            item1 = menu.Append(wx.ID_ANY, "choose plotmodels")
            self.Bind(wx.EVT_MENU, self.getFnSelectModels("Plotmodels", "getPlotModels", "plotmodels", mdl), item1)
        elif isinstance(mdl,ASlide):
            item1 = menu.Append(wx.ID_ANY, "choose projections")
            self.Bind(wx.EVT_MENU, self.getFnSelectModels("Projections", "getProjections", "projections", mdl), item1)
        elif isinstance(mdl,ASource):
            item1 = menu.Append(wx.ID_ANY, "Init")
            item2 = menu.Append(wx.ID_ANY, "Start")
            item3 = menu.Append(wx.ID_ANY, "Stop")
            self.Bind(wx.EVT_MENU, lambda *a,**k:mdl.init(), item1)
            self.Bind(wx.EVT_MENU, lambda *a,**k:mdl.start(), item2)
            self.Bind(wx.EVT_MENU, lambda *a,**k:mdl.stop(), item3)
        self.PopupMenu(menu)
        menu.Destroy()
        if isinstance(mdl, AModel):
            self.__modelSel = mdl
            self.__configPanel.updatePage(self.__modelSel)        
        event.Skip()

    def getFnSelectModels(self,title,getterN,key,mdl):
        def fn(*a,**k):
            mdls=getattr(mdl.getContainer(),getterN)()
            mdlsAlSel=getattr(mdl,"get_"+key)()
            dlg = wx.MultiChoiceDialog(self, 
                        'Select %s for model %s'%(title,mdl.get_name()),
                        title+' selection',
                        [m.get_name() for m in mdls])
            sels=[]
            for i,m in enumerate(mdls):
                if m in mdlsAlSel:
                    sels.append(i)
            dlg.SetSelections(sels)
            if dlg.ShowModal() == wx.ID_OK:
                mdlsSel=[mdls[i] for i in dlg.GetSelections()]
                getattr(mdl,"set_"+key)(mdlsSel)
        return fn

    def OnSelChanged(self,event):
        item = event.GetItem()
        a = self.GetItemData(item).GetData()
        if isinstance(a, AModel):
            self.__modelSel = a
            self.__configPanel.updatePage(self.__modelSel)
        event.Skip()

    def getSlideSelected(self):
        it = self.GetSelection()
        if not it.IsOk():
            return None
        k = 0
        mdlSel = None
        while k < 4:
            mdlSel = self.GetItemPyData(it)
            if not isinstance(mdlSel,AModel):
                return None
            if isinstance(mdlSel,ASlide):
                break
            else:
                it = self.GetItemParent(it)
            k +=1

        print k
        if k < 4:
            return mdlSel

    def updateTree(self):
        self.DeleteAllItems()
        container=App().mainWin.getContainer()
        root = self.AddRoot("container",data=wx.TreeItemData(container))
        cc=self.AppendItem(root, "slides", 0,data=wx.TreeItemData(container))
        for slide in container.getSlides():
            it = self.AppendItem(cc, slide.get_name(), 1,data=wx.TreeItemData(slide))
            if slide == self.__modelSel: self.SelectItem(it)
               
            for projection in slide.get_projections():
                itt = self.AppendItem(it, projection.get_name(), 1,data=wx.TreeItemData(projection))
                if projection == self.__modelSel: self.SelectItem(itt)
                
                for pmdl in projection.get_plotmodels():
                    ittt = self.AppendItem(itt, pmdl.get_name(), 1,data=wx.TreeItemData(pmdl))
                    if pmdl == self.__modelSel: self.SelectItem(ittt)
                    
                    for variable in pmdl.get_variables():
                        itttt = self.AppendItem(ittt, variable.get_name(), 1,data=wx.TreeItemData(variable))
                        if variable == self.__modelSel: self.SelectItem(itttt)

        ll=[("projections",container.getProjections()),
            ("plotmodels",container.getPlotModels()),
            ("variables",container.getVariables()),
            ("sources",container.getSources())]
        for label,mdls in ll:
            cc=self.AppendItem(root, label, 0,data=wx.TreeItemData(container))
            for mdl in mdls:
                it = self.AppendItem(cc, mdl.get_name(), 1,data=wx.TreeItemData(mdl))
                if mdl == self.__modelSel: self.SelectItem(it)
