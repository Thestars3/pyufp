#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import io
import logging
import os
import select
import subprocess
import time
import threading

class StreamLogger(io.IOBase):
	"""
	주어진 로깅 객체에 파일 처럼 쓸수 있는 객체를 생성합니다.
	
	예컨데, 다음과 같이 활용 할 수 있습니다.
	
	.. code-block:: python

		>>> import ufp.logging
		>>> import subprocess
		>>> import logging
		>>> logging.setLevel(logging.DEBUG)
		>>> with ufp.logging.StreamLogger(logging.INFO) as out:
		... 	with ufp.logging.StreamLogger(logging.ERROR) as err:
		... 		subprocess.call(['ls', '-1'], stdout=out, stderr=err)
		... 
		... 	
		INFO:root:test (d1).file
		INFO:root:test (d2).file
		INFO:root:test.file
		0
	
	.. 참조 : 
		http://stackoverflow.com/questions/4713932/decorate-delegate-a-file-object-to-add-functionality/4838875#4838875
		http://stackoverflow.com/questions/13923344/logging-from-an-external-application
	
	:param logger: 로깅 객체. 생략시 전역 로깅 객체를 사용합니다.
	:type logger: logging.Logger, None
	:param level: 로그 작성 레벨
	:type level: int
	"""
	def __init__(self, level, logger=None):
		self.logger = logging.getLogger() if logger is None else logger
		self.level = level
		self.pipe = os.pipe()
		self.thread = threading.Thread(target=self._flusher)
		self.thread.start()
	
	def _flusher(self):
		self._run = True
		buf = b''
		while self._run:
			for fh in select.select([self.pipe[0]], [], [], 0)[0]:
				buf += os.read(fh, 1024)
				while b'\n' in buf:
					data, buf = buf.split(b'\n', 1)
					self.write(data.decode())
			time.sleep(1)
		self._run = None
	
	def write(self, data):
		"""
		스트림에 메세지를 작성합니다.
		
		:param data: 데이터. 
		"""
		return self.logger.log(self.level, data)
	
	def fileno(self):
		"""
		이 스트림의 fileno를 반환합니다.
		
		:return: 이 스트림의 파일 디스크립터
		:rtype: int
		"""
		return self.pipe[1]
	
	def close(self):
		"""
		스트림을 닫습니다.
		"""
		if self._run:
			self._run = False
			while self._run is not None:
				time.sleep(1)
			os.close(self.pipe[0])
			os.close(self.pipe[1])
		pass
	