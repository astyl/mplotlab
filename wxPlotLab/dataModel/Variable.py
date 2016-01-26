# -*-coding:Utf-8 -*

from AbcModel import AbcModel,MODELS,STRING
from Source import Source
# from AbcType import NDARRAY
from numpy import *

class Variable(AbcModel):
    attributeInfos = list(AbcModel.attributeInfos)
    attributeInfos.extend([
        ("source", (Source,Source,Source(),"data")),
        ("formula",(str,STRING,"","formula to compose with other variable data "+\
                                "(ex: 'sin(T)' with 'T' a source name)"+\
                                "It uses numpy expressions")),
        # filter min/max expression
    ])
    def getVariableData(self):
        sourceValues = self.get_source().getSourceData()
        values = self.applyFormula(sourceValues)
        # filters and variable composition could be here ..
        return values
    
    def applyFormula(self,sourceValues):
        """
        @param sourceValues : np.array
        @param sources : dict
            ex : {'T':<numpyarray>}
        """
        formula = self.get_formula()
        values = sourceValues
        if formula !="":
            container = self.get_container()
            if container is None:
                raise Exception("variable not registered. Cannot perform formula evaluation")
            sources=self.get_container().getSources()
            values = eval(formula,globals(),{s.get_name():s.getSourceData() for s in sources})
        return values
        

        