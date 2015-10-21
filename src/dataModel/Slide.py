# -*-coding:Utf-8 -*

from AbcModel import AbcModel

class Slide(AbcModel):
    attributes = dict(AbcModel.attributes)
    attributes.update({
        "projections": (list,"model",[],"projections"),
        "title": (str,"string","","figure title"),
    })
    
    