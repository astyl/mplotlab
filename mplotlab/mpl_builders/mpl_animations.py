# -*-coding:Utf-8 -*

from matplotlib.animation import ArtistAnimation as AA

class MPL_ArtistAnimation(AA):

    def updateArtists(self,artists):
        print "updating artists %s ...."%artists
        for line in artists:
            collection = line.abcModel
            line.set_xdata(collection.get_X().getVariableData())
            line.set_ydata(collection.get_Y().getVariableData())
        return artists

    def _step(self, *a,**k):
        artists = self._framedata[0]
        self.updateArtists(artists)
        AA._step(self,*a,**k)

