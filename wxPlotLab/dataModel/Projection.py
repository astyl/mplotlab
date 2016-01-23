# -*-coding:Utf-8 -*

from AbcModel import AbcModel,AttributeTypes

class Projection(AbcModel):
    attributeInfos = dict(AbcModel.attributeInfos)
    attributeInfos.update({ 
        "collections": (list,AttributeTypes.MODEL,[],"collections"),
        "xlabel": (str,AttributeTypes.STRING,"","axes xlabel"),
        "ylabel": (str,AttributeTypes.STRING,"","axes ylabel"),
        "xmin": (float,AttributeTypes.FLOAT,0.0,"axes xmin"),
        "xmax": (float,AttributeTypes.FLOAT,5.0,"axes xmax"),
        "ymin": (float,AttributeTypes.FLOAT,0.0,"axes ymin"),
        "ymax": (float,AttributeTypes.FLOAT,5.0,"axes ymax"),
    })
    
