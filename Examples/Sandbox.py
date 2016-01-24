# -*-coding:Utf-8 -*

import numpy as np

# src
from wxPlotLab import App
from wxPlotLab.dataModel import Variable,\
                                Collection,\
                                Projection,\
                                Slide

# DATA MODEL
def makeSlide():
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
    return slide


app = App()
# SET SLIDE MODEL
slide = makeSlide()
slide2 = makeSlide()
slide2.set_name("ee")
print slide
app.mainWin.showSlide(slide)
app.mainWin.showSlide(slide2)
# GO :) 
app.MainLoop()
