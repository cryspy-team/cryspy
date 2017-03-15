#!/usr/bin/env python

from distutils.core import setup

setup(name='cryspy',
      version='0.1',
      description=' ',
      author='Tobias Froehlich',
      author_email='',
      url='https://github.com/cryspy-team/cryspy/',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Topic :: Scientific/Engineering :: Physics',
          'Topic :: Multimedia :: Graphics :: 3D Rendering',
          'Topic :: Scientific/Engineering :: Visualization',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 3'
          ],
      packages=['cryspy'],
      install_requires=[
          'uncertainties',
          'quicktions']
     )
