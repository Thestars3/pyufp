#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess

class Notepad(object):
	def open(self):
		self._process = subprocess.Popen(['kate', '--stdin'], stdin=subprocess.PIPE)
		pass
	
	def write(self, content):
		self._process.stdin.write(content)
		pass
	
	def close(self):
		self._process.kill()
		pass
	
	@classmethod
	def show(cls, content):
		"""
		주어진 내용을 보여줍니다.
		객체를 반환합니다.
		"""
		notepad = cls()
		notepad.open()
		notepad.write(content)
		return notepad
	