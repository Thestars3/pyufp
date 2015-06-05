#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import itertools

def _get_instance_name(instance):
	if isinstance(instance, unicode):
		return instance
	if isinstance(instance, object):
		return type(instance).__name__
	return instance.__class__.__name__

def make_type(type_name, class_name):
	"""
	형식 repr 문자열을 생성합니다.
	
	:param type_name: 형식명.
	:type type_name: unicode
	:param class_name: 클래스 명.
	:type class_name: unicode, instance
	:return: u"<{type_name} '{class_name}'>"
	:rtype: unicode
	"""
	return "<{type_name} '{class_name}'>".format(
		type_name = type_name,
		class_name = _get_instance_name(class_name)
	)

def make_object(type_name, values=[], orderd_items=[], items={}, **kwargs):
	"""
	객체 repr 문자열을 생성합니다.
	
	:param type_name: 형식명. instance를 줄 경우, 해당 오브젝트의 클래스명을 사용합니다.
	:type type_name: unicode, instance
	:param values: 값들. values, args순서로 배치됩니다.
	:type values: [value, ...]
	:param items: 값들. orderd_items, items, kwargs순서로 배치됩니다.
	:type items: {key:value, ...}
	:param orderd_items: 값들. 전달된 순서대로 배치합니다.
	:type orderd_items: [(key,value), ...]
	:param **kwargs: 값들.\n
		형식과 값은 items의 각 요소와 같습니다.
	:return: u'{type_name}({value}, ..., {key}={value}, ...)'
	:rtype: unicode
	"""
	#값 목록 작성
	def convert(value):
		if isinstance(value, unicode):
			buffer = value.replace("'", r"\'")
			return "'{0}'".format(buffer)
		return repr(value)
	repr_list = list()
	for value in values:
		buffer = convert(value)
		repr_list.append(buffer)
	for key, value in itertools.chain(orderd_items, items.items(), kwargs.items()):
		buffer = convert(value)
		buffer = '{key}={value}'.format(key=key, value=buffer)
		repr_list.append(buffer)
	
	return '{type_name}({repr})'.format(
		type_name = _get_instance_name(type_name), 
		repr = ', '.join(repr_list)
	)
