# -*-coding:Utf-8 -*
 
from Variable import Variable
from Collection import Collection
from Projection import Projection
from Slide import Slide


modelClasses = [Variable,Collection,Projection,Slide]
modelContainers = {}

def voidContainers():
    modelContainers.update({modelClass : {} \
                                for modelClass in modelClasses})

voidContainers()

def regModel(model):
    for modelClass in modelClasses:
        if isinstance(model,modelClass):
            name = model.get_name()
            modelContainers[modelClass][name]=model

def delModel(model):
    for modelClass in modelClasses:
        if isinstance(model,modelClass):
            name = model.get_name()
            del modelContainers[modelClass][name]
    del model


