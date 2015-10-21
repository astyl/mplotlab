# -*-coding:Utf-8 -*

from AbcModel import AbcModel
from Variable import Variable

class Collection(AbcModel):
    attributes = dict(AbcModel.attributes)
    attributes.update({
        "X": (Variable,"model",Variable(),"var X"),
        "Y": (Variable,"model",Variable(),"var Y"),
        "color": (str,"color","blue","artist color"),
        "linestyle":  (str,"string","-","linestyle"),
    })        
        
        
        
    