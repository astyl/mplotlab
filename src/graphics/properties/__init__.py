# -*-coding:Utf-8 -*

from PyObjectProperty import PyObjectProperty
import wx.propgrid as wxpg


propertyMap = {
    "ndarray": PyObjectProperty,
    "color": wxpg.ColourProperty,   
    "model": PyObjectProperty,
    "string":wxpg.StringProperty,
    "bool":wxpg.BoolProperty,
    "float":wxpg.FloatProperty    
}

