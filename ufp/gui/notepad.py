#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess
import pprint
import os

class Notepad(object):
	def open(self):
		"""
		메모창을 엽니다.
		"""
		self._devnull = open(os.devnull, 'w')
		self._process = subprocess.Popen(['kate', '--stdin'], stdin=subprocess.PIPE, stdout=self._devnull, stderr=self._devnull)
		pass
	
	def write(self, content):
		"""
		메모에 내용을 씁니다.
		
		:param content: 쓸 내용. list의 경우 각 항목을 줄 단위로 분할하여 기록합니다. list내에 존재하는 unicode는 그대로 기록하고, 그 외는 pprint.pformat함수를 호출하여 텍스트로 바꾸어 기록합니다. 그 외 요소는 모두 pprint.pformat함수를 호출하여 기록합니다.
		"""
		if isinstance(content, unicode):
			write = content.encode('UTF-8')
		elif isinstance(content, list):
			write = list()
			for i in content:
				if isinstance(i, unicode):
					write.append(i.encode('UTF-8'))
				else:
					write.append(pprint.pformat(i))
			write = '\n'.join(write)
		else:
			write = pprint.pformat(content)
		self._process.stdin.write(write)
		self._process.stdin.close()
	
	def close(self):
		"""
		메모창을 닫습니다.
		"""
		self._process.terminate()
		self._devnull.close()
		pass
	
	@classmethod
	def show(cls, content):
		"""
		주어진 내용을 보여줍니다.
		
		:param content: 보여줄 내용. :py:func:`~ufp.gui.Notepad.write` 의 내용과 같습니다.
		:return: 객체를 반환합니다.
		:rtype: :py:class:`~ufp.gui.Notepad`
		"""
		notepad = cls()
		notepad.open()
		notepad.write(content)
		return notepad
	