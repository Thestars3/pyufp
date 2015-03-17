#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals

__all__ = list()

__all__ += ['reset'] 
reset = u"\033[39;49;00m";       #: 색상값을 초기화

"""글자 색"""
__all__ += ['red', 'green', 'yellow', 'blue', 'blue', 'magenta', 'cyan']
red = u"\033[31;01m";            #: 빨강색
green = u"\033[32;01m";          #: 초록색
yellow = u"\033[33;01m";         #: 노랑색
blue = u"\033[34;01m";           #: 파랑색
magenta = u"\033[35;01m";        #: 자홍색, 마젠타색
cyan = u"\033[36;01m";           #: 밝은 파랑색, 시안색
