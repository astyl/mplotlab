# -*-coding:Utf-8 -*

import numpy as np

# src
from mplotlab import App
from mplotlab.dataModel import Source,SourceExpression,\
                                Variable,\
                                Collection,\
                                Projection,\
                                Slide

# DATA MODEL
def makeSlide(source):
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
        X = Variable(source=source),
        Y = Variable(formula="sin(2*pi*T)"),
        color = "blue",
        linestyle =  "-",
    ))
    collections.append(Collection(
        name = "collection2",
        X = Variable(source=source),
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
        name = "collection3",
        X = Variable(source=source),
        Y = Variable(formula="exp(T)"),
        color = "red",
        linestyle =  "-",
    ))
    return slide


app = App()
# SET SLIDE MODEL  
# sourceT= SourceExpression(name="T",expression="np.arange(0.0,3.0,0.1)")
# slide = makeSlide(sourceT)
# slide2 = makeSlide(sourceT)
# slide2.set_name("slide 2")
# print slide
# app.mainWin.showSlide(slide)
# app.mainWin.showSlide(slide2)
# # GO :) 
app.MainLoop()
