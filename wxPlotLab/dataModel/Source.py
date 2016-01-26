# -*-coding:Utf-8 -*

from AbcModel import AbcModel,STRING
from AbcType import AType
import numpy as np

class NDARRAY(AType):
    @classmethod
    def toxml(*a,**k):
        """ values aren't serialized as any parameter.
        They are generated from source handlers such as
        expression, files or remote data streams
        """
        pass
    @classmethod
    def fromstring(*a,**k):
        return np.array([])

class Source(AbcModel):
    attributeInfos = list(AbcModel.attributeInfos)
    attributeInfos.extend([
        ("values", (np.ndarray,NDARRAY,np.array([]),"values to address to many variables")),
    ])
    def __init__(self,*a,**k):
        AbcModel.__init__(self,*a,**k)
        self.__isInit = False 
        
    def initHandlers(self):
        """ Initialize values"""
        self.__isInit = True
        
    def getSourceData(self):
        if not self.__isInit:
            self.initHandlers()
        return self.get_values().copy()

class SourceExpression(Source):
    attributeInfos = list(Source.attributeInfos)
    attributeInfos.extend([
        ("expression", (str,STRING,"","expression that returns a numpy array")),
    ])

    def initHandlers(self):
        """ Initialize values """
        values = eval(self.get_expression())
        self.set_values(values)
        Source.initHandlers(self)

