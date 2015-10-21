# -*-coding:Utf-8 -*

from AbcModel import AbcModel

class Projection(AbcModel):
    attributes = dict(AbcModel.attributes)
    attributes.update({
        "collections": (list,"model",[],"collections"),
        "xlabel": (str,"string","","axes xlabel"),
        "ylabel": (str,"string","","axes ylabel"),
        "xmin": (float,"float",0.0,"axes xmin"),
        "xmax": (float,"float",5.0,"axes xmax"),
        "ymin": (float,"float",0.0,"axes ymin"),
        "ymax": (float,"float",5.0,"axes ymax"),
    })
    
