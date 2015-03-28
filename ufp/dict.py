#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import UserDict

class Lazy(UserDict.UserDict):
	"""
	설정된 사전 값에 대해 접근 할때 초기화되도록 설정 할 수 있는 사전.
	
	늦은 초기화가 생략 된 경우, 해당 키의 값에 대해서는 늦은 초기화를 사용하지 않도록 설정되어 있습니다.
	
	사용 예는 다음과 같습니다.
	
	.. code-block:: python
		
		>>> import ufp.dict
		>>> from ufp.terminal.debug import print_ as debug
		>>> dict = ufp.dict.Lazy()
		>>> def function():
		... 	debug('inited...')
		... 	return 10
		... 
		>>> dict.add('lazyInitValue', function, True)
		>>> dict['lazyInitValue']
		[DEBUG] inited...
		10
		>>> dict['lazyInitValue']
		10
	"""
	def __init__(self, dict=None):
		self.data = {}
		if dict is not None:
			self.update(dict)
		self._lazyInitDict = {}
	
	def add(self, key, value, lazyInit=False):
		"""
		늦은 초기화 여부를 설정하면서 사전에 등록합니다.
		
		:param key: 키
		:param value: 값
		:param lazyInit: 늦은 초기화 설정. True시 늦은 초기화를 사용함.
		"""
		self[key] = value
		self._lazyInitDict[key] = lazyInit
	
	def items(self):
		"""
		기존 UserDict.UserDict.items와 같습니다.
		"""
		for key, value in self.data.items():
			if self._lazyInitDict.get(key, False) and callable(value):
				value = value()
				self.data[key] = value
				self._lazyInitDict[key] = False
			yield key, value
	
	def values(self):
		"""
		기존 UserDict.UserDict.values와 같습니다.
		"""
		return map(lambda k,v: v, self.items())
	
	def __delitem__(self, key):
		if key in self._lazyInitDict:
			del self._lazyInitDict[key]
		del self.data[key]
	
	def setLazyInit(self, key, lazyInit):
		"""
		개별 키에 대한 늦은 초기화 여부를 설정합니다.
		
		:param key: 키
		:param lazyInit: 늦은 초기화 설정. True시 늦은 초기화를 사용함.
		"""
		self._lazyInitDict[key] = lazyInit
	
	def __getitem__(self, key):
		if self._lazyInitDict.get(key, False) and callable(self.data[key]):
			self.data[key] = self.data[key]()
			self._lazyInitDict[key] = False
		return self.data[key]


def setdefault(dict, key, default, empty=None):
	"""
	주어진 dict에 key가 존재하지 않으면, default를 설정합니다. 이때, key가 존재하더라도 empty와 같다면 default를 설정합니다. 
	
	사전 객체의 모든 요소와 empty값은 __eq__ 메소드가 작성되어 있어야 합니다. None은 예외.
	
	:param dict: 사전
	:type dict: dict
	:param key: 키
	:param default: 기본값
	:param empty: 이미 설정된 값이 empty와 같다면 default값을 설정함.
	"""
	if key not in dict:
		dict[key] = default
		return
	
	if dict[key] is None or dict[key] == empty:
		dict[key] = default
	pass
