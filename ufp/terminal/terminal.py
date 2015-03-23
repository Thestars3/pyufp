#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import sys
import ANSIColors

__all__ = ['feed', 'pause']

def feed(*objects):
	"""
	기존 줄을 지우고, 입력한 메시지를 화면에 씁니다.
	
	:param objects: 화면에 출력할 오브젝트
	:type objects: object
	"""
	ANSIColors.clearLine()
	print(*objects, end='')
	sys.stdout.flush()
	pass

def pause():
	"""
	사용자의 입력을 대기합니다.
	
	엔터를 눌러야 입력 대기가 끝납니다.
	"""
	print('[Enter]를 눌러 다음으로 진행합니다...', end = '');
	raw_input("");
	pass
