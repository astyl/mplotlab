#!/usr/bin/env python
# coding: utf-8 

import socket
import threading
import time

class DataThread(threading.Thread):
    def __init__(self, clientsocket):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket

    def run(self): 
        self.__count=0
        print "waiting instructions..."
        r = self.clientsocket.recv(2048)
        if r=="waitingForNewData":
            while True:
                self.cbThread()

    def cbThread(self):
        self.clientsocket.send(u"%f "%self.__count)
        self.__count+=1
        # called every 50ms
        time.sleep(0.050)
        
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("localhost", 50981))

print( "Listening...")
tcpsock.listen(10)
print( "Waiting for connection ...")
(clientsocket, (ip, port)) = tcpsock.accept()
newthread = DataThread(clientsocket)
print( "Starting DataThread ...")
newthread.start()
    