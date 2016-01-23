# -*-coding:Utf-8 -*

from AbcModel import AbcModel,AttributeTypes
import numpy as np

class Variable(AbcModel):
    attributeInfos = list(AbcModel.attributeInfos)
    attributeInfos.extend([
        ("data", (np.ndarray,AttributeTypes.NDARRAY,np.array([]),"data")),
        # filter min/max expression
        # source ?
    ])