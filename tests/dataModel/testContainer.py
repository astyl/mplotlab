# -*-coding:Utf-8 -*

import unittest
from wxPlotLab.dataModel.Container import Container,\
                                    Variable,\
                                    Collection,\
                                    Projection,\
                                    Slide

class TestContainer(unittest.TestCase):
    def test_container(self):
        cc = Container()
        s1 = Slide(name="s1")
        s2 = Slide(name="s2")
        p1 = Projection(name="p1")
        p2 = Projection(name="p2")
        c1 = Collection(name="c1")
        c2 = Collection(name="c2")
        v1 = Variable(name="v1")
        v2 = Variable(name="v2")
        
        cc.register(s1)
        cc.register(s2)
        cc.register(p1)
        cc.register(p2)
        cc.register(c1)
        cc.register(c2)
        cc.register(v1)
        cc.register(v2)
        
        self.assertTrue(len(cc.getSlides())==2)
        self.assertTrue(len(cc.getProjections())==2)
        self.assertTrue(len(cc.getCollections())==2)
        self.assertTrue(len(cc.getVariables())==2)
        
        cc.delete(s1)
        self.assertTrue(len(cc.getSlides())==1)
        cc.delete(p1)
        self.assertTrue(len(cc.getProjections())==1)
        cc.delete(c1)
        self.assertTrue(len(cc.getCollections())==1)
        cc.delete(v1)
        self.assertTrue(len(cc.getVariables())==1)
        
        cc.flush()
        self.assertTrue(len(cc.getSlides())==0)
        self.assertTrue(len(cc.getProjections())==0)
        self.assertTrue(len(cc.getCollections())==0)
        self.assertTrue(len(cc.getVariables())==0)
        

if __name__ == '__main__':
    unittest.main()