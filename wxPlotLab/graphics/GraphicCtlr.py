# -*-coding:Utf-8 -*

from Navigation import Navigation

class GraphicCtlr(object):

    def __init__(self,mainWin):
        self.__mainWin = mainWin
        self.__canvas = mainWin.getCanvas()
        self.__navigation = Navigation(self.__canvas,mainWin=mainWin)    
        
    def zoom(self):
        self.__navigation.zoom() 
        
    def pan(self):
        self.__navigation.pan() 