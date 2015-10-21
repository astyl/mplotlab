# -*-coding:Utf-8 -*

from PyObjectProperty import PyObjectProperty
from wx.propgrid import ColourProperty,\
                        BoolProperty,\
                        FloatProperty,\
                        IntProperty,\
                        StringProperty


propertyMap = {
    "ndarray": PyObjectProperty,
    "color": ColourProperty,   
    "model": PyObjectProperty,
    "string":StringProperty,
    "bool":BoolProperty,
    "int":IntProperty,
    "float":FloatProperty    
}

