# -*-coding:Utf-8 -*

import unittest
import xml.etree.cElementTree as ET
from mplotlab.models.abcmodels import AModel
from mplotlab.models.container import Container
from mplotlab.utils.abctypes import STRING,BOOL,COLOR,FLOAT,INT,LIST
from mplotlab.utils.abctypes import RegisterType

import numpy as np

class ClassA(AModel):
    parametersInfo = list(AModel.parametersInfo)
    parametersInfo.extend([
        ("infoA", STRING,lambda:"info","ClassA info"),                     
    ])            
class ClassB(AModel):
    parametersInfo = list(AModel.parametersInfo)
    parametersInfo.extend([
        ("infoB", STRING,lambda:"info","ClassB info"),                     
    ])
class ClassC(ClassB):
    parametersInfo = list(ClassB.parametersInfo)
    parametersInfo.extend([
        ("infoC", STRING,lambda:"info","ClassC info"),                     
    ])
class ClassD(AModel):
    parametersInfo = list(AModel.parametersInfo)
    parametersInfo.extend([
        ("paramBool", BOOL,lambda:False,""),                      
        ("paramInt", INT,lambda:45,""),                      
        ("paramFloat", FLOAT,lambda:1.33,""),                      
        ("paramColor", COLOR,lambda:"blue","color for class D"),                     
        ("paramModel", ClassA,lambda:None,""),                    
        ("paramModelList", LIST,lambda: [],"")
    ])

RegisterType(ClassA)
RegisterType(ClassB)
RegisterType(ClassC)
RegisterType(ClassD)

class TestAModel(unittest.TestCase):
    def setUp(self):
        Container.modelCategories = [ClassA,ClassB,ClassD]
        Container.categoryLabels = ["classA","classB","classD"]
        self.__container=Container()
        oA = ClassA(self.__container,name="instanceA")
        oB = ClassB(self.__container,name="instanceB")
        oC = ClassC(self.__container,name="instanceC")
        oD = ClassD(self.__container,name="instanceD",
                    paramModel=oA,
                    paramModelList=[oB,oC])
        self.INST = (oA,oB,oC,oD)

    def tearDown(self):
        del self.INST
        del self.__container

    def test_print(self):
        oD = self.INST[3]
        print oD
      
    def test_float(self):
        oD = self.INST[3]
        oD.set_paramFloat(4.5)
        self.assertTrue(oD.get_paramFloat() == 4.5)
        try:
            oD.set_paramInt(4.6)
        except TypeError as e:
            self.assertTrue(\
"""TypeError:expected <type 'int'>, got <type 'float'>""" in str(e))
  
    
    def test_getter(self):
        oD = self.INST[3]
        ll = oD.get_paramModelList()
        self.assertTrue(len(ll)==2)
        del ll[1]
        self.assertTrue(len(ll)==1)
        self.assertTrue(len(oD.get_paramModelList())==1)
        
    def test_doc(self):
        oD = self.INST[3]
        pp = oD.get_paramColor.__doc__
        print pp
        self.assertTrue(pp == """
color for class D
@return paramColor:<type 'str'>
""")
            
    def test_update(self):
        oD = self.INST[3]
        oD.set_paramBool(True)
        oD.set_paramInt(95)
        self.assertTrue(oD.get_paramBool()==True)
        self.assertTrue(oD.get_paramInt()==95)
          
    def test_toxml(self):
        self.__container.toxml("toto.xml")

    def test_fromxml(self):
        self.__container.flush()
        self.__container.fromxml("toto2.xml")
        self.__container.toxml("toto3.xml")

if __name__ == '__main__':
    unittest.main()


