#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

RGB_MIN_VALUE = 0
RGB_MAX_VALUE = 255

GRAYSCALE_MIN_VALUE = 0
GRAYSCALE_MAX_VALUE = 255

# 호환 설정
from .. import image
image.RGB_MIN_VALUE = RGB_MIN_VALUE
image.RGB_MAX_VALUE = RGB_MAX_VALUE
image.GRAYSCALE_MIN_VALUE = GRAYSCALE_MIN_VALUE
image.GRAYSCALE_MAX_VALUE = GRAYSCALE_MAX_VALUE
