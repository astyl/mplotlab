__version__  = '0.2'
__date__     = '08/02/2016'

import sys, wx
try:
    if not hasattr(sys, 'frozen'):
        import wxversion
        wxversion.ensureMinimal('2.9')
except ImportError:
    pass
except:
    pass


# App (singleton)
class App(object):
    __instance = None
    def __new__(cls,*a,**k):
        if cls.__instance is None:
            cls.__instance = App.newApp(*a,**k)
        return cls.__instance

    @staticmethod
    def newApp(*a,**k):
        app = wx.App(*a,**k)
        app.mainWin = newWxPlotFrame()
        app.SetTopWindow(app.mainWin)
        app.mainWin.Show()
        return app

# Utils
from utils import log,\
                  configParser,\
                  msgMap,\
                  createError,\
                  getErrHdlr,\
                  regErrHdlr,\
                  remErrHdlr,\
                  checkTypeParams,\
                  checkTypeReturned

# Models
from mplotlab.models import Slide,\
                      Variable,\
                      Collection,\
                      Projection,\
                      Container

# Graphics
from graphics import newWxPlotFrame,\
                     newWxPlotPanel



