# -*-coding:Utf-8 -*

from matplotlib.animation import ArtistAnimation as AA

class MPL_ArtistAnimation(AA):

    def updateArtists(self,artists):
        for line in artists:
            pltmdl = line.abcModel
            mvars=pltmdl.get_variables()
            line.set_xdata(mvars[0].getData())
            line.set_ydata(mvars[1].getData())
        return artists

    def _step(self, *a,**k):
        artists = self._framedata[0]
        self.updateArtists(artists)
        AA._step(self,*a,**k)

