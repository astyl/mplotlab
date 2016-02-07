# -*-coding:Utf-8 -*

from Navigation import Navigation

class GraphicCtlr(object):

    def __init__(self,canvas):
        self.__canvas = canvas
        self.__navigation = Navigation(self.__canvas)

    def control(self,zoom=True,pan=False):
        nav = self.__navigation
        if pan == (nav._active != "PAN"):
            nav.pan()
        if zoom == (nav._active != "ZOOM"):
            nav.zoom()
