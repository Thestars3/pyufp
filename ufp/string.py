#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import unicodedata

def removeControlChar(string):
	"""
	제어문자를 제거합니다.
	
	:param string: 문자열
	:type string: unicode
	:return: 제어 문자가 제거된 문자열
	:rtype: unicode
	"""
	return ''.join(ch for ch in string if unicodedata.category(ch)[0]!="C")
