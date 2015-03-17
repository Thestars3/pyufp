#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess

class Notepad(object):
	def open(self):
		"""
		@brief 메모창을 엽니다.
		"""
		self._process = subprocess.Popen(['kate', '--stdin'], stdin=subprocess.PIPE)
		pass
	
	def write(self, content):
		"""
		@brief 메모에 내용을 씁니다.
		@param content 쓸 내용
		"""
		self._process.stdin.write(content)
		pass
	
	def close(self):
		"""
		@brief 메모창을 닫습니다.
		"""
		self._process.kill()
		pass
	
	@classmethod
	def show(cls, content):
		"""
		@brief 주어진 내용을 보여줍니다.
		@param content 보여줄 내용
		@return 객체를 반환합니다.
		"""
		notepad = cls()
		notepad.open()
		notepad.write(content)
		return notepad
	