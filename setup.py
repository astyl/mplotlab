#!/usr/bin/env python

from setuptools import setup

version = "0.2"
long_desc = """
MPLOTLAB: Interactive Matplotlib Application using wxPython
==================================================================

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

Mplotlab is closely modelled on the excellent project `wxmplot`_ developped by Matt Newville

.. image:: https://raw.githubusercontent.com/astyl/mplotlab/master/doc/images/slide_dynamic_example.gif
"""


setup(name = 'mplotlab',
      version = version,
      author = 'Andre ASTYL',
      author_email = 'andreastyl@gmail.com',
      download_url = 'http://github.com/astyl/mplotlab/',
      requires     = ('wx', 'numpy', 'matplotlib'),
      license      = 'MIT License',
      description  = 'Interactive Matplotlib Application using wxPython',
      long_description = long_desc,
      platforms = ('Windows', 'Linux', 'Mac OS X'),
      classifiers=['Intended Audience :: Science/Research',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Visualization'],
      packages = ['mplotlab',
                  'mplotlab.models',
                  'mplotlab.mpl_builders',
                  'mplotlab.graphics',
                  'mplotlab.utils'],
)
