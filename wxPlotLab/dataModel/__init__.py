# -*-coding:Utf-8 -*
from AbcType import FLOAT,\
                    STRING,\
                    COLOR,\
                    INT,\
                    BOOL,\
                    AtypeRegister

from AbcModel import AbcModel,MODELS,NewModelId
from Variable import Variable
from Collection import Collection
from Projection import Projection
from Slide import Slide
from Container import Container

AtypeRegister.registerAType(\
    FLOAT,STRING,COLOR,INT,BOOL, 
    AbcModel,MODELS,
    Variable,
    Collection,
    Projection,
    Slide,
Container)
        
                    