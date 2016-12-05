# -*-coding:Utf-8 -*

from abcmodels import AModel
from mplotlab.utils.abctypes import RegisterType,LIST,COLOR,STRING,BOOL

class APlotModel(AModel):
    parametersInfo = list(AModel.parametersInfo)
    parametersInfo.extend([
        ("variables",LIST,lambda:[],"variables X, Y [,Z] ... "),
        ("animation",BOOL,lambda:False,"plot animation")
    ])

class Line2D(APlotModel):
    parametersInfo = list(APlotModel.parametersInfo)
    parametersInfo.extend([
        ("color",COLOR,lambda:'blue',"line color"),
        ("linestyle",STRING,lambda:'-',"linestyle"),
    ])

# Atype Registration
RegisterType(APlotModel)
RegisterType(Line2D)
