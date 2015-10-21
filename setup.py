#!/usr/bin/env python

from setuptools import find_packages
from distutils.core import setup

version = "0.1"
long_desc = ''''''


setup(name = 'wxPlotLab',
      version = version,
      author = 'Andre ASTYL',
      author_email = 'andreastyl@gmail.com',
      download_url = 'http://github.com/astyl/wxPlotLab/',
      requires     = ('wx', 'numpy', 'matplotlib'),
      license      = 'MIT License',
      description  = 'A library for plotting in wxPython using matplotlib',
      long_description = long_desc,
      platforms = ('Windows', 'Linux', 'Mac OS X'),
      classifiers=['Intended Audience :: Science/Research',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering',
                   'Topic :: Scientific/Engineering :: Visualization'],
      packages = find_packages(),
)
