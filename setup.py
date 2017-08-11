#!/usr/bin/env python

from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

from wordninja import __version__

setup(name='wordninja',
  version=__version__,
  description="Probabilistically split concatenated words using NLP based on English Wikipedia uni-gram frequencies.",
  author='Derek Anderson',
  author_email='public@kered.org',
  packages = ['wordninja'],
  url='https://github.com/keredson/wordninja',
  package_data={'wordninja': ['wordninja_words.txt.gz']},
  package_dir={'wordninja': 'wordninja'},
  include_package_data=True,
  py_modules=['wordninja'],
)
