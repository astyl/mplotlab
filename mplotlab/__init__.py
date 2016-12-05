__version__  = '0.3'
__date__     = '08/12/2016'

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
            cls.__instance = App.__newApp(*a,**k)
        return cls.__instance

    @staticmethod
    def __newApp(*a,**k):
        app = wx.App(*a,**k)
        app.mainWin = newWxPlotFrame()
        app.SetTopWindow(app.mainWin)
        app.mainWin.Show()
        return app
 
# Graphics
from graphics import newWxPlotFrame,\
                     newWxPlotPanel


