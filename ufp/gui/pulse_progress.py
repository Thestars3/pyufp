#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
from PyQt4.QtCore import pyqtSlot, QObject
import subprocess
import os

class PulseProgress(QObject):
	"""
	진행 표시줄이 끝없이 움직이는 진행 표시창을 띄웁니다.
	
	사용 예제는 다음과 같습니다.
		
	.. code-block:: python

		>>> import ufp.gui
		>>> import time
		>>> a = ufp.gui.PulseProgress('title', 'message')
		>>> a.open(); time.sleep(3); a.close()
		
	"""
	def __init__(self, title, message):
		"""
		진행 표시창을 초기화합니다.
		
		:param title: 제목
		:type title: unicode
		:param message: 메시지
		:type message: unicode
		"""
		super(PulseProgress, self).__init__()
		self.title = title
		self.message = message
		pass
	
	@pyqtSlot()
	def open(self):
		"""
		진행 표시창을 엽니다.
		"""
		self._devnull = open(os.devnull, 'w')
		self._zenity = subprocess.Popen(['zenity', '--progress', '--text', self.message, '--pulsate', '--no-cancel', '--auto-close', '--title', self.title], stdin=subprocess.PIPE, stdout=self._devnull, stderr=self._devnull)
		self._zenity.stdin.write('y')
		pass
	
	@pyqtSlot()
	def close(self):
		"""
		진행 표시창을 닫습니다.
		"""
		self._zenity.terminate()
		self._devnull.close()
		pass
	