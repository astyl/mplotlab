# -*-coding:Utf-8 -*

## logger
from Logger import log
## params
from ParamMgr import configParser
## error handler
from ErrorMgr import msgMap,\
                     createError,\
                     getErrHdlr,\
                     regErrHdlr,\
                     remErrHdlr


def checkTypeParams(*aTypes,**kTypes):
    def deco(fn):
        def fn2(*args,**kwargs):
            # [*] 
            for a,aType in zip(args,aTypes):
                if not isinstance(a,aType):
                    raise TypeError(u"TypeError:expected %s, got %s"\
                                            % (aType, type(a)))
            # [**]
            for param,val in kwargs.items():
                if kTypes.has_key(param) and \
                        not isinstance(val,kTypes[param]):
                    raise TypeError(u"TypeError[%s]:expected %s, got %s"\
                                            % (param,kTypes[param], type(val)))
            return fn(*args,**kwargs)
        return fn2
    return deco    

def checkTypeReturned(*aTypes):
    def deco(fn):
        def fn2(*args,**kwargs):
            res = fn(*args,**kwargs)
            if isinstance(res,(list,tuple)):
                if len(aTypes)>0 and isinstance(res,aTypes[0]):
                    return res
                else:
                    resT = res
            else:
                resT = res,

            for r,aType in zip(resT,aTypes):
                if not isinstance(r,aType):
                    raise TypeError("TypeError:expected %s, got %s"\
                                            % (aType, type(r)))
            return res
        return fn2
    return deco    

            
if __name__ == "__main__":
    
    print "# TEST 1"
    log.info("test")
    
    print "# TEST 2"
    msgMap["errId_1"]="Test error with the var '{var}'"
    err = createError(key="errId_1", 
                      args={"var":"alpha"}, 
                      exception=EnvironmentError())
    log.error(err)
    
    print "# TEST 3"
    log.warn("Current version is %s "%configParser.get("DEFAULT","version"))
    
    print "# TEST 4"
    @checkTypeParams(int,lola = int)
    @checkTypeReturned(str,int,dict)
    def testMethod(nb,lola= 1):
        res = lola+nb
        return "%f"%res,res,{"res":res}
    
    print testMethod(9,lola=3)
    try:
        testMethod(lola="5")
    except TypeError as e:
        print e

    
    