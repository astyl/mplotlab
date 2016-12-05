# -*-coding:Utf-8 -*

import xml.etree.cElementTree as ET  
import numpy as np
import codecs

class AType(object):
    ## default type associated for this value
    typeClass = str
    
    @classmethod
    def toxml(cls,parameter,value,et,attr={},**k):
        """ 
        @param parameter: str
            parameter name
        @param value: object
            attribute value
        @param et: ElementTree
            element tree to populate onto
        @param attr: dict
            element tree child attributes 
        @param k: dict
            optionnal attributes (for derived class)
        example:
            INT.toxml("width", 200, root) 
            produces :
            <root>
                (...)
                <INT name="width">200</INT>
            </root> 
        """
        subEt = cls.getSubEt(cls.__name__,parameter,value,et,**attr)
        cls.populate(parameter,value,subEt,**k)
    
    @staticmethod
    def getSubEt(clsname,parameter,value,et,**attr):
        """ 
        Create a sub element for the attribute
        @param clsname: str
            attribute class name
        @param parameter: str
            parameter name
        @param et: ElementTree
            element tree to populate onto
        @param value: object
            attribute value
        @param attr: dict
            element tree child(s) attributes
        @return ElementTree
        """
        return ET.SubElement(et, clsname,parameter=parameter,**attr)

    @classmethod
    def populate(cls,parameter,value,subEt,**k):
        """
        Parse attribute value within the sub element
        @param parameter: str
            parameter name
        @param value: object
            attribute value
        @param subEt: ElementTree
            element tree dedicated to parse value 
        @param k: dict
            optionnal attributes (for derived class)
        """
        subEt.text = cls.tostring(value,**k)

    @classmethod
    def tostring(cls,value,**k):
        """
        Return the attribute value parsed (unicode)
        @param value: object
            attribute value
        @param k: dict
            optionnal attributes (for derived class)
        @return unicode
        """        
        return unicode(value)

    @classmethod
    def fromxml(cls,et,**k):
        """ 
        Return the attribute value
        @param et: Element
            element tree to decode
        @param k: dict
            optionnal attributes (for derived class)
        @param object
        example:
            if et represents:
                <INT name="width">200</INT>        
            INT.fromxml(et) -> 200 
        """
        text = et.text if et.text is not None else ""
        return cls.fromstring(text,attr=et.attrib,**k)

    @classmethod
    def fromstring(cls,text,attr={},**k):
        """ 
        Return the value from parsed unicode
        @param text: unicode 
            text of element tree
        @param attr: dict
            element tree attributes
        @param k: dict
            optionnal attributes (for derived class)
        @param object
        """        
        return cls.typeClass(text)

class STRING(AType): 
    pass

class COLOR(AType): 
    pass

class INT(AType): 
    typeClass = int

class FLOAT(AType): 
    typeClass = float

class BOOL(AType):
    typeClass = bool
    @classmethod
    def tostring(cls,value,**k):
        return u"%o"%value

    @classmethod
    def fromstring(cls,text,**k):
        return text != u"0"




