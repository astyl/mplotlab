# -*-coding:Utf-8 -*

import wx
from wx.aui import AuiNotebook
from mplotlab import App
from GraphicPanel import GraphicPanel

class GraphicBook(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent)
        
        # tabs handler
        self.__book= AuiNotebook(self)
        
        self.layout()

    def layout(self):
        sizer = wx.BoxSizer()
        sizer.Add(self.__book, 1, wx.EXPAND)
        self.SetSizer(sizer)
        wx.CallAfter(self.__book.SendSizeEvent)

    def updateBook(self):
        """
        Delete graphicPanel pages that refer to 'obselete' slide
        And update book page name from its slide name
        """
        cs = {slide: slide.get_name() \
                for slide in App().mainWin.getContainer().getSlides()}
        for i,gp in enumerate(self.getGraphicPanels()):
            slide = gp.getSlide()
            if not slide in cs.keys():
                self.__book.DeletePage(i)
                self.updateBook()
                return
            else:
                self.__book.SetPageText(i,cs[slide])
        gpSlides=self.getGraphicSlides()
        for slide in cs.keys():
            if not slide in gpSlides:
                gp=self.createGraphicPanel(slide)
            else:
                gp=self.getGraphicPanel(slide)
    
    def createGraphicPanel(self,slide):
        """ Create the graphic panel for the slide
        if necessary and select it.
        There cannot be 2 graphic panels for the same
        slide
        """
        gp = GraphicPanel(self)
        gp.setSlide(slide)
        self.__book.AddPage(gp, slide.get_name())
        return gp

    def selectGraphicPanel(self,gp):
        idx = self.getGraphicPanels().index(gp)
        self.__book.SetSelection(idx)

    def getGraphicPanel(self,slide):
        gp=None
        ss = self.getGraphicSlides()
        if slide in ss:
            idx = ss.index(slide)
            gp = self.getGraphicPanels()[idx]
        return gp  

    def getGraphicSlides(self):
        return [gp.getSlide() for gp in self.getGraphicPanels()]

    def getGraphicPanels(self):
        return [self.__book.GetPage(i) for i in \
                            range(self.__book.GetPageCount())]

