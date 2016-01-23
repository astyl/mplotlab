# -*-coding:Utf-8 -*

from AbcModel import AbcModel,AttributeTypes
from Variable import Variable

class Collection(AbcModel):
    attributeInfos = list(AbcModel.attributeInfos)
    attributeInfos.extend([
        ("X", (Variable,AttributeTypes.MODEL,Variable(),"var X")),
        ("Y", (Variable,AttributeTypes.MODEL,Variable(),"var Y")),
        ("color", (str,AttributeTypes.COLOR,"blue","artist color")),
        ("linestyle",  (str,AttributeTypes.STRING,"-","linestyle")),
    ])        
        
        
        
    