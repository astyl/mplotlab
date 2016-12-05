# -*-coding:Utf-8 -*

from abcmodels import AModel
from mplotlab.utils.abctypes import STRING,INT,RegisterType
import socket
from numpy import *

class ASource(AModel):
    CallLater=None 
        # wx.CallLater(time_in_ms,callable)
    
    def __init__(self,*a,**k):
        AModel.__init__(self,*a,**k)
        self._refresh=False
        self._dataFrozen=None

    def init(self,*a,**k):
        pass

    def start(self,*a,**k):
        pass

    def stop(self,*a,**k):
        pass

    def _compute(self,*a,**k):
        return []

    def getData(self,*a,**k):
        if not self._refresh:
            self._dataFrozen=self._compute(*a,**k)
            self._refresh=True
        return self._dataFrozen

class SourceExpression(ASource):
    parametersInfo = list(ASource.parametersInfo)
    parametersInfo.extend([
        ("expression",STRING,lambda:"array([])","values to address to many variables"),
    ])
    def _compute(self,*a,**k):
        return eval(self.get_expression(),globals())

class SourceSocket(ASource):
    parametersInfo = list(ASource.parametersInfo)
    parametersInfo.extend([
        ("host", STRING,lambda:"localhost","host used to configure the socket connection"),
        ("port", INT,lambda:50981,"host used to configure the socket connection"),
        ("buffsize",INT,lambda:9999999,"buffer size"),
        ("period",INT,lambda:500,"polling period in ms")
    ])

    def __init__(self,*a,**k):
        ASource.__init__(self,*a,**k)
        self._values = array([])
        self._messages = []
        self.__socket = None
        self.__stop = None

    def init(self,*a,**k):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        name = self.get_name()
        host = self.get_host()
        port = self.get_port()
        print "(%s) connecting %s:%d ..." %(name,host,port)
        self.__socket.connect((host, port))    
        print "(%s) connecting %s:%d ... OK" %(name,host,port)
        ASource.init(self,*a,**k)

    def start(self,*a,**k):
        self.__socket.send("waitingForNewData")
        self.__stop = False
        self._values = array([])
        self._messages = []
        ASource.CallLater(self.get_period(),self.cbThread)
        ASource.start(self,*a,**k)

    def stop(self,*a,**k):
        self.__stop = True
        ASource.stop(self,*a,**k)

    def cbThread(self):
        if not self.__stop:
            message = self.__socket.recv(self.get_buffsize())
            self._messages.extend(message.split())
            self._refresh=False
            ASource.CallLater(self.get_period(),self.cbThread)

    def _compute(self):
        #new_values=fromstring(msgs,dtype=int)
        if len(self._messages)>0:
            new_values=array(self._messages)
            new_values = new_values.astype(float)
            self._values=append(self._values,new_values)
            self._messages=[]
        return self._values

# Atype Registration
RegisterType(ASource)
RegisterType(SourceExpression)
RegisterType(SourceSocket)
