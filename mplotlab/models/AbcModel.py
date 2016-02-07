# -*-coding:Utf-8 -*
from mplotlab.utils import checkTypeReturned, checkTypeParams
from copy import copy

from AbcType import AType,STRING#,VECTOR

def NewModelId():
    res = NewModelId.id
    NewModelId.id +=1
    return res
NewModelId.id=0

class AbcModel(AType):
    """ 
    Abstract class representing a model element.
    For derived class, use the parameter 'attributeInfos' to auto generate 
    its properties 
    """
    __id = None 
    attributeInfos = [ 
        # attribute definition
        ("name", (                  # attribute name
             str,                  # attribute value instance of
             STRING,               # attribute type 
             "",        # attribute default value (can be None)
             "name info"           # attribute short description
        )),
    ]
    
    def __init__(self,**k):
        self.__id = k.pop("__id_serialized",NewModelId())
        self.__container = k.pop("container",None)
        try: self.__container.register(self)
        except: pass
        self.__properties = {}
        for name,infos in self.attributeInfos:
            vclass,vtype,value,desc = infos
            if not isinstance(value,vclass):
                raise Exception("Attribute default value of '%s'"+ \
                                "should be an instance of '%s' "%(name,vclass))
            
            # add attribute (ex: 'self._name')
            setattr(self,"_"+name,copy(value))
            # add attribute setter (ex: 'self.set_name('new_name')')
            setattr(self,"set_"+name,self.__createSetter(name,vclass,desc))
            # add attribute getter (ex: 'self.get_name()')
            setattr(self,"get_"+name,self.__createGetter(name,vclass,desc))
            # add attribute type 
            self.__properties[name] = vtype
        ## Specialisation from dict arguments
        self.update(**k)

    def get_container(self):
        return self.__container

    def _set_container(self,container):
        self.__container=container

    def get_id(self):
        return self.__id

    @staticmethod
    def getSubEt(clsname,parameter,model,et,**attr):
        return AType.getSubEt(clsname,parameter,model,et,
                              id=str(model.get_id()),
                              name=model.get_name(),
                              **attr)

    @classmethod
    def populate(cls,parameter,self,subEt,parseModel=False):
        if parseModel:
            for name,aType in self.__properties.items():
                value = self.getAttr(name)
                aType.toxml(name,value,subEt,parseModel=False)

    @classmethod
    def fromxml(cls, et, **k):
        container = k.get("container")
        name = et.tag
        m_id = int(et.attrib.get("id"))
        if container.hasModel(m_id):
            return container.getModel(m_id)
        else:
            infos = {name:vType for name,(_,vType,_,_) in cls.attributeInfos}
            params = {"__id_serialized":m_id}
            for subEt in et:
                name = subEt.attrib["parameter"]
                vType = infos[name]
                params[name] = vType.fromxml(subEt, **k)
            new_model = cls(**params)
            return new_model

    def getProperties(self):
        return self.__properties

    def update(self,**k):
        """ 
        update the model from dict arguments
        ex: self.update(name="toto",size=170)
        """
        for name, value in k.items():
            self.setAttr(name,value)

    def __checkAttrName(self,name):
        if not hasattr(self, "_"+name):
            raise Exception("Attribute %s doesn't exist" % name)

    def setAttr(self,name,value):
        """ 
        set the value of an attribute 
        ex : self.setAttr("name",value)
        """
        self.__checkAttrName(name)
        getattr(self,"set_"+name)(value)

    def getAttr(self,name):
        self.__checkAttrName(name)
        return getattr(self,"get_"+name)()

    def __str__(self,it=""):
        m_id = self.get_id()
        msgT = [it+"[%s] ID:%d"%(self.__class__.__name__,m_id)]
        msgL = []
        for name,(_,vType,_,_) in self.attributeInfos:
            value = self.getAttr(name)
            if issubclass(vType, AbcModel):
                value = value.__str__(it+"\t")
            elif issubclass(vType, MODELS):
                sep = "\n"+it+"\t"+"-"*25
                value = sep.join(\
                     map(lambda x:x.__str__(it+"\t"),value)\
                     +["\n"]\
                     )
            msgL.append(it+"%s:%s" % (name,value))
        return "\n"+"\n".join(msgT+msgL)

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

class MODELS(AType):
    typeClass = AbcModel
    containerStaticClass = None #Container to init

    @classmethod
    def populate(cls,name,abcModels,subEt,**k):
        for i,model in enumerate(abcModels):
            modelClass = model.__class__
            if not issubclass(modelClass,cls.typeClass):
                raise Exception()
            modelClass.toxml(name+"%d"%i,model,subEt,**k)

    @classmethod
    def fromxml(cls,et,**k):
        res=[]
        for subEt in et:
            modelClass = cls.containerStaticClass.getAType(subEt.tag)
            res.append(modelClass.fromxml(subEt,**k))
        return res
