#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

def preallocate(size, value=None):
	"""
	size 만큼의 길이를 가진 list를 반환합니다. 리스트의 내용은 value로 채워집니다.
	
	:param size: 할당 할 크기.
	:type size: int
	:param value: 초기화 할 값.
	:return: size만큼 할당 된 list.
	"""
	return size * [value]

def chunks(list, step):
	"""
	list를 step 단위로 묶어 yield합니다.
	
	.. 아래 함수가 정상적으로 작동 이유. 파이썬에서는 범위에서 벗어난 인덱스에 접근하려 할때, 자동으로 마지막 요소까지만 접근하도록 조정해준다.
	.. 참조 : http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python?page=1&tab=votes#tab-top
	
	예를 들어, 다음과 같이 작동합니다.
	
	.. code-block:: python
	
		>>> import ufp.list
		>>> for i in ufp.list.chunks(range(20), 5):
		... 	print(i)
		...
		[0, 1, 2, 3, 4]
		[5, 6, 7, 8, 9]
		[10, 11, 12, 13, 14]
		[15, 16, 17, 18, 19]
	
	:param list: 리스트
	:type list: list
	:param step: 단위
	:type step: int
	:yield: 각 step단위로 묶인 리스트. [...]
	"""
	length = len(list)
	for index in xrange(0, length, step):
		yield list[index:index+step]
	pass
