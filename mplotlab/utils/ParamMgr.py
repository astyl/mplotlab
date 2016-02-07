# -*-coding:Utf-8 -*

from ConfigParser import ConfigParser 
import os

defaultParams={"version":"0.1"}
paramFile = os.path.join(os.path.dirname(__file__),"params.cfg")

configParser = ConfigParser(defaultParams)
configParser.read(paramFile)
        

        