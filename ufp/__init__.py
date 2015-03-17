#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@brief 사용자 함수 묶음.
@version v4\n
	bash -> c++ -> (qt ->) python
@author 별님 <w7dn1ng75r@gmail.com>
@details \n
	홈페이지 : http://thestars3.tistory.com/
"""

from __future__ import unicode_literals, absolute_import

__author__ = '별님'
__copyright__ = 'Copyright (C) 2015년 별님'
__credits__ = ['별님']
__maintainer__ = "별님"
__license__ = "GPL v3"
__version__ = "1.0.0"
__email__ = "w7dn1ng75r@gmail.com"
__status__ = "Production"
__package__ = str('ufp')

from .ufp import *

#하위 호환성 유지를 위한 설정
from . import _compatibleness
