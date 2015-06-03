#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
from ufp.terminal.debug import print_ as debug

class CachedProperty(object):    
	"""
	한번 실행한 결과를 기억하는 속성 장식자.
	
	setter를 설정 할 경우, 설정 하려는 값을 반환해줘야 합니다. 반환하지 않을 경우, 설정된 값은 None이 됩니다.
	
	deleter를 설정 할 경우, 메소드가 수행 된 이후 저장된 값이 삭제됩니다.
	
	.. code-block:: python

		>>> class Test(object):
		... 	@CachedProperty
		... 	def value(self):
		... 		print('Calculating self.value')
		... 		return 10
		... 	
		>>> test = Test()
		>>> print(test.value)
		Calculating self.value
		10
		>>> print(test.value) 
		10
		>>> test.value = 100
		>>> test.value
		100
		>>> del test.value
		>>> test.value
		Calculating self.value
		10
	
	.. 참조:
		http://code.activestate.com/recipes/276643-caching-and-aliasing-with-descriptors/
		http://stackoverflow.com/questions/3237678/how-to-create-decorator-for-lazy-initialization-of-a-property
		https://gist.github.com/sharoonthomas/1673907
	
	:param method: 메소드.
	:type method: function
	"""
	def __init__(self, method):
		self.fget = method
		self.fset = None
		self.fdel = None
		
		self.__doc__ = method.__doc__
		self.name = method.__name__
		
	def setter(self, method):
		self.fset = method
		return self
	
	def deleter(self, method):
		self.fdel = method
		return self
	
	def __get__(self, instance, cls): 
		if instance is None:
			return self
		
		if self.name in instance.__dict__:
			return instance.__dict__[self.name]
		
		value = self.fget(instance)
		instance.__dict__[self.name] = value
		return value
	
	def __set__(self, instance, value):
		if self.fset:
			value = self.fset(instance, value)
		instance.__dict__[self.name] = value
	
	def __delete__(self, instance):
		if self.fdel:
			self.fdel(instance)
		if self.name in instance.__dict__:
			del instance.__dict__[self.name]
		pass
	
