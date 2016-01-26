# -*-coding:Utf-8 -*

from AbcModel import MODELS,AtypeRegister
from Variable import Variable
from Collection import Collection
from Projection import Projection
from Slide import Slide
import xml.etree.cElementTree as ET  


class Container(object):
    MODELCLASSES = [Variable,Collection,Projection,Slide]
    def __init__(self):
        self.__modelsByClass = {}
        self.__modelsById = {}
        self.flush()

    def __str__(self,*a,**k):
        msg = ""
        for modelClass in self.MODELCLASSES:
            for model in self.__modelsByClass[modelClass]:
                msg+=model.__str__(*a,**k)
        return msg

    def flush(self):
        self.__modelsByClass.update({modelClass : [] \
                                for modelClass in self.MODELCLASSES})
        self.__modelsById = {}

    def toxml(self,filename):
        root = ET.Element("container")
        for modelClass in self.MODELCLASSES:
            models=[]
            for model in self.__modelsByClass[modelClass]:
                models.append(model)
            MODELS.toxml(modelClass.__name__,models,root,parseModel=True)
        tree = ET.ElementTree(root)
        tree.write(filename)

    def fromxml(self,filename):        
        tree = ET.ElementTree(file=filename)
        root = tree.getroot()
        for et in root:
            models = MODELS.fromxml(et,container=self)
            for model in models:
                self.register(model)
        return ET.ElementTree(root)

    def register(self,model):
        m_id = model.get_id()
        if not self.hasModel(m_id):
            self.__modelsById[m_id]=model
            for modelClass in self.MODELCLASSES:
                if isinstance(model,modelClass):
                    ll = self.__modelsByClass[modelClass]
                    ll.append(model)
                    break

    def delete(self,model):
        m_id = model.get_id()
        if self.hasModel(m_id):
            del self.__modelsById[m_id]
            for modelClass in self.MODELCLASSES:
                if isinstance(model,modelClass):
                    ll = self.__modelsByClass[modelClass]
                    del ll[ll.index(model)]

    def hasModel(self,m_id):
        return self.__modelsById.has_key(m_id)

    def getModel(self,m_id):
        return self.__modelsById.get(m_id,None)

    def getVariables(self):
        return self.__modelsByClass[Variable]

    def getCollections(self):
        return self.__modelsByClass[Collection]

    def getProjections(self):
        return self.__modelsByClass[Projection]

    def getSlides(self):
        return self.__modelsByClass[Slide]
