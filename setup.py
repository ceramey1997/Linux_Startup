#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

setup_dir = os.path.dirname(os.path.abspath(__file__))

requirments = (
    open(os.path.join(setup_dir, 'requirements.txt')).read().splitlines()
)

required = [line for line in requirments if not line.startswith('-')]

setup(name='coop_startup',
      description='to streamline pc start up after a shut down',
      author='Cole Ramey',
      install_requires=['six'],
      include_package_data=True,
      entry_points={
          'console_scripts' : ['startup = startup:Important_Programs_open'],
      },
    )