#!/usr/bin/env python
from setuptools import setup

VERSION = "0.2.7"

setup (
       name = "threadly",
       version = VERSION,
       author = "Luke Wahlmeier",
       author_email = "lwahlmeier@gmail.com",
       url = "http://lwahlmeier.github.io/python-threadly/",
       download_url = "https://github.com/lwahlmeier/python-threadly/tarball/%s"%(VERSION),
       license = "lgpl",
       description = "Threading pool and scheduler for python",
       long_description = open('README-pypi.rst').read(),
       keywords = ['threading', 'scheduling'],
       classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities'
        ],
       py_modules =  ['threadly'],
       test_suite = 'tests',
      )
