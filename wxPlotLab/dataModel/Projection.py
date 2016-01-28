# -*-coding:Utf-8 -*

from AbcModel import AbcModel,MODELS
from AbcType import FLOAT,STRING,BOOL


class Projection(AbcModel):
    attributeInfos = list(AbcModel.attributeInfos)
    attributeInfos.extend([ 
        ("collections", (list,MODELS,[],"collections")),
        ("xlabel", (str,STRING,"","axes xlabel")),
        ("ylabel", (str,STRING,"","axes ylabel")),
        ("autolim", (bool,BOOL,False,"Auto lim axis. Doesn't use x,y min/max")),
        ("xmin", (float,FLOAT,0.0,"axes xmin")),
        ("xmax", (float,FLOAT,5.0,"axes xmax")),
        ("ymin", (float,FLOAT,0.0,"axes ymin")),
        ("ymax", (float,FLOAT,5.0,"axes ymax")),
    ])
    
