# -*-coding:Utf-8 -*

from systemUtils import checkTypeReturned, checkTypeParams

class AbcModel(object):
    attributes = {
        "name": (str,"string","defaultName","name info"),
    }
    def __init__(self,**k):
        self.__properties = {}
        
        for name,infos in self.attributes.items():
            vtype,propertyInfo,defaultValue,desc = infos
                
            setterFn = self.__createSetter(name,vtype,desc)
            getterFn = self.__createGetter(name,vtype,desc)
            
            self.__properties[name] = propertyInfo 
            setterFn(defaultValue)
            setattr(self,"set_"+name,setterFn)
            setattr(self,"get_"+name,getterFn)
        
        self.update(**k)

    def update(self,**k):
        for name, value in k.items():
            self.setAttr(name,value)
    
    def setAttr(self,name,value):
        getattr(self,"set_"+name)(value)
    
    def getAttr(self,name):
        return getattr(self,"get_"+name)()
        
    def __str__(self):
        msgL = ["[%s]"%self.__class__.__name__]
        msgL.extend([ "%s:%s" % (name,self.getAttr(name))
                                for name in self.attributes.keys()])
        return "\n".join(msgL)
    
    def getProperties(self):
        return self.__properties

    def __createSetter(self,name,vtype,desc):
        @checkTypeParams(vtype)
        def setterFn(value):
            return setattr(self,"__"+name,value)
        setterFn.__doc__ = """
{desc}
@param {name} \a {vtype}
""".format(name=name,vtype=vtype,desc=desc)
        return setterFn
        
    def __createGetter(self,name,vtype,desc):
        @checkTypeReturned(vtype)
        def getterFn():
            return getattr(self,"__"+name)
        getterFn.__doc__ = """
{desc}
@return {name} \a {vtype}
""".format(name=name,vtype=vtype,desc=desc)
        return getterFn

if __name__ == "__main__":
    
    print "# TEST 1"
    
    class TestClass(AbcModel):
        attributes = dict(AbcModel.attributes)
        attributes.update({
            "name2": (str,"string","","info name"),                      
            "paramBool": (bool,"bool",False,"info bool"),                      
            "paramInt": (int,"int",0,"info int"),                      
            "paramFloat": (float,"float",0.,"info float"),                      
            "paramColor": (object,"color","blue","info color"),                      
            "paramTuple": (tuple,"list",tuple(),"info tuple"),                      
            "paramList": (list,"list",list(),"info list"),
        })
   
    tc = TestClass()
    
    
    print tc
    
    print "# TEST 2"
    tc.set_paramFloat(4.5)
    print tc.get_paramFloat() == 4.5
    try:
        tc.set_paramInt(4.6)
    except TypeError as e:
        print e
    
    print "# TEST 3"
    ll = tc.get_paramList()
    ll.append("toto")
    print ll
    print tc.get_paramList()
    
    print "# TEST 4"
    print tc.get_paramTuple.__doc__
    
    print "# TEST 5"
    tc.update(paramBool=True,paramList=["titi"])
    print tc