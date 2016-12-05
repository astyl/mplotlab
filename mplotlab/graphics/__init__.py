# -*-coding:Utf-8 -*

import wx
from PyObjectProperty import PyObjectProperty
from wx.propgrid import ColourProperty,\
                        BoolProperty,\
                        FloatProperty,\
                        IntProperty,\
                        StringProperty

from mplotlab.utils.abctypes import \
    STRING,COLOR, INT, FLOAT, BOOL,LIST
from mplotlab.models.abcmodels import \
    AModel
from mplotlab.models.sources import \
    ASource
from mplotlab.models.variables import Variable
###
ASource.CallLater=wx.CallLater

propertyMap = {
    COLOR: ColourProperty,   
    STRING:StringProperty,
    BOOL:BoolProperty,
    INT:IntProperty,
    FLOAT:FloatProperty,
    LIST:PyObjectProperty,
    AModel:PyObjectProperty, 
    Variable:PyObjectProperty, 
}

# Plot Panel1
from GraphicPanel import GraphicPanel
def newWxPlotPanel(parent):
    return GraphicPanel(parent)

# Plot Frame
from MainWin import MainWin
def newWxPlotFrame():
    return MainWin()

