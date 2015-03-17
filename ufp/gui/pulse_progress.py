#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
from PyQt4.QtCore import pyqtSlot, QObject
import subprocess

class PulseProgress(QObject):
	def __init__(self, title, message):
		super(PulseProgress, self).__init__()
		self.title = title
		self.message = message
		pass
	
	@pyqtSlot()
	def open(self):
		self._zenity = subprocess.Popen(['zenity', '--progress', '--text', self.message, '--pulsate', '--no-cancel', '--auto-close', '--title', self.title], stdin=subprocess.PIPE)
		self._zenity.stdin.write('y')
		pass
	
	@pyqtSlot()
	def close(self):
		self._zenity.kill()
		pass
	