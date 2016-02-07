# -*-coding:Utf-8 -*
from mpl_animations import MPL_ArtistAnimation

def buildFigure(figure,slide):
    # Slide
    title = slide.get_title()
    projections = slide.get_projections()
    
    figure.suptitle(title)
    figure.abcModel = slide
    
    animatedArtists = []
    # Projection
    for i,projection in enumerate(projections):
        collections = projection.get_collections()
        xlabel = projection.get_xlabel()
        ylabel = projection.get_ylabel()
        autolim = projection.get_autolim()
        xlim = projection.get_xmin(),projection.get_xmax()
        ylim = projection.get_ymin(),projection.get_ymax()
        
        
        axes = figure.add_subplot(len(projections),1,i+1)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)       

        axes.abcModel = projection
        projection.axes = axes
        
        for collection in collections:
            # Collection
            X = collection.get_X().getVariableData()
            Y = collection.get_Y().getVariableData()
            pL = ["color","linestyle"]
            kw = { k: collection.getAttr(k) \
                                        for k in pL} 
            
            line,=axes.plot(X,Y,**kw)
            line.abcModel = collection
            
            if collection.get_animation():
                animatedArtists.append(line)

        if not autolim:
            axes.set_xlim(xlim)
            axes.set_ylim(ylim)
        else:
            axes.set_xlim()
            axes.set_ylim() 

    if len(animatedArtists)>0:
        if hasattr(figure,"ani"):
            figure.ani._stop()
        figure.ani = MPL_ArtistAnimation(figure, [animatedArtists], interval=100, blit=True,
                                repeat_delay=0)
