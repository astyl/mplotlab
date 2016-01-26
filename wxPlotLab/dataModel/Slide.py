# -*-coding:Utf-8 -*

from AbcModel import AbcModel,MODELS
from AbcType import STRING

class Slide(AbcModel):
    attributeInfos = list(AbcModel.attributeInfos)
    attributeInfos.extend([ 
        ("title", (str,STRING,"","figure title")),
        ("projections", (list,MODELS,[],"projections")),
    ])
