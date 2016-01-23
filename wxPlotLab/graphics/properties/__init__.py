# -*-coding:Utf-8 -*

from PyObjectProperty import PyObjectProperty
from wx.propgrid import ColourProperty,\
                        BoolProperty,\
                        FloatProperty,\
                        IntProperty,\
                        StringProperty

# class :
#     # this class is only used as a simple enumeration
#     STRING,COLOR,NDARRAY,INT,FLOAT,MODEL= list(range(6))
from wxPlotLab.dataModel import AttributeTypes
propertyMap = {
    AttributeTypes.NDARRAY: PyObjectProperty,
    AttributeTypes.COLOR: ColourProperty,   
    AttributeTypes.MODEL: PyObjectProperty,
    AttributeTypes.STRING:StringProperty,
    AttributeTypes.BOOL:BoolProperty,
    AttributeTypes.INT:IntProperty,
    AttributeTypes.FLOAT:FloatProperty    
}

