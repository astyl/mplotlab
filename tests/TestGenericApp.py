# -*-coding:Utf-8 -*

import unittest
import numpy as np
import sys

# src
sys.path.append("../src")

from __init__ import app,figure,gc,gp,win

class Test(unittest.TestCase):

    def testName(self):
        app.run(self.fnTest)

    def fnTest(self):  
        # MATPLOTLIB SCRIPT
        axes = figure.add_subplot(121) 
        t = np.arange(0.0,3.0,0.01)
        s = np.sin(2*np.pi*t)
        s2= np.sin(2*np.pi*(t-.5))
        
        axes.plot(t,s,"blue")
        axes.plot(t,s2,"green")
        
        axes2 = figure.add_subplot(122) 
        axes2.plot(t,np.exp(t),"red")
        # END
        
        # MODE ZOOM (VIA GRAPHIC CONTROLER)
        gc.zoom()
        # DRAW AND DISPLAY (VIA GRAPHIC PANEL)
        win.draw()

if __name__ == "__main__":
    unittest.main()