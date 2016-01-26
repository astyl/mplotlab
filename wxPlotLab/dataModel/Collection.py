# -*-coding:Utf-8 -*

from AbcModel import AbcModel
from Variable import Variable
from AbcType import COLOR ,\
                    STRING

class Collection(AbcModel):
    attributeInfos = list(AbcModel.attributeInfos)
    attributeInfos.extend([
        ("X", (Variable,Variable,Variable(),"var X")),
        ("Y", (Variable,Variable,Variable(),"var Y")),
        ("color", (str,COLOR,"blue","artist color")),
        ("linestyle",  (str,STRING,"-","linestyle")),
    ])
