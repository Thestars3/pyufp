#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
출처 : http://stackoverflow.com/questions/5189699/how-can-i-make-a-class-property-in-python
"""

from __future__ import unicode_literals, absolute_import, division, print_function
import inspect

class ClassProperty(object):
	def __init__(self, fget, fset=None):
		self.fget = fget
		self.fset = fset
	
	def __get__(self, obj, klass=None):
		if klass is None:
			klass = type(obj)
		return self.fget.__get__(obj, klass)()
		
	def __set__(self, obj, value):
		if not self.fset:
			raise AttributeError(b"can't set attribute")
		if inspect.isclass(obj):
			type_ = obj
			obj = None
		else:
			type_ = type(obj)
		return self.fset.__get__(obj, type_)(value)
	
	def setter(self, func):
		if not isinstance(func, (classmethod, staticmethod)):
			func = classmethod(func)
		self.fset = func
		return self    
	

class ClassPropertyMetaClass(type):
	def __setattr__(self, key, value):
		if key in self.__dict__:
			obj = self.__dict__.get(key)
			if obj and type(obj) is ClassProperty:
				return obj.__set__(self, value)
		super(ClassPropertyMetaClass, self).__setattr__(key, value)
	

def classproperty(function):
	"""
	class property를 만듭니다.
	
	setter를 사용하기 위해서는 메타 클래스를 :py:class:`ufp.descriptor.ClassPropertyMetaClass` 로 지정해야 합니다.
	
	사용 예는 다음과 같습니다.
	
	.. code-block:: python
	
		>>> import ufp.descriptor
		>>> class Test(object):
		... 	__metaclass__ = ufp.descriptor.ClassPropertyMetaClass
		... 	_vlaue = 10
		... 	
		... 	@ufp.descriptor.classproperty
		... 	def value(self):
		... 		return self._vlaue
		... 		
		... 	@value.setter
		... 	def value(self, v):
		... 		self._vlaue = v
		... 
		>>> Test.value
		10
		>>> Test.value = 100
		>>> Test.value
		100
	
	:param function: 함수
	:type function: function
	:return: class property
	:rtype: :py:class:`ClassProperty`
	"""
	if not isinstance(function, (classmethod, staticmethod)):
		function = classmethod(function)
	
	return ClassProperty(function)
	