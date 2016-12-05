# -*-coding:Utf-8 -*
from mplotlab import App
from mplotlab.models.container import Container
from mplotlab.models.sources import SourceSocket,SourceExpression
from Sandbox import addSlides

def addSources(container):
    # Here, I create and configure a socket source that will 
    # accept a client/server TCP communication.
    SourceSocket(container,name="T",
                          host="localhost",
                          port=50981,
                          buffsize=9999999,
                          period=500) 
    SourceExpression(container, name="K",
        expression="25",         
    )
 
if __name__ == '__main__':
    # Create the mplotlab application
    app = App()    
    # Create models stored in container
    container=app.mainWin.getContainer()
    addSources(container)
    addSlides(container)
    # Update animation
    plotModels=container.getPlotModels()
    for pmdl in plotModels:
        pmdl.set_animation(True)    
    # launch
    app.mainWin.showSlide()
    app.MainLoop()
