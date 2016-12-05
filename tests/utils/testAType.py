# -*-coding:Utf-8 -*

import unittest
from mplotlab.utils.abctypes import LIST,\
                                    STRING,\
                                    COLOR,\
                                    INT,\
                                    BOOL
import numpy as np 

class TestAType(unittest.TestCase):

    def test_LIST(self):
        ali = LIST()
        l = ali.getBase()
        l.append(BOOL(False))
        l.append(INT(36))
        msg=ali.tostringxml("mylist")
        msgRef=\
        """<root><mylist type="LIST">"""+\
            """<elem type="BOOL">0</elem>"""+\
            """<elem type="INT">36</elem>"""+\
        """</mylist></root>"""

        self.assertEqual(msgRef, msg)

if __name__ == '__main__':
    unittest.main()

