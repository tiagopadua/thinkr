# -*- coding: UTF-8 -*-

import os
import sys

'''
Created on May/31/2015

@author: tiagopadua@gmail.com
'''


__version__ = '0.0.1'
__author__ = 'Tiago de Pádua'
__description__ = 'Software that thinks'


def __path(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

if os.path.exists(__path('build.info')):
    __build__ = open(__path('build.info')).read().strip()
else:
    __build__ = '0'

__version__ = __version__ + '.' + __build__

