# -*-coding:Utf-8 -*
"""
TOTO
   
"""


from AbcType import FLOAT,\
                    STRING,\
                    COLOR,\
                    INT,\
                    BOOL

from AbcModel import AbcModel,MODELS,NewModelId
from Source import Source, SourceExpression,SourceSocket,NDARRAY
from Variable import Variable
from Collection import Collection
from Projection import Projection
from Slide import Slide
from Container import Container

Container.registerAType(\
    FLOAT,STRING,COLOR,INT,BOOL,NDARRAY,
    AbcModel,MODELS,
    Source, SourceExpression,SourceSocket,
    Variable,
    Collection,
    Projection,
    Slide,
    Container)
MODELS.containerStaticClass=Container
                