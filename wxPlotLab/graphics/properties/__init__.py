# -*-coding:Utf-8 -*

from PyObjectProperty import PyObjectProperty
from wx.propgrid import ColourProperty,\
                        BoolProperty,\
                        FloatProperty,\
                        IntProperty,\
                        StringProperty
from wxPlotLab.dataModel import COLOR,STRING,INT,FLOAT,BOOL,MODELS,Variable
# class :
#     # this class is only used as a simple enumeration
#     STRING,COLOR,NDARRAY,INT,FLOAT,MODEL= list(range(6))
# from wxPlotLab.dataModel import AbcModel,

propertyMap = {
#     NDARRAY: PyObjectProperty,
    COLOR: ColourProperty,   
#     MODEL: PyObjectProperty,
    STRING:StringProperty,
    BOOL:BoolProperty,
    INT:IntProperty,
    FLOAT:FloatProperty,
    MODELS:PyObjectProperty, 
    Variable:PyObjectProperty,     
}

