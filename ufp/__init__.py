#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals, absolute_import

__title__ = 'ufp'
__version__ = '1.4.0'
__author__ = '별님'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2015 별님'

from .ufp import *

#하위 호환성 유지를 위한 설정
from . import _compatibleness
