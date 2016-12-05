# -*-coding:Utf-8 -*

from mplotlab.utils.abctypes import RegisterType,STRING
from abcmodels import AModel
from numpy import *

class AVariable(AModel):
    def getData(self):
        return []

class Variable(AVariable):
    parametersInfo = list(AVariable.parametersInfo)
    parametersInfo.extend([
        ("formula",STRING,lambda:'',"formula that combines data sources"+\
                                    "(ex: 'sin(T)' with 'T' a source name)"+\
                                    "It calls numpy functions"),
    ])

    def getData(self):
        formula = self.get_formula()
        container = self.getContainer()
        if container is None:
            raise Exception("variable not registered in a container"+
                            "Cannot perform formula evaluation")
        sources=container.getSources()
        values = eval(formula,
                      globals(),
                      {s.get_name():s.getData() for s in sources})
        return values
        
# Atype Registration
RegisterType(AVariable)
RegisterType(Variable)
        