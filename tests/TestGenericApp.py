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
        axes = figure.add_subplot(111) 
        t = np.arange(0.0,3.0,0.01)
        s = np.sin(2*np.pi*t)
        axes.plot(t,s)
        # END
        
        # MODE ZOOM (VIA GRAPHIC CONTROLER)
        gc.zoom()
        # DRAW AND DISPLAY (VIA GRAPHIC PANEL)
        win.draw()

if __name__ == "__main__":
    unittest.main()