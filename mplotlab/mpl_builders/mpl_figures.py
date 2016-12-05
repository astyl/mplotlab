# -*-coding:Utf-8 -*
from mpl_animations import MPL_ArtistAnimation

def buildFigure(figure,slide):
    # Slide
    title = slide.get_title()
    projections = slide.get_projections()
    aniperiod= slide.get_animation_period()
    figure.suptitle(title)
    figure.abcModel = slide
    
    animatedArtists = []
    # Projection
    for i,projection in enumerate(projections):
        pltmdls = projection.get_plotmodels()
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
        
        for pltmdl in pltmdls:
            mvars=pltmdl.get_variables()
            X = mvars[0].getData()
            Y = mvars[1].getData()
            pL = ["color","linestyle"]
            kw = { k: getattr(pltmdl,"get_"+k)() \
                                        for k in pL} 
            line,=axes.plot(X,Y,**kw)
            line.abcModel = pltmdl
            
            if pltmdl.get_animation():
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
            del figure.ani
        figure.ani = MPL_ArtistAnimation(figure, [animatedArtists], interval=aniperiod,blit=False,
                                repeat_delay=0)
