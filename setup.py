#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup
from setuptools import find_packages

# ┏━╸╻ ╻┏━╸╻ ╻┏━┓┏━┓
# ┣╸ ┃ ┃┃  ┣━┫┣━┫┣┳┛
# ╹  ┗━┛┗━╸╹ ╹╹ ╹╹┗╸

def readme():
    with open('README.rst') as f:
        return f.read()

import fuchar

setup(
    name='fuchar',
    version=fuchar.__version__,
    author=fuchar.__author__,
    author_email=fuchar.__author_email__,
    url=fuchar.__url__,
    license=fuchar.__license__,
    description=fuchar.__doc__,
    long_description=readme(),
    entry_points={
        'console_scripts': [
            'fuchar=fuchar.__main__:main',
        ]
    },
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
    ],
)

