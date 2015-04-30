#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

def urshift(val, n):
	"""
	부호 없이 식을 비트 단위로 오른쪽으로 이동합니다.
	
	자바스크립트의 >>> 연산자와 같은 역할을 합니다. 예를 들어 '(-1000) >>> 3'는 'ufp.math.rshift(-1000, 3)'와 같습니다.
	
	.. 참조 : http://stackoverflow.com/questions/5832982/how-to-get-the-logical-right-binary-shift-in-python
	
	:param val: 식
	:param n: 비트 수
	:return: 부호 없이 식을 비트 단위로 오른쪽으로 이동한 결과 값.
	"""
	if val >= 0:
		return val >> n
	else:
		return ( val + 0x100000000 ) >> n
	pass
