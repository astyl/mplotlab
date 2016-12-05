# -*-coding:Utf-8 -*

from mplotlab.models.abcmodels import AModel
from mplotlab.utils.abctypes import STRING,LIST,INT,RegisterType

class ASlide(AModel):
    parametersInfo = list(AModel.parametersInfo)
    parametersInfo.extend([ 
        ("title",STRING,lambda:"","figure title"),
        ("projections", LIST,lambda:[],"projections"),
        ("animation_period", INT,lambda:500,"refresh animation period in ms"),
    ])

class Slide(ASlide):
    pass

# Atype Registration
RegisterType(ASlide)
RegisterType(Slide)