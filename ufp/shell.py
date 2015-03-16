#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

def quote(string):
	"""
	@brief shell에서 해석되지 않도록 콰우팅합니다.
	@param string 문자열
	@return 콰우팅 된 문자열
	"""
	buffer = string.replace("'", r"'\''")
	buffer = "'{0}'".format(buffer)
	return buffer
	