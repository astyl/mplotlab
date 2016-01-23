# -*-coding:Utf-8 -*
from matplotlib.lines import Line2D

def buildFigure(figure,slide):
    # Slide
    title = slide.get_title()
    projections = slide.get_projections()
    
    figure.suptitle(title)
    figure.abcModel = slide
    
    # Projection
    for i,projection in enumerate(projections):
        collections = projection.get_collections()
        xlabel = projection.get_xlabel()
        ylabel = projection.get_ylabel()
        xlim = projection.get_xmin(),projection.get_xmax()
        ylim = projection.get_ymin(),projection.get_ymax()
        
        axes = figure.add_subplot(len(projections),1,i+1)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)
        axes.set_xlim(xlim)
        axes.set_ylim(ylim)

        axes.abcModel = projection
        
        for collection in collections:
            # Collection
            X = collection.get_X().get_data()
            Y = collection.get_Y().get_data()
            pL = ["color","linestyle"]
            kw = { k: collection.getAttr(k) \
                                        for k in pL} 
            
            line = Line2D(X,Y,**kw)
            axes.add_line(line)
            
            line.abcModel = collection
            
                