# -*-coding:Utf-8 -*
from matplotlib.backend_bases import NavigationToolbar2

import wx

class Cursors:
    # this class is only used as a simple namespace
    HAND, POINTER, SELECT_REGION, MOVE = list(range(4))
cursors = Cursors()

cursord = {
    cursors.MOVE : wx.CURSOR_HAND,
    cursors.HAND : wx.CURSOR_HAND,
    cursors.POINTER : wx.CURSOR_ARROW,
    cursors.SELECT_REGION : wx.CURSOR_CROSS,
    }

class Navigation(NavigationToolbar2):
    '''
    classdocs
    '''
    def _init_toolbar(self,*args,**kwargs):
        pass
    
    def set_message(self,s):
        from graphics import app
        app.mainWin.GetStatusBar().SetStatusText(s,0)
        
    def set_cursor(self, cursor):
        cursor =wx.StockCursor(cursord[cursor])
        self.canvas.SetCursor( cursor )

    def release(self, event):
        try: del self.lastrect
        except AttributeError: pass

    def dynamic_update(self):
        d = self._idle
        self._idle = False
        if d:
            self.canvas.draw()
            self._idle = True

    def press(self, event):
        if self._active == 'ZOOM':
            self.wxoverlay = wx.Overlay()

    def release(self, event):
        if self._active == 'ZOOM':
            # When the mouse is released we reset the overlay and it
            # restores the former content to the window.
            self.wxoverlay.Reset()
            del self.wxoverlay

    def draw_rubberband(self, event, x0, y0, x1, y1):
        # Use an Overlay to draw a rubberband-like bounding box.

        dc = wx.ClientDC(self.canvas)
        odc = wx.DCOverlay(self.wxoverlay, dc)
        odc.Clear()

        # Mac's DC is already the same as a GCDC, and it causes
        # problems with the overlay if we try to use an actual
        # wx.GCDC so don't try it.
        if 'wxMac' not in wx.PlatformInfo:
            dc = wx.GCDC(dc)

        height = self.canvas.figure.bbox.height
        y1 = height - y1
        y0 = height - y0

        if y1<y0: y0, y1 = y1, y0
        if x1<y0: x0, x1 = x1, x0

        w = x1 - x0
        h = y1 - y0
        rect = wx.Rect(x0, y0, w, h)

        rubberBandColor = '#C0C0FF' # or load from config?

        # Set a pen for the border
        color = wx.NamedColour(rubberBandColor)
        dc.SetPen(wx.Pen(color, 1))

        # use the same color, plus alpha for the brush
        r, g, b = color.Get()
        color.Set(r,g,b, 0x60)
        dc.SetBrush(wx.Brush(color))
        dc.DrawRectangleRect(rect)
        