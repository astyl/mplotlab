# -*-coding:Utf-8 -*

from Navigation import Navigation


class GraphicCtlr(object):

    def __init__(self,canvas):
        self.__navigation = Navigation(canvas)    
        
    def zoom(self):
        self.__navigation.zoom() 
        
    def pan(self):
        self.__navigation.pan() 