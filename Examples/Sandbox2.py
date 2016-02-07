# -*-coding:Utf-8 -*

import numpy as np

# src
from mplotlab import App
from mplotlab.dataModel import Source,SourceExpression,SourceSocket,\
                                Variable,\
                                Collection,\
                                Projection,\
                                Slide

# DATA MODEL
def makeSlide(sourceT):
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

    collections.append(Collection(
        name = "collection1",
        animation=True,
        X = Variable(source=sourceT),
        Y = Variable(formula="sin(2*pi*T)"),
        color = "blue",
        linestyle =  "-",
    ))
    collections.append(Collection(
        name = "collection2",
        animation=True,
        X = Variable(source=sourceT),
        Y = Variable(formula="sin(2*pi*(T-0.5))"),
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
    
    collections.append(Collection(
        animation=True,
        name = "collection3",
        X = Variable(source=sourceT),
        Y = Variable(formula="exp(T)"),
        color = "red",
        linestyle =  "-",
    ))
    return slide

app = App()
# SET SLIDE MODEL
# sourceT= SourceSocket(name="T",
#                       host="localhost",
#                       port=50981,
#                       buffsize=9999999,
#                       period=50) 
# slide = makeSlide(sourceT)
# slide2 = makeSlide(sourceT)
# slide2.set_name("ee")
# app.mainWin.showSlide(slide)
# app.mainWin.showSlide(slide2)
# GO :) 
app.MainLoop()
