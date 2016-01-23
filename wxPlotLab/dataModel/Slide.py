# -*-coding:Utf-8 -*

from AbcModel import AbcModel,AttributeTypes

class Slide(AbcModel):
    attributeInfos = dict(AbcModel.attributeInfos)
    attributeInfos.update({ 
        "projections": (list,AttributeTypes.MODEL,[],"projections"),
        "title": (str,AttributeTypes.STRING,"","figure title"),
    })
    
    