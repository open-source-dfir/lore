#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Installation and deployment script."""

try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup


setup(
    name='lore',
    version='20200920',
    description='Documentation about developing Open Source DFIR tools',
    long_description=(
        'Documentation about developing Open Source DFIR tools'),
    license='CC-BY-4.0 License',
    url='https://github.com/open-source-dfir/lore',
    maintainer='Open Source DFIR maintainers',
    maintainer_email='open-source-dfir-maintainers@googlegroups.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    data_files=[
        ('share/doc/lore', [
            'LICENSE', 'README.md']),
    ],
)
