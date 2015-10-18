
import wx.propgrid as wxpg
from matplotlib.lines import Line2D
from PyObjectProperty import PyObjectProperty
from matplotlib.artist import Artist
from matplotlib.axes._base import _AxesBase
from matplotlib.figure import Figure

artistParams = {
    Artist : [  
        ("label",wxpg.StringProperty),
        ("visible",wxpg.BoolProperty),
        ("alpha",wxpg.FloatProperty)
    ],
    Figure : [
        ("dpi",wxpg.IntProperty),
        ("facecolor",wxpg.ColourProperty),
        ("edgecolor",wxpg.ColourProperty),
        ("frameon",wxpg.BoolProperty),
        ("tight_layout",wxpg.BoolProperty),         
    ],
    Line2D : [  
        ("xdata",PyObjectProperty),
        ("ydata",PyObjectProperty),
        ("linewidth",wxpg.FloatProperty),
        ("linestyle",wxpg.StringProperty),
        ("color",wxpg.ColourProperty),
        ("marker",wxpg.StringProperty),
#         ("markevery",wxpg.FloatProperty),
        ("markersize",wxpg.FloatProperty),
        ("markeredgewidth",wxpg.FloatProperty),
        ("markeredgecolor",wxpg.ColourProperty),
        ("markerfacecolor",wxpg.ColourProperty),
        ("markerfacecoloralt",wxpg.ColourProperty),
        ("fillstyle",wxpg.StringProperty),
        ("antialiased",wxpg.BoolProperty),
        ("dash_capstyle",wxpg.StringProperty),
        ("solid_capstyle",wxpg.StringProperty),
        ("dash_joinstyle",wxpg.StringProperty),
        ("solid_joinstyle",wxpg.StringProperty),
        ("pickradius",wxpg.FloatProperty),
        ("drawstyle",wxpg.StringProperty),
    ],
    _AxesBase : [
#         ("adjustable",wxpg.StringProperty),
        ("anchor",wxpg.StringProperty),
        ("aspect",wxpg.StringProperty),
#         ("autoscale_on",wxpg.BoolProperty),
        ("axis_bgcolor",wxpg.ColourProperty),
#         ("axisbelow",PyObjectProperty),
#         ("cursor_props",PyObjectProperty),
        ("frame_on",wxpg.BoolProperty),
#         ("navigate",wxpg.BoolProperty),
#         ("navigate_mode",wxpg.StringProperty),
        ("position",PyObjectProperty),
#         ("sharex",PyObjectProperty),
#         ("sharey",PyObjectProperty),
        ("title",wxpg.StringProperty),
        ("xlabel",wxpg.StringProperty),
        ("xlim",PyObjectProperty),
#         ("xscale",wxpg.StringProperty),
#         ("xticklabels",PyObjectProperty),
#         ("xticks",PyObjectProperty),
        ("ylabel",wxpg.StringProperty),
        ("ylim",PyObjectProperty),
#         ("yscale",wxpg.StringProperty),
#         ("yticklabels",PyObjectProperty),
#         ("yticks",PyObjectProperty),
        
    ]
}