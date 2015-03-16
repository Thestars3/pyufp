#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

def unpadPkcs5(s):
	"""
	@brief PKCS#5 표준 패딩을 제거한다.
	"""
	return s[0:-ord(s[-1])]
	