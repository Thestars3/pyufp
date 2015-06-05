#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
from trashcli.trash import TrashPutCmd
import io
import chardet
import HTMLParser
import re

__all__ = [
	'trashPut',
	'cleanSubtitle'
]

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
