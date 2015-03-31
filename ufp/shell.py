#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess
import re
import os

def pgrep(pattern, extraArgs=list()):
	"""
	pattern에 해당하는 이름을 가진 프로세스 목록을 반환합니다.
	
	:param pattern: 프로세서 이름의 패턴
	:type pattern: unicode
	:param extraArgs: 추가 옵션
	:type extraArgs: list(unicode, ...)
	:return: 만약 pgrep 프로세서가 오류가 존재함을 알린(0과 1이 아닌 종료코드를 반환)다면 그 종료 코드를 반환합니다.
	:return: 만약 찾지 못한다면 빈 list를 반환합니다.
	:return: 찾는다면, [(id, name), ...]의 리스트를 반환합니다.
	"""
	args = ['pgrep', '-l', '--', pattern] + extraArgs
	with open(os.devnull, 'w') as devnull:
		ps = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=devnull)
		ps.wait()
		if ps.returncode == 0:
			buffer = ps.stdout.read()
			return re.findall('^(\d+)\s+(.*)$', buffer, re.MULTILINE)
		elif ps.returncode == 1:
			return list()
		else: 
			return ps.returncode
	pass

def quote(string):
	"""
	shell에서 주어진 문자열이 해석되지 않도록 콰우팅합니다.
	
	:param string: 문자열
	:type string: unicode
	:return: 콰우팅 된 문자열
	:rtype: unicode
	"""
	buffer = string.replace("'", r"'\''")
	return "'{string}'".format(string=buffer)
	