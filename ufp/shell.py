#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

def quote(string):
	"""
	shell에서 주어진 문자열이 해석되지 않도록 콰우팅합니다.
	
	:param string: 문자열
	:type string: unicode
	:return: 콰우팅 된 문자열
	:rtype: unicode
	"""
	buffer = string.replace("'", r"'\''")
	return "'{0}'".format(buffer)
	