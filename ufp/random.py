#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import random
import string as _p_string

def string(length, chars=_p_string.ascii_letters + _p_string.digits):
	"""
	@brief 지정된 길이 만큼의 램덤 문자열을 되돌려줍니다.
	
	@param length 문자열의 길이
	@param chars 문자 집합(리스트 형식)
		[a, ..., z, A, ..., Z, ..., 0, ..., 9] (기본값)
	
	@return 램덤 문자열
	"""
	string = unicode()
	for i in xrange(length):
		string += random.choice(chars)
		pass
	return string
	