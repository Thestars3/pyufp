#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import random
import string as _p_string
import __builtin__

def bytes(size):
	"""
	size byte만큼의 램덤 바이트 데이터를 만듭니다.
	
	.. 참조 : http://stackoverflow.com/questions/5495492/random-byte-string-in-python/28131868#28131868
	
	:param size: 생성할 램덤 바이트 크기(단위 byte).
	:type size: int
	:return: 램덤 바이트 데이터.
	:rtype: bytes
	"""
	buffer = [ random.getrandbits(8) for _ in xrange(size) ]
	buffer = bytearray(buffer)
	return __builtin__.bytes(buffer)

def string(length, chars=_p_string.ascii_letters + _p_string.digits):
	"""
	지정된 길이 만큼의 램덤 문자열을 되돌려줍니다.
	
	:param length: 문자열의 길이
	:type length: int
	:param chars: 문자 집합\n
		[a, ..., z, A, ..., Z, 0, ..., 9] (기본값)
	:type chars: str, unicode, list
	:return: 램덤 문자열
	:rtype: unicode
	"""
	string = unicode()
	for i in xrange(length):
		string += random.choice(chars)
		pass
	return string
	