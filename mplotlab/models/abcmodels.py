# -*-coding:Utf-8 -*
from mplotlab.utils.decorators import checkTypeReturned, checkTypeParams
from mplotlab.utils.abctypes import RegisterType,AType,STRING,DICT

def NewModelId(cls):
    if not NewModelId.idsByType.has_key(cls):
        NewModelId.idsByType[cls]=0
    modelId = int(NewModelId.idsByType[cls])
    NewModelId.idsByType[cls]+=1
    return modelId
NewModelId.idsByType={}

class AModel(DICT):
    """ 
    Base model class
    >>> import xml.etree.cElementTree as ET
    >>> root = ET.Element("root")
    >>> from container import Container
    >>> ct = Container()
    >>> mdl = AModel(ct,name="tintin")
    >>> mdl.toxml("model",root,populateModel=True)
    >>> print ET.tostring(root)
    <root><model id="0" type="AModel"><name type="STRING">tintin</name></model></root>
    >>> ct2 = Container()
    >>> mdlExp=AType.fromxml(root[0],ct2)
    >>> print mdlExp.get_name()
    tintin
    """
    parametersInfo = [ 
        (
            "name",          # parameter name
            STRING,          # parameter type (type)
            lambda:"noname", # callable that returns default value
            "model name"     # parameter description
        ),
        # ...
    ]

    def __init__(self,container,*a,**kwargs):
        DICT.__init__(self)
        self.__id = int(NewModelId(self.__class__))
        self.__container = container
        self.__container.register(self)

        for name,vclass,getDefaultValue,desc in self.parametersInfo:
            if not issubclass(vclass,AType):
                raise Exception("Type parameter '%s'"+ \
                                "must be a subclass of AType"%(name))

            if name in kwargs.keys():
                value=kwargs[name]
            else:
                value=getDefaultValue()

            if isinstance(value,vclass.BaseType):
                b=value
                value=vclass()
                value.setBase(b)

            if not value is None and \
                    not isinstance(value,vclass):
                raise Exception("Type parameter '%s' "%(name)+ \
                                "must be %s "%(vclass))                

            self._baseValue[name]=value
            # create setter & getter
            if issubclass(vclass, AModel):
                setterFn=self.__createSetterAModel(name,vclass,desc)
                getterFn=self.__createGetterAModel(name,vclass,desc)
            else:
                setterFn=self.__createSetterBaseType(name,vclass,desc)
                getterFn=self.__createGetterBaseType(name,vclass,desc)
            # add parameter setter
            setattr(self,"set_"+name,setterFn)
            # add parameter getter
            setattr(self,"get_"+name,getterFn)

    def get_id(self):
        return self.__id
    
    def getContainer(self):
        return self.__container

    def getSubEt(self,*a,**k):
        subEt=AType.getSubEt(self,*a,**k)
        subEt.set("id","%d"%self.__id)
        return subEt

    def populate(self,subEt,*a,**k):
        populateModel=k.get("populateModel",False)
        if populateModel:
            k["populateModel"]=False
            DICT.populate(self, subEt,*a,**k)

    @classmethod
    def fromxmlclass(cls,et,container,*a,**k):
        c_id = int(et.attrib["id"])
        if container.hasModel(c_id,cls,useContext=True):
            mdl=container.getModel(c_id,cls,useContext=True)
        else:
            mdl=DICT.fromxmlclass.__func__(cls,et,container,*a,**k)
            container.registerContext(c_id,mdl)
        return mdl

    def __createSetterAModel(self,name,vclass,desc):      
        @checkTypeParams(vclass)
        def setterFn(value):
            self._baseValue[name]=value
        setterFn.__doc__ = "\n%s\n@param %s:%s\n" % \
                                    (desc,name,vclass)           
        return setterFn

    def __createSetterBaseType(self,name,vclass,desc):      
        @checkTypeParams(vclass.BaseType)
        def setterFn(value):
            self._baseValue[name].setBase(value)
        setterFn.__doc__ = "\n%s\n@param %s:%s\n" % \
                                    (desc,name,vclass.BaseType)           
        return setterFn

    def __createGetterAModel(self,name,vclass,desc):
        @checkTypeReturned(vclass)
        def getterFn():
            return self._baseValue[name]
        getterFn.__doc__ = "\n%s\n@return %s:%s\n" % \
                                    (desc,name,vclass)
        return getterFn
    
    def __createGetterBaseType(self,name,vclass,desc):
        @checkTypeReturned(vclass.BaseType)
        def getterFn():
            return self._baseValue[name].getBase()
        getterFn.__doc__ = "\n%s\n@return %s:%s\n" % \
                                    (desc,name,vclass.BaseType)
        return getterFn

# Atype Registration
RegisterType(AModel)

if __name__ == '__main__':
    import doctest
    doctest.testmod()