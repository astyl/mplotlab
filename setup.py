#!/usr/bin/env python

from distutils.core import setup

version = "0.1"
long_desc = """
mplotlab is an interactive plotting application using Matplotlib and wxPython.
It provides an API that intends to help users to build their own application
that displays nicely by leaving them to focus on mastering their data. 

mplotlab is particularly meant to be suitable for streaming data, real-time processing and visualization. 
It uses an enhanced graphic animation of matplotlib spoken for interactive application.
It provides nice features such as tweakable data filters and source handlers (sockets, ...).

mplotlab engine is based on a figure factory that interprets a mplotlab model parsable in an .xml file.
Thus, it allows end-users to save and load figures without typing any line of code.

mplotlab is closely modelled on the excellent project 'wxmplot' developped by Matt Newville
https://github.com/newville/wxmplot
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
                  'mplotlab.dataModel',
                  'mplotlab.graphics',
                  'mplotlab.graphics.figureFactory',
                  'mplotlab.graphics.properties',
                  'mplotlab.utils'],
)
