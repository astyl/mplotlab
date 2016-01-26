# -*-coding:Utf-8 -*

import unittest
import xml.etree.cElementTree as ET
from wxPlotLab.dataModel import AbcModel,\
                                FLOAT,\
                                MODELS,\
                                STRING,\
                                COLOR,\
                                INT,\
                                BOOL,\
                                AtypeRegister
import numpy as np

class TestAbcModel(unittest.TestCase):
    def setUp(self):
        class ClassA(AbcModel):
            attributeInfos = list(AbcModel.attributeInfos)
            attributeInfos.extend([
                ("infoA", (str,STRING,"ClassA info","")),                     
#                 ("array",(np.ndarray,NDARRAY,np.arange(10),"array info"))                   
            ])            
        class ClassB(AbcModel):
            attributeInfos = list(AbcModel.attributeInfos)
            attributeInfos.extend([
                ("infoB", (str,STRING,"ClassB info","")),                     
            ])
        class ClassC(ClassB):
            attributeInfos = list(ClassB.attributeInfos)
            attributeInfos.extend([
                ("infoC", (str,STRING,"ClassC info","")),                     
            ])
        oA = ClassA(name="instanceA")
        oB = ClassB(name="instanceB")
        oC = ClassC(name="instanceC")
        class ClassD(AbcModel):
            attributeInfos = list(AbcModel.attributeInfos)
            attributeInfos.extend([
                ("paramBool", (bool,BOOL,False,"")),                      
                ("paramInt", (int,INT,45,"")),                      
                ("paramFloat", (float,FLOAT,1.33,"")),                      
                ("paramColor", (str,COLOR,"blue","color for class D")),                     
                ("paramModel", (ClassA,ClassA,oA,"")),                    
                ("paramModelList", (list,MODELS,[oB,oC],""))
            ])
        oD = ClassD(name="instanceD")
        self.INST = (oA,oB,oC,oD)
        self.CLASSES = {o.__class__.__name__:o.__class__ for o in self.INST}
    
    def tearDown(self):
        del self.INST
        del self.CLASSES
    
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
@return paramColor <type 'str'>
""")
           
    def test_update(self):
        oD = self.INST[3]
        oD.update(paramBool=True,paramInt=95)
        self.assertTrue(oD.get_paramBool()==True)
        self.assertTrue(oD.get_paramInt()==95)
         
  
    def test_xml(self):
         
        root = ET.Element("root")
         
         
        for o in self.INST:
            o.__class__.toxml(o.get_name(),o,root,parseModel=True)
            xmlstr =  ET.tostring(root)
            print xmlstr
  
        tree = ET.ElementTree(root)
        tree.write("toto.xml")
        #########"
        tree = ET.ElementTree(file='toto.xml')
        root = tree.getroot()
          
        class DumbContainer(object):
            dico = {}
            def getModel(self,mid):
                return self.dico[mid]
            def hasModel(self,mid): 
                return self.dico.has_key(mid)
            def register(self,model):
                self.dico[model.get_id()]=model

        container = DumbContainer()
        AtypeRegister.registerAType(*self.CLASSES.values())
        for et in root:
            CModel = self.CLASSES[et.tag]
            model = CModel.fromxml(et,container=container)
            container.register(model)
          
        for l in container.dico.values():
            print l

if __name__ == '__main__':
    unittest.main()


