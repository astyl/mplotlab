# -*-coding:Utf-8 -*

# Logger
from Logger import log
log = log
# Application
from GenericApp import GenericApp
app = GenericApp()
# Main Window
win = app.mainWin
# Graphic Panel (wx.Panel with matplotlib canvas & figure)
gp = app.mainWin.getGraphicPanel()
# Graphic Control ( zoom/pan)
gc = app.mainWin.getGraphicCtrl()
# Matplotlib Canvas
canvas = gp.getCanvas()
# Matplotlib Figure
figure = gp.getFigure()

