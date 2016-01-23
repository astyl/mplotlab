# -*-coding:Utf-8 -*
from wxPlotLab.utils import checkTypeReturned, checkTypeParams

class AttributeTypes:
    # this class is only used as a simple enumeration
    STRING,COLOR,NDARRAY,INT,FLOAT,MODEL= list(range(6))

class AbcModel(object):
    """ Abstract class representing a model element.
    Use the parameter 'attributeInfos' to auto generate 
    its properties.
    """
    attributeInfos = { 
        # attribute definition
        "name": (                  # attribute name
             str,                  # attribute value instance of
             AttributeTypes.STRING, # attribute type (from enum AttributeTypes)
             "defaultName",        # attribute default value (can be None)
             "name info"           # attribute short description
        ),
    }
    
    def __init__(self,**k):
        for name,infos in self.attributeInfos.items():
            vclass,_,value,desc = infos
            if not isinstance(value,vclass):
                raise Exception("Attribute default value of '%s'"+ \
                                "should be an instance of '%s' "%(name,vclass))
            
            # add attribute (ex: 'self._name')
            setattr(self,"_"+name,value)
            # add attribute setter (ex: 'self.set_name('new_name')')
            setattr(self,"set_"+name,self.__createSetter(name,vclass,desc))
            # add attribute getter (ex: 'self.get_name()')
            setattr(self,"get_"+name,self.__createGetter(name,vclass,desc))
        
        ## Specialisation from dict arguments
        self.update(**k)

    def update(self,**k):
        """ update the model from dict arguments
        ex: self.update(name="toto",size=170)
        """
        for name, value in k.items():
            self.setAttr(name,value)

    def __checkAttrName(self,name):
        if not hasattr(self, "_"+name):
            raise Exception("Attribute %s doesn't exist" % name)

    def setAttr(self,name,value):
        """ set the value of an attribute 
        ex : self.setAttr("name",value)
        """
        self.__checkAttrName(name)
        getattr(self,"set_"+name)(value)

    def getAttr(self,name):
        self.__checkAttrName(name)
        return getattr(self,"get_"+name)()

    def __str__(self):
        msgT = ["[%s]"%self.__class__.__name__]
        msgL = ["%s:%s" % (name,self.getAttr(name))
                                for name in self.attributeInfos.keys()]
        return "\n".join(msgT+msgL)

    def __createSetter(self,name,vclass,desc):
        @checkTypeParams(vclass)
        def setterFn(value):
            return setattr(self,"_"+name,value)
        setterFn.__doc__ = """
{desc}
@param {name} {vclass}
""".format(name=name,vclass=vclass,desc=desc)
        return setterFn
        
    def __createGetter(self,name,vclass,desc):
        @checkTypeReturned(vclass)
        def getterFn():
            return getattr(self,"_"+name)
        getterFn.__doc__ = """
{desc}
@return {name} {vclass}
""".format(name=name,vclass=vclass,desc=desc)
        return getterFn

