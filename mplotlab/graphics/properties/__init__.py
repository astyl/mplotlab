# -*-coding:Utf-8 -*

from PyObjectProperty import PyObjectProperty
from wx.propgrid import ColourProperty,\
                        BoolProperty,\
                        FloatProperty,\
                        IntProperty,\
                        StringProperty
from mplotlab.dataModel import COLOR,\
                               STRING,\
                               INT,\
                               FLOAT,\
                               BOOL,\
                               MODELS,\
                               Variable,\
                               Source,\
                               NDARRAY

propertyMap = {
    COLOR: ColourProperty,   
    STRING:StringProperty,
    BOOL:BoolProperty,
    INT:IntProperty,
    FLOAT:FloatProperty,
    MODELS:PyObjectProperty, 
    Variable:PyObjectProperty,   
    Source:PyObjectProperty,     
    NDARRAY:PyObjectProperty,      
}

