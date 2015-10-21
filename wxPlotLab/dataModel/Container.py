# -*-coding:Utf-8 -*

from Variable import Variable
from Collection import Collection
from Projection import Projection
from Slide import Slide

MODELCLASSES = [Variable,Collection,Projection,Slide]


class Container():
    def __init__(self):
        self.__modelContainers = {}
        self.voidModels()

    def voidModels(self):
        self.__modelContainers.update({modelClass : {} \
                                for modelClass in MODELCLASSES})

    def regModel(self,model):
        for modelClass in MODELCLASSES:
            if isinstance(model,modelClass):
                name = model.get_name()
                self.__modelContainers[modelClass][name]=model

    def delModel(self,model):
        for modelClass in MODELCLASSES:
            if isinstance(model,modelClass):
                name = model.get_name()
                del self.__modelContainers[modelClass][name]
        del model
