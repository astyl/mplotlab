# -*-coding:Utf-8 -*
from mplotlab import App
from mplotlab.models.container import Container
from mplotlab.models.sources import SourceExpression
from mplotlab.models.variables import Variable
from mplotlab.models.plotmodels import Line2D
from mplotlab.models.projections import Projection2D
from mplotlab.models.slides import Slide

# DATA MODEL
def addSources(container):
    SourceExpression(container, name="T",
        expression="arange(0,100)",         
    )
    SourceExpression(container, name="K",
        expression="25",         
    )
def addSlides(container):
    varX=Variable(container, name="X", 
        formula="T"
    )
    varY1=Variable(container, name="Y", 
        formula="sin(2*pi*T/K)"
    )
    varY2=Variable(container, name="Y", 
        formula="cos(2*pi*T/K)"
    )
    lines_1=Line2D(container, name="sin",
        variables=[varX,varY1],
        color="blue",
        linestyle="-"
    )
    lines_2=Line2D(container, name="cos",
        variables=[varX,varY2],
        color="red",
        linestyle=":"
    )
    proj = Projection2D(container, name= "proj",
        plotmodels=[lines_1,lines_2]
    )
    slide0 = Slide(container, name = "slide",
        projections=[proj],
        title = "test slide title",
    )

if __name__ == '__main__':
    # Create the mplotlab application
    app = App()    
    # Create models stored in container
    container=app.mainWin.getContainer()
    addSources(container)
    addSlides(container)
    # launch
    app.mainWin.showSlide()
    app.MainLoop()

