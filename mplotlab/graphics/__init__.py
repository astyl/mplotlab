# -*-coding:Utf-8 -*

import wx

from PyObjectProperty import PyObjectProperty
from wx.propgrid import ColourProperty,\
                        BoolProperty,\
                        FloatProperty,\
                        IntProperty,\
                        StringProperty
from mplotlab.models import COLOR,\
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

# Plot Panel111
from GraphicPanel import GraphicPanel
def newWxPlotPanel(parent):
    return GraphicPanel(parent)

# Plot Frame
from MainWin import MainWin
def newWxPlotFrame():
    return MainWin()