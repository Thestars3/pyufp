#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
from trashcli.trash import TrashPutCmd
import io
import chardet
import HTMLParser
import re
import itertools

__all__ = ['trashPut', 'cleanSubtitle', 'make_repr']

def make_repr(type_name, values=[], orderd_items=[], items={}, *args, **kwargs):
	"""
	repr 문자열을 생성합니다.
	
	:param type_name: 형식명. instance를 줄 경우, 해당 오브젝트의 클래스명을 사용합니다.
	:type type_name: unicode, instance
	:param values: 값들. values, args순서로 배치됩니다.
	:type values: [value, ...]
	:param items: 값들. orderd_items, items, kwargs순서로 배치됩니다.
	:type items: {key:value, ...}
	:param orderd_items: 값들. 전달된 순서대로 배치합니다.
	:type orderd_items: [(key,value), ...]
	:param *args: 값들.\n
		형식과 값은 values의 각 요소와 같습니다.
	:param **kwargs: 값들.\n
		형식과 값은 items의 각 요소와 같습니다.
	:return: u'{type_name}({value}, ..., {key}={value}, ...)'
	:rtype: unicode
	"""
	#형식명 설정
	if isinstance(type_name, unicode):
		pass
	elif isinstance(type_name, object):
		type_name = type(type_name).__name__
	else:
		type_name = type_name.__class__.__name__
	
	#값 목록 작성
	def convert(value):
		if isinstance(value, unicode):
			buffer = value.replace("'", r"\'")
			return "'{0}'".format(buffer)
		return repr(value)
	repr_list = list()
	for value in itertools.chain(values, args):
		buffer = convert(value)
		repr_list.append(buffer)
	for key, value in itertools.chain(orderd_items, items.items(), kwargs.items()):
		buffer = convert(value)
		buffer = '{key}={value}'.format(key=key, value=buffer)
		repr_list.append(buffer)
	
	return '{type_name}({repr})'.format(
		type_name=type_name, 
		repr=', '.join(repr_list)
	)

def cleanSubtitle(content, type=None):
	"""
	자막 파일을 깨끗히 만듭니다.
	
	다음 문제를 해결해줍니다:
	
		* 자막 깨짐 현상 해결(대신 mplayer의 기본 인코딩은 utf8이여야 합니다).
		* 자막에 존재하는 html 이스케이프된 문자열을 정상적으로 출력되도록 수정합니다.
		* smi 파일에 sami태그가 빠진 경우 추가시켜 줍니다.
	
	.. note:: 오직, smi, ass 파일만 지원합니다.
	.. caution:: 변환 결과가 잘못 될 수도 있습니다.
	
	:param content: 자막 내용.
	:type content: unicode, bytes
	:param type: 자막 종류.\n
		u'smi': 주어진 내용은 smi 파일.
		u'ass':주어진 내용은 ass 파일.
		None: smi, ass파일에 대한 공통 작업만 수행.
	:return: 변환된 자막 내용을 유니코드 문자열 타입으로 반환합니다.
	:rtype: unicode
	"""
	if not isinstance(content, unicode):
		encoding = chardet.detect(content)['encoding']
		content = content.decode(encoding, errors='replace')
	
	#smi 파일에 대한 처리.
	if type == 'smi':
		#sami 태그가 존재하지 않을 시 추가
		if not re.match(r'<SAMI>', content):
			content = '<SAMI>' + content
	
	#&#[0-9]+; 이스케이프 해제
	unescape = HTMLParser.HTMLParser().unescape
	buffer = lambda m: unescape(m.group(0))
	content = re.sub(r'&#\d+;', buffer, content)
	
	return content

def trashPut(target):
	"""
	대상을 휴지통에 버립니다.
	
	trashcli 패키지의 trash-put 명령어에 대한 인터페이스.
	
	:param taget: 지울 대상의 경로 문자열
	:type taget: unicode
	
	:return: True. 성공시
	:return: False. 문제가 존재 할 시
	:rtype: bool
	"""
	out = io.BytesIO()
	err = io.BytesIO()
	TrashPutCmd(out, err).run(['', '--', target.encode('utf8')])
	if err.getvalue():
		return False
	return True
