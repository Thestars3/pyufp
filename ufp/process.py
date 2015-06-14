#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess

def pgrep(pattern, only_match_name=False):
	"""
	pattern 형식에 매칭되는 프로세서를 찾습니다.
	
	:Availability: Unix.
	:param pattern: 패턴. True를 주면 전체 프로세서를 검색.
	:type pattern: unicode, True
	:param only_match_name: Only match processes whose name exactly match the pattern.
	:type only_match_name: bool
	:return: 프로세스 아이디 목록.
	:rtype: [int, ...]
	"""
	commands = ['pgrep']
	if only_match_name:
		commands.append('-x')
	commands.append('--')
	commands.append('' if pattern is True else pattern)
	try:
		out = subprocess.check_output(commands)
		out = out.strip()
		return [ int(i) for i in out.split('\n') ]
	except subprocess.CalledProcessError:
		return []
	pass
	
def pkill(pattern):
	"""
	pattern 형식에 매칭되는 프로세서를 종료시킵니다.
	
	:Availability: Unix.
	:param pattern: 패턴.
	:type pattern: unicode
	"""
	subprocess.call(['pkill', pattern])

def nohup(args, stdin=None, stdout=None, stderr=None):
	"""
	hangup 시그널은 무시하고 지정한 명령을 실행합니다.
	
	:Availability: Unix.
	:param args: 명령행 인자 목록.
	:type args: [unicode, ...]
	:param stdin: 표준입력. 만약 지정하지 않으면 /dev/null로 재지향됩니다.
	:param stdout: stdin과 동일.
	:param stderr: stderr과 동일.
	:return: 서브 프로세서 객체.
	:rtype: subprocess.Popen
	"""
	if stdin is None or stdout is None or stderr is None:
		devnull = open('/dev/null', 'w+b')
		if stdin is None:
			stdin = devnull
		if stdout is None:
			stdout = devnull
		if stderr is None:
			stderr = devnull
	
	return subprocess.Popen(
		['nohup'] + args, 
		stdin = stdin,
		stdout = stdout, 
		stderr = stderr
	)
	