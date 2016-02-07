# -*-coding:Utf-8 -*

from AbcModel import AbcModel 
from AbcType import AType,STRING,INT
import numpy as np
import socket
import wx

class NDARRAY(AType):
    @classmethod
    def toxml(*a,**k):
        """ 
        values aren't serialized as any parameter.
        They are generated from source handlers such as
        expression, files or remote data streams
        """
        pass
    @classmethod
    def fromstring(*a,**k):
        return np.array([])

class Source(AbcModel):
    attributeInfos = list(AbcModel.attributeInfos)
    attributeInfos.extend([
        ("values", (np.ndarray,NDARRAY,np.array([]),"values to address to many variables")),
    ])
    def __init__(self,*a,**k):
        AbcModel.__init__(self,*a,**k)
        self.__init = False
        
    def init(self):
        self.__init = True

    def stop(self):
        self.__init = False

    def isInit(self):
        return self.__init

    def getSourceData(self):
        if not self.isInit():
            self.init()
        return self.get_values().copy()

class SourceExpression(Source):
    attributeInfos = list(Source.attributeInfos)
    attributeInfos.extend([
        ("expression", (str,STRING,"","expression that returns a numpy array")),
    ])

    def init(self):
        """ Initialize values """
        values = eval(self.get_expression())
        self.set_values(values)
#         Source.init(self)

class SourceSocket(Source):
    attributeInfos = list(Source.attributeInfos)
    attributeInfos.extend([
        ("host", (str,STRING,"localhost","host used to configure the socket connection")),
        ("port", (int,INT,50981,"host used to configure the socket connection")),
        ("buffsize",(int,INT,9999999,"buffer size")),
        ("period",(int,INT,50,"polling period in ms"))
    ])

    def __init__(self,*a,**k):
        Source.__init__(self,*a,**k)
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def init(self):
        """ Initialize values """
        
        host = self.get_host()
        port = self.get_port()
        print "connecting %s:%d ..." %(host,port)
        try:
            self.__socket.connect((host, port))    
        except Exception as e:
            print e
            print "connection failed..."
            print "couldn't update source %s"%self.get_name()
        # start the data stream
        Source.init(self)
        wx.CallLater(10,self.cbThread)
       
    def cbThread(self):
        if self.isInit():
            print "SENDING READY FOR RECEPTION"
            try:
                self.__socket.send("giveMeYourData")
            except Exception as e:
                print "REATTEMPTING ..."
                wx.CallLater(1000,self.cbThread)
                return
            print "WAITING FOR MESSAGE"
            message = self.__socket.recv(self.get_buffsize())
            print "PROCESSING MESSAGE"
            self.handleMessage(message)
            wx.CallLater(self.get_period(),self.cbThread)
        else:
            print "SOURCE CALLBACK STOPPED"

    def handleMessage(self,message):
        old_values = self.get_values()
        value_received = float(message)
        new_values = np.append(old_values,value_received)
        self.set_values(new_values)
