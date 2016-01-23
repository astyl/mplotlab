# -*-coding:Utf-8 -*

import numpy as np

# src
from wxPlotLab import newWxPlotApp
from wxPlotLab.dataModel import Variable,\
                                Collection,\
                                Projection,\
                                Slide


# DATA MODEL
slide = Slide(
    name = "slide",
    title = "test title slide ",
)
projections = slide.get_projections()
# projection 1
projection = Projection(
    name = "projection1",
    xlabel = "xlabel projection 1 ",
    ylabel = "ylabel projection 1 ",
    collections = [],
    xmin = 0.,
    xmax = 3.,
    ymin = -1. ,
    ymax  = 1.
)
projections.append(projection)
collections = projection.get_collections()

t = np.arange(0.0,3.0,0.1)
collections.append(Collection(
    name = "collection1",
    X = Variable(data=t),
    Y = Variable(data=np.sin(2*np.pi*t)),
    color = "blue",
    linestyle =  "-",
))
collections.append(Collection(
    name = "collection2",
    X = Variable(data=t),
    Y = Variable(data=np.sin(2*np.pi*(t-.5))),
    color = "green",
    linestyle =  "-",
))


# projection 2
projection = Projection(
    name = "projection2",
    xlabel = "xlabel projection 2 ",
    ylabel = "ylabel projection 2 ",
    collections = [],
    xmin = 0.,
    xmax = 3.,
    ymin = np.exp(0),
    ymax = np.exp(3)
)
projections.append(projection)
collections = projection.get_collections()

t = np.arange(0.0,3.0,0.1)
collections.append(Collection(
    name = "collection3",
    X = Variable(data=t),
    Y = Variable(data=np.exp(t)),
    color = "red",
    linestyle =  "-",
))
print slide
# END

app = newWxPlotApp()
win = app.GetTopWindow()
gp = win.getGraphicPanel()

# SET SLIDE MODEL (GRAPHIC PANEL)
win.setSlide(slide)

# BUILDING ARTISTS IN THE FIGURE
win.build()

# canvas.draw
win.draw()
win.getGraphicCtrl().zoom()

# MAINLOOP
app.MainLoop()
