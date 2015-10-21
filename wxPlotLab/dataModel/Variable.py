# -*-coding:Utf-8 -*

from AbcModel import AbcModel
import numpy as np

class Variable(AbcModel):
    attributes = dict(AbcModel.attributes)
    attributes.update({
        "data": (np.ndarray,"ndarray",np.array([]),"data"),
        # filter min/max expression
        # source ?
    })