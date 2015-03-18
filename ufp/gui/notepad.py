#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess
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
		
		:param content: 쓸 내용
		"""
		self._process.stdin.write(content)
		self._process.stdin.close()
		pass
	
	def close(self):
		"""
		메모창을 닫습니다.
		"""
		self._devnull.close()
		self._process.kill()
		pass
	
	@classmethod
	def show(cls, content):
		"""
		주어진 내용을 보여줍니다.
		
		:param content: 보여줄 내용
		:return: 객체를 반환합니다.
		"""
		notepad = cls()
		notepad.open()
		notepad.write(content)
		return notepad
	