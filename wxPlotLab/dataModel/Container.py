# -*-coding:Utf-8 -*

from Variable import Variable
from Collection import Collection
from Projection import Projection
from Slide import Slide

MODELCLASSES = [Variable,Collection,Projection,Slide]

class Container():
    def __init__(self):
        self.__modelContainers = {}
        self.flush()

    def flush(self):
        self.__modelContainers.update({modelClass : {} \
                                for modelClass in MODELCLASSES})

    def register(self,model):
        for modelClass in MODELCLASSES:
            if isinstance(model,modelClass):
                name = model.get_name()
                self.__modelContainers[modelClass][name]=model

    def delete(self,model):
        for modelClass in MODELCLASSES:
            if isinstance(model,modelClass):
                name = model.get_name()
                del self.__modelContainers[modelClass][name]
        del model

    def getVariables(self):
        return self.__modelContainers[Variable]

    def getCollections(self):
        return self.__modelContainers[Collection]

    def getProjections(self):
        return self.__modelContainers[Projection]

    def getSlides(self):
        return self.__modelContainers[Slide]
            