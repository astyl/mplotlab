# -*-coding:Utf-8 -*

from abcmodels import AModel
from mplotlab.utils.abctypes import FLOAT,LIST,STRING,BOOL,RegisterType

class AProjection(AModel):
    parametersInfo = list(AModel.parametersInfo)
    parametersInfo.extend([ 
        ("plotmodels",LIST,lambda:[],"plotModels"),
        ("title", STRING,lambda:"title","axes title"),
        ("xlabel", STRING,lambda:"","axes xlabel"),
        ("ylabel", STRING,lambda:"","axes ylabel"),
    ])

class Projection2D(AProjection):
    parametersInfo = list(AProjection.parametersInfo)
    parametersInfo.extend([ 
        ("autolim",BOOL,lambda:True,"Auto lim axis. Won't use x/y min/max"),
        ("xmin", FLOAT,lambda:0.0,"axes xmin"),
        ("xmax", FLOAT,lambda:1.0,"axes xmax"),
        ("ymin", FLOAT,lambda:0.0,"axes ymin"),
        ("ymax", FLOAT,lambda:1.0,"axes ymax"),
    ])

RegisterType(AProjection)
RegisterType(Projection2D)
