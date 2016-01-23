# -*-coding:Utf-8 -*

from AbcModel import AbcModel,AttributeTypes

class Slide(AbcModel):
    attributeInfos = list(AbcModel.attributeInfos)
    attributeInfos.extend([ 
        ("title", (str,AttributeTypes.STRING,"","figure title")),
        ("projections", (list,AttributeTypes.MODEL,[],"projections")),
    ])
    
    