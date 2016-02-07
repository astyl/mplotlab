
.. mplotlab documentation master file

MPLOTLAB: Interactive Matplotlib Application using wxPython
==================================================================

.. _wxPython: http://www.wxpython.org/
.. _matplotlib:  http://matplotlib.sourceforge.net/
.. _wxmplot: https://github.com/newville/wxmplot/

**Mplotlab** is an interactive plotting application using `matplotlib`_ and `wxPython`_.
It provides an API that intends to help users to build their own application by leaving them to focus on mastering their data. 

**Mplotlab** is particularly meant to be suitable for **streaming data, real-time processing and interactive visualization**. 
It uses an enhanced graphic animation of matplotlib spoken for interactive application.
It provides nice features such as tweakable data filters and source handlers (*sockets, ...*).

**Mplotlab** engine is based on a figure factory that interprets a mplotlab model parsable in an .xml file.
Thus, it allows GUI users to edit, save and load figures without typing any line of code.

**Mplotlab** is closely modelled on the excellent project `wxmplot`_ developped by Matt Newville

.. image:: images/slide_dynamic_example.gif

.. toctree::
   :maxdepth: 2

   installation
   mplotlab.models
   mplotlab.mpl_builders
   mplotlab.graphics
   mplotlab.utils
   examples