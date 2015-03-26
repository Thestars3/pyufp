#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

def unpadPkcs5(data):
	"""
	PKCS#5 표준 패딩을 제거한다.
	
	:param data: 입력 데이터
	:type data: bytes
	:returns: 패딩이 제거된 데이터
	:rtype: bytes
	"""
	return data[0:-ord(data[-1])]
	