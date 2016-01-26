# -*-coding:Utf-8 -*

import unittest
import xml.etree.cElementTree as ET
from wxPlotLab.dataModel import FLOAT,\
                                STRING,\
                                COLOR,\
                                INT,\
                                BOOL
#                                 VECTOR,\
#                                 NDARRAY,\
import numpy as np

class TestAType(unittest.TestCase):
    def test_STRING(self):
        root = ET.Element("root")
        msg = "hello world !"
        STRING.toxml("msg",msg , root)
        mm = ET.tostring(root)
        print mm
        self.assertTrue(mm == """<root><STRING parameter="msg">hello world !</STRING></root>""")
        
        res = STRING.fromxml(root[0])
        print res 
        self.assertTrue(res == msg)
        
    def test_INT(self):
        root = ET.Element("root")
        msg = 78
        INT.toxml("msg",msg , root)
        mm = ET.tostring(root)
        print mm
        self.assertTrue(mm == """<root><INT parameter="msg">78</INT></root>""")
        
        res = INT.fromxml(root[0])
        print res 
        self.assertTrue(res == msg)
        
    def test_FLOAT(self):
        root = ET.Element("root")
        msg = 78.5
        FLOAT.toxml("msg",msg , root)
        mm = ET.tostring(root)
        print mm
        self.assertTrue(mm == """<root><FLOAT parameter="msg">78.5</FLOAT></root>""")
        
        res = FLOAT.fromxml(root[0])
        print res 
        self.assertTrue(res == msg)        

    def test_BOOL(self):
        root = ET.Element("root")
        msg = True
        BOOL.toxml("msg",msg , root)
        mm = ET.tostring(root)
        print mm
        self.assertTrue(mm == """<root><BOOL parameter="msg">1</BOOL></root>""")
        
        res = BOOL.fromxml(root[0])
        print res 
        self.assertTrue(res == msg)

if __name__ == '__main__':
    unittest.main()

