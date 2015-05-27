#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
from bs4 import Tag, NavigableString, Comment

def copy(element):
	"""
	beautifulsoup4 객체의 요소를 복제합니다.
	
	오직 해당 요소의 정보만 복사합니다. 자식들에 대한 정보는 원본과 공유됩니다.
	
	.. bugs::
		work around bug where there is no builder set https://bugs.launchpad.net/beautifulsoup/+bug/1307471.
	
	.. 이 함수 작성에 다음 문서를 참조하였음.
		http://stackoverflow.com/questions/23057631/clone-element-with-beautifulsoup
	
	:param element: 복제 할 원소.
	:type element: bs4.Tag, bs4.NavigableString, bs4.Comment
	:return: 복제된 원소.
	"""
	if isinstance(element, (NavigableString, Comment)):
		return type(element)(element)
	
	clone_element = Tag(None, element.builder, element.name, element.namespace, element.nsprefix)
	clone_element.attrs = dict(element.attrs)
	for attr in ('can_be_empty_element', 'hidden'):
		setattr(clone_element, attr, getattr(element, attr))
	for child in element.contents:
		clone_element.append(child)
	return clone_element

def deepcopy(element):
	"""
	beautifulsoup4 객체의 요소를 재귀적으로 복제합니다.
	
	요소가 가진 정보 및 자식의 모든 정보를 재귀적으로 복제합니다.
	
	이 함수를 통하여, beautifulsoup4 4.0.2에서 append 함수 사용시 발생하는 DOM 깨짐현상(기존에 존재하던 태그에 접근 불가능해지거나, 각 메소드들 별로 원래 정상적으로 접근하게될 결과의 일부분만 얻게 되는 현상)을 피할 수 있습니다.
	
	.. 이 함수 작성에 다음 문서를 참조하였음.
		http://stackoverflow.com/questions/23057631/clone-element-with-beautifulsoup
	
	:param element: 복제 할 원소.
	:type element: bs4.Tag, bs4.NavigableString, bs4.Comment
	:return: 복제된 원소.
	"""
	if isinstance(element, (NavigableString, Comment)):
		return type(element)(element)
	
	clone_element = Tag(None, element.builder, element.name, element.namespace, element.nsprefix)
	# work around bug where there is no builder set
	# https://bugs.launchpad.net/beautifulsoup/+bug/1307471
	clone_element.attrs = dict(element.attrs)
	for attr in ('can_be_empty_element', 'hidden'):
		setattr(clone_element, attr, getattr(element, attr))
	for child in element.contents:
		clone_element.append(deepcopy(child))
	return clone_element
