# -*-coding:Utf-8 -*
from Logger import log

msgMap = {}
errHdlrs = {}

def createError(key="",args={},exception=None):
    kw = {
        "msg": msgMap.get(key,"Error"),
        "args":args,
        "exception":exception,
    }
    return Error(**kw)

def getErrHdlr(name=None):
    return errHdlrs.get(name,ErrorHdlr())

def regErrHdlr(name,errHdlr):
    errHdlrs[name]=errHdlr  

def remErrHdlr(name):
    if name in errHdlrs.keys():
        del errHdlrs[name]
    
class ErrorHdlr(object):
    __slots__ = ['__errors']
    def __init__(self):
        self.__errors = []

    def handle(self,err):
        self.__errors.append(err)
        log.error(err)
        
    def check(self):
        return len(self.__errors)==0
    
class Error(object):
    __slots__ = ['__msg','__args','__exception']
    def __init__(self,msg="",args={},exception=None):
        self.__msg = msg
        self.__args = args
        self.__exception = exception
        
    def __str__(self):
        msg = self.__msg.format(**self.__args)
        if not self.__exception is None:
            msg += "- " + repr(self.__exception)
        return msg 
    
    def __repr__(self):
        return self.__str__()
