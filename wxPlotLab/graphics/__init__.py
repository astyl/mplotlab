# -*-coding:Utf-8 -*

import wx

# Plot Panel
from GraphicPanel import GraphicPanel
def newWxPlotPanel(parent):
    return GraphicPanel(parent)

# Plot Frame
from MainWin import MainWin
def newWxPlotFrame():
    return MainWin()

# Plot App
def newWxPlotApp():
    app = wx.App()
    frame = newWxPlotFrame()
    app.SetTopWindow(frame)
    frame.Show()
    return app