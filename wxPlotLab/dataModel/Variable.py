# -*-coding:Utf-8 -*

from AbcModel import AbcModel,MODELS,STRING
# from AbcType import NDARRAY
import numpy as np

class Variable(AbcModel):
    attributeInfos = list(AbcModel.attributeInfos)
    attributeInfos.extend([
        ("data", (np.ndarray,STRING,np.array([]),"data")),
        # filter min/max expression
        # source ?
    ])
