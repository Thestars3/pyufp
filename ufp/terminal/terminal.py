#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import sys

__all__ = ['feed', 'pause']

def feed(*msg) :
	sys.stdout.write("\r\033[K")
	print(*msg, end='')
	sys.stdout.flush()
	pass

def pause() :
	"""
	@brief 사용자의 입력을 대기합니다.
	"""
	print('[Enter]를 눌러 다음으로 진행합니다...', end = '');
	raw_input("");
	pass
