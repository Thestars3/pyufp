#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

from ..repr import make_object as make_repr

#호환 설정
from .. import ufp as b
b.make_repr = make_repr
b.__all__.append('make_repr')
