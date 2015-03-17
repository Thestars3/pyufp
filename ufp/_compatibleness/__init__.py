#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

from .terminal import color
sys.modules['ufp.terminal.color'] = color
from .. import terminal
terminal.color = color
