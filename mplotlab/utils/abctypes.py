# -*-coding:Utf-8 -*
import xml.etree.cElementTree as ET  

__classRegister={}
def RegisterType(cls):
    clsName=cls.__name__
    __classRegister[clsName]=cls

def GetType(name):
    return __classRegister[name]

def GetSubTypes(cls):
    res=[]
    for T in __classRegister.values():
        if issubclass(T, cls):
            res.append(T)
    return res

class AType():
    """ 
    base type declaration
    such as str, float, bool, ...
    But custom types can be 
    handled as well
    """
    BaseType = str

    def __init__(self,*a,**k):
        """ 
        AType constructor creates a
        BaseType object
        """
        self._baseValue=self.BaseType(*a,**k)

    def getBase(self):
        """ 
        @return BaseType object to get
        """
        return self._baseValue

    def setBase(self,value):
        """ 
        @param BaseType object to set
        """
        self._baseValue=value

    def __str__(self,it=""):
        return "%s(%s)"%(self._baseValue,
                        self.__class__.__name__)

    def torootxml(self,parameter,*a,**k):
        root = ET.Element("root")
        self.toxml(parameter,root,*a,**k)
        return root

    def tofilexml(self,parameter,filename,*a,**k):
        root = self.torootxml(parameter,*a,**k)
        tree = ET.ElementTree(root)
        tree.write(filename)
        
    def tostringxml(self,parameter,*a,**k):
        root = self.torootxml(parameter,*a,**k)
        return ET.tostring(root)

    def toxml(self,parameter,et,*a,**k):
        """ 
        Performs XML serialization
        @param parameter: str
            parameter name
        @param et: ElementTree
            parent element tree to populate
        @param k: dict
            optional attributes (for derived class)
        """
        subEt = self.getSubEt(parameter,et,*a,**k)
        self.populate(subEt,*a,**k)

    def getSubEt(self,parameter,et,*a,**k):
        """ 
        Create a sub element for this from 
        a parent element
        @param parameter: str
            parameter name
        @param et: ElementTree
            element tree to populate
        @param k: dict
            optional attributes (for derived class)
        @return ElementTree
        """
        subEt = ET.SubElement(et, parameter)
        subEt.set("type",self.__class__.__name__)
        return subEt

    def populate(self,subEt,*a,**k):
        """
        Parse this on sub element
        @param subEt: ElementTree
            element tree dedicated to parse value 
        @param k: dict
            optional attributes (for derived class)
        """
        subEt.text = unicode(self._baseValue)

    @staticmethod
    def fromfilexml(filename,*a,**k):        
        tree = ET.ElementTree(file=filename)
        return AType.fromxml(tree.getroot(),*a,**k)

    @staticmethod
    def fromstringxml(text,*a,**k):        
        root = ET.fromstring(text)
        return AType.fromxml(root[0],*a,**k)

    @staticmethod
    def fromxml(et,*a,**k):
        """ 
        Return the attribute value
        @param et: Element
            element tree to decode
        @param k: dict
            optional attributes (for derived class)
        """
        clsName = et.attrib["type"]
        cls = GetType(clsName)
        return cls.fromxmlclass(et,*a,**k)

    @classmethod
    def fromxmlclass(cls,et,*a,**k):
        """ 
        Return the attribute value
        @param et: Element
            element tree to decode
        @param k: dict
            optional attributes (for derived class)
        """
        text = et.text if et.text is not None else u""
        return cls(text)

class STRING(AType): 
    pass

class COLOR(AType): 
    pass

class INT(AType):
    """
    >>> valRef = INT(4)
    >>> msg=valRef.tostringxml("max")
    >>> print msg
    <root><max type="INT">4</max></root>
    >>> valExp=AType.fromstringxml(msg)
    >>> print valExp.getBase()
    4
    """
    BaseType = int

class FLOAT(AType):
    """
    >>> valRef = FLOAT(4.5)
    >>> msg=valRef.tostringxml("max")
    >>> print msg
    <root><max type="FLOAT">4.5</max></root>
    >>> valExp=AType.fromstringxml(msg)
    >>> print valExp.getBase()
    4.5
    """
    BaseType = float

class BOOL(AType):
    """
    >>> valRef = BOOL(True)
    >>> msg=valRef.tostringxml("max")
    >>> print msg
    <root><max type="BOOL">1</max></root>
    >>> valExp=AType.fromstringxml(msg)
    >>> print valExp.getBase()
    True
    """
    BaseType = bool

    def populate(self,subEt,*a,**k):
        subEt.text = u"%o"%self._baseValue

    @classmethod
    def fromxmlclass(cls,et,*a,**k):
        val = True if et.text==u"1" else False 
        return cls(val)

class DICT(AType):
    """
    >>> root = ET.Element("root")
    >>> adi = DICT()
    >>> d = adi.getBase()
    >>> d["status"]=BOOL(False)
    >>> d["id"]=INT(36)
    >>> adi.toxml("mydict",root)
    >>> print ET.tostring(root)
    <root><mydict type="DICT"><status type="BOOL">0</status><id type="INT">36</id></mydict></root>
    >>> valExp=AType.fromxml(root[0])
    >>> dictExp=valExp.getBase()
    >>> dictExp["status"].getBase()
    False
    >>> dictExp["id"].getBase()
    36
    """    
    BaseType = dict

    def populate(self,subEt,*a,**k):
        for key,value in self._baseValue.items():
            value.toxml(key,subEt,*a,**k)

    @classmethod
    def fromxmlclass(cls,et,*a,**k):
        obj=cls(*a,**k)
        dico=obj.getBase()
        for subEt in et:
            dico[subEt.tag]=AType.fromxml(subEt,*a,**k)
        return obj

class LIST(AType):
    """
    >>> root = ET.Element("root")
    >>> ali = LIST()
    >>> l = ali.getBase()
    >>> l.append(BOOL(False))
    >>> l.append(INT(36))
    >>> ali.toxml("mylist",root)
    >>> print ET.tostring(root)
    <root><mylist type="LIST"><elem type="BOOL">0</elem><elem type="INT">36</elem></mylist></root>
    >>> valExp=AType.fromxml(root[0])
    >>> ll=valExp.getBase()
    >>> ll[0].getBase()
    False
    >>> ll[1].getBase()
    36
    """    
    BaseType = list

    def populate(self,subEt,*a,**k):
        for value in self._baseValue:
            value.toxml("elem",subEt,*a,**k)

    @classmethod
    def fromxmlclass(cls,et,*a,**k):
        obj=cls(**k)
        ll=obj.getBase()
        for subEt in et:
            ll.append(AType.fromxml(subEt,*a,**k))
        return obj

# Atype Registration
RegisterType(STRING)
RegisterType(COLOR)
RegisterType(INT)
RegisterType(FLOAT)
RegisterType(BOOL)
RegisterType(DICT)
RegisterType(LIST)

if __name__ == '__main__':
    import doctest
    doctest.testmod()