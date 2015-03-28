#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import __builtin__ as builtins
import ANSIColors

def print_(*objects, **kwargs):
	"""
	디버깅 메시지를 터미널에 출력합니다.
	
	빨간색으로 강조된 '[디버그]' 문자열 뒤에 주어진 objs가 출력됩니다.
	
	.. @link http://pythonhosted.org/ANSIColors-balises/ANSIColors.html ANSIColors Module — ANSIColors-balises public documentation
	
	:param objects: 출력할 오브젝트들
	:type objects: object
	:param kwargs: 옵션(__builtin__.print 함수의 인자와 같습니다)
	"""
	buffer = ANSIColors.sprint('<Red>[DEBUG]<reset> ')
	builtins.print(buffer, end='');
	builtins.print(*objects, **kwargs);
	pass
