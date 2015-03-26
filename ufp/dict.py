#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

def setdefault(dict, key, default, empty=None):
	"""
	주어진 dict에 key가 존재하지 않으면, default를 설정합니다. 이때, key가 존재하더라도 empty와 같다면 default를 설정합니다. 
	
	사전 객체의 모든 요소와 empty값은 __eq__ 메소드가 작성되어 있어야 합니다. None은 예외.
	
	:param dict: 사전
	:type dict: dict
	:param key: 키
	:param default: 기본값
	:param empty: 이미 설정된 값이 empty와 같다면 default값을 설정함.
	"""
	if key not in dict:
		dict[key] = default
		return
	
	if dict[key] is None or dict[key] == empty:
		dict[key] = default
	pass
