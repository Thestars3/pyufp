#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

# terminal module
from .terminal import color
sys.modules['ufp.terminal.color'] = color
from .. import terminal
terminal.color = color

# image module
from . import image as s
from .. import image as d
d.RGB_MIN_VALUE = s.RGB_MIN_VALUE
d.RGB_MAX_VALUE = s.RGB_MAX_VALUE
d.GRAYSCALE_MIN_VALUE = s.GRAYSCALE_MIN_VALUE
d.GRAYSCALE_MAX_VALUE = s.GRAYSCALE_MAX_VALUE
