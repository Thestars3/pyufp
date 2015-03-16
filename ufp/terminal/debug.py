#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import __builtin__ as builtins

from . import color as _p_color

def print(*objs) :
	builtins.print('{0}[디버그]{1} '.format(_p_color.bak.red, _p_color.reset), end='');
	builtins.print(*objs);
	pass
