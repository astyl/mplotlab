# -*-coding:Utf-8 -*

import unittest
from wxPlotLab.dataModel.AbcModel import AbcModel

class TestAbcModel(unittest.TestCase):
    def setUp(self):
        class TestClass(AbcModel):
            attributeInfos = list(AbcModel.attributeInfos)
            attributeInfos.extend([
                ("name2", (str,"string","","info name")),                      
                ("paramBool", (bool,"bool",False,"info bool")),                      
                ("paramInt", (int,"int",0,"info int")),                      
                ("paramFloat", (float,"float",0.,"info float")),                      
                ("paramColor", (object,"color","blue","info color")),                      
                ("paramTuple", (tuple,"list",tuple(),"info tuple")),                      
                ("paramList", (list,"list",list(),"info list")),
            ])
        self.tc = TestClass()
    
    def tearDown(self):
        del self.tc
    
    def test_print(self):
        pp = str(self.tc)
        print pp
        self.assertTrue(pp == """[TestClass]
name:defaultName
name2:
paramBool:False
paramInt:0
paramFloat:0.0
paramColor:blue
paramTuple:()
paramList:[]""")
    
    def test_float(self):
        self.tc.set_paramFloat(4.5)
        print self.tc.get_paramFloat() == 4.5
        try:
            self.tc.set_paramInt(4.6)
        except TypeError as e:
            print e

    def test_getter(self):
        ll = self.tc.get_paramList()
        self.assertTrue(len(ll)==0)
        ll.append("toto")
        self.assertTrue(len(ll)==1)
        self.assertTrue(len(self.tc.get_paramList())==1)
    
    def test_doc(self):
        pp = self.tc.get_paramTuple.__doc__
        print pp
        self.assertTrue(pp == """
info tuple
@return paramTuple <type 'tuple'>
""")
        
    def test_update(self):
        self.tc.update(paramBool=True,paramList=["titi"])
 
if __name__ == '__main__':
    unittest.main()