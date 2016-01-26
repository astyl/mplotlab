# -*-coding:Utf-8 -*

import unittest
from wxPlotLab.dataModel import Container,\
                                Variable,\
                                Collection,\
                                Projection,\
                                Slide
                                

class TestContainer(unittest.TestCase):
    
    def test_container(self):        
        cc = Container()
        v1 = Variable(name="v1")
        cc.register(v1)

        dump1 = str(cc)
        print cc
        cc.toxml("toto2.xml")
          
        cc = Container()
        cc.fromxml("toto2.xml")
        dump2 = str(cc)
        print cc
        self.assertTrue(dump1==dump2)
 
    def test_container2(self):
        cc = Container()
        v1 = Variable(name="v1")
        v2 = Variable(name="v2")
        v3 = Variable(name="v3")
        v4 = Variable(name="v4")
        v5 = Variable(name="v5")
        c1 = Collection(name="c1",X=v1,Y=v2)
        c2 = Collection(name="c2",X=v1,Y=v3)
        c3 = Collection(name="c3",X=v1,Y=v4)
        c4 = Collection(name="c4",X=v1,Y=v5)
        p1 = Projection(name="p1",collections=[c1])
        p2 = Projection(name="p2",collections=[c1,c2])
        p3 = Projection(name="p3",collections=[c1,c2,c3])
        s1 = Slide(name="s1",projections=[p1])
        s2 = Slide(name="s2",projections=[p2])
        s3 = Slide(name="s3",projections=[p1,p2])
          
        cc.register(v1)
        cc.register(v2)
        cc.register(v3)
        cc.register(v4)
        cc.register(v5)
        cc.register(c1)
        cc.register(c2)
        cc.register(c3)
        cc.register(c4)
        cc.register(p1)
        cc.register(p2)
        cc.register(p3)
        cc.register(s1)
        cc.register(s2)
        cc.register(s3)
        self.assertTrue(len(cc.getSlides())==3)
        self.assertTrue(len(cc.getProjections())==3)
        self.assertTrue(len(cc.getCollections())==4)
        self.assertTrue(len(cc.getVariables())==5)
           
        dump1 = str(cc)
        cc.toxml("toto3.xml")
           
        cc = Container()
        cc.fromxml("toto3.xml")
        dump2 = str(cc)
         
        print dump1
        self.assertTrue(dump1==dump2)


if __name__ == '__main__':
    unittest.main()