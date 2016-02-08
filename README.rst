MPLOTLAB: Interactive Matplotlib Application using wxPython
===========================================================
.. warning::
The project has just come out from the prototype phase and still needs a lot of hard work to meet its promise ! 

Description
-----------
.. _wxPython: http://www.wxpython.org/
.. _matplotlib:  http://matplotlib.sourceforge.net/
.. _wxmplot: https://github.com/newville/wxmplot/

Mplotlab is an interactive plotting application using `matplotlib`_ and `wxPython`_.
It provides an API that intends to help users to build their own application by leaving them to focus on mastering their data. 

Mplotlab is particularly meant to be suitable for **streaming data, real-time processing and interactive visualization**. 
It uses an enhanced graphic animation of matplotlib spoken for interactive application.
It provides nice features such as tweakable data filters and source handlers (*sockets, ...*).

Mplotlab engine is based on a figure factory that interprets a mplotlab model parsable in an .xml file.
Thus, it allows GUI users to edit, save and load figures without typing any line of code.

Mplotlab is closely modelled on the excellent project `wxmplot`_ developped by Matt Newville.

Demo
----

Animated slides (T=1s) receiving simply the time from a tcp/ip socket (T=50ms) and plotting the transformations cosinus, sinus, and tangent.

.. image:: https://raw.githubusercontent.com/astyl/mplotlab/master/doc/images/slide_dynamic_example.gif

Documentation
-------------
.. _here:: http://pythonhosted.org/mplotlab/

Documentation is avaible  `here`_.


Contacts
--------

Contributors are welcome :) !
André ASTYL
andreastyl@gmail.com
