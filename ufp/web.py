#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals
import tempfile
import urllib
import re
import cookielib
import chardet

from . import path as _p_path
from . import string as _p_string

def trimFilename(filename, **options):
	"""
	웹에서 다운받은 파일의 이름을 손질함.
	
	다음 작업을 수행합니다:
	
		- url coding 풀기
		- 사용불가능한 문자를 대체문자로 치환
		- 웹에서의 공백치환을 감지하고 경우에 따라 해제
		- 파일 이름을 다듬기
		- UHC로 변환가능한 인코딩은 변환
	
	.. caution:: 인코딩 변환이 잘못될수도 있습니다.
	
	:param filename: 파일명 유니코드 문자열
	:type filename: unicode, bytes
	:param from_encoding: 입력 인코딩.\n
		'auto' : 자동으로 인코딩을 파악합니다. \n
		False : 인코딩을 변환하지 않습니다. (기본)\n
		기타('utf8', 'uhc', ...)
	:param consider_extension: 확장자 고려 여부\n
		True: 확장자를 고려하여 작업합니다.\n
		False: 확장자를 고려하지 않습니다. (기본)
	:type consider_extension: bool
		
	:return: 변환된 문자열
	:return: u'Unknown'. 결과물이 공백이 될 경우 공백 대신 이 문자열이 반환됩니다.
	:rtype: unicode
	"""
	#옵션 초기값 설정
	options.setdefault(u'consider_extension', False)
	options.setdefault(u'from_encoding', False)
		
	#옵션 처리 : consider_extension
	considerExtension = options[u'consider_extension']
	
	#옵션 처리 : from_encoding
	if options[u'from_encoding'] == u'auto':
		fromEncoding = chardet.detect(filename)['encoding']
	elif options[u'from_encoding'] == False:
		fromEncoding = None
	else:
		fromEncoding = options[u'from_encoding']
	
	#url 디코딩
	filename = urllib.unquote(filename)
	
	#인코딩 변환
	if fromEncoding:
		filename = filename.decode(fromEncoding, errors='replace')
	
	#url 디코딩
	filename = urllib.unquote(filename)
	
	#전체 파일명의 앞뒤 공백 제거
	filename = filename.strip()
	
	#파일명에 사용불가능한 문자 치환
	filename = _p_path.replaceSpiecalChar(filename)
	
	#확장자 분리
	if considerExtension:
		ext = _p_path.extension(filename)
		if ext:
			filename = _p_path.filename(filename)
		else:
			considerExtension = False
		
	#이름에 포함된 and표시 제거
	if not re.search(u' ', filename):
		pattern1 = re.compile(u'[_+]', re.UNICODE)
		pattern2 = re.compile(ur'\.', re.UNICODE)
		if pattern1.search(filename):
			filename = pattern1.sub(' ', filename)
		elif pattern2.search(filename):
			filename = pattern2.sub(' ', filename)
	
	#파일이름의 앞뒤 공백 제거
	filename = filename.strip()
	
	#제어문자 제거
	filename = _p_string.removeControlChar(filename)
	#filename = re.sub('[:cntrl:]', ' ', filename, flags=re.UNICODE)
	
	#파일명 합침.
	if considerExtension:
		filename = '.'.join((filename, ext))
	
	#파일명을 반환
	if filename:
		return filename
	return 'Unknown'
	
def dequoteJsStr(jsStr) :
	"""
	자바 스크립트를 위해 콰우팅된 문자열을 콰우팅 해제시킵니다.
	
	:param jsStr: 콰우팅된 자바 스크립트 문자열
	:type jsStr: unicode
	:return: 디콰우팅 된 문자열.\n
		ex) abc\'asd\' -> abc'asd'
	:rtype: unicode
	"""
	REGEXS = [
		(r'\\', '\\'),
		(r"\'", "'"),
		(r'\"', '"'),
		(r'\n', '\n')
	];
	for before, after in REGEXS :
		jsStr = jsStr.replace(before, after)
	return jsStr;

def loadNetscapeCookie(session, cookiePath):
	"""
	Netscape 타입의 쿠키를 가져와서 requests session에 설정합니다.
	
	.. @remark 쿠키 헤더\n
	  # Netscape HTTP Cookie File\n
	  # http://www.netscape.com/newsref/std/cookie_spec.html\n
	  # This is a generated file!  Do not edit.
	
	:param session: requests 세션 객체
	:type session: requests.sessions.Session
	:param cookiePath: 쿠키 파일 경로 문자열
	:type cookiePath: unicode
	"""
	#임시 파일 생성
	with tempfile.NamedTemporaryFile('wb', prefix='.tmp_', suffix='.cookie') as tmpCookie:
		#넷스케이프 헤더 작성
		tmpCookie.write('# Netscape HTTP Cookie File\n')
		tmpCookie.write('# http://www.netscape.com/newsref/std/cookie_spec.html\n')
		tmpCookie.write('# This is a generated file!  Do not edit.\n')
		tmpCookie.write('\n')
		
		#기존 쿠키 파일의 내용을 삽입; 윈도우식 줄바꿈 -> 리눅스식으로 치환.
		with open(cookiePath, 'r') as f:
			buffer = f.read().replace('\r', '\n')
			tmpCookie.write(buffer.encode('UTF-8'))
		tmpCookie.flush()
		
		#쿠키 파일 불러오기
		cookieJar = cookielib.MozillaCookieJar(tmpCookie.name)
		cookieJar.load(ignore_discard=True, ignore_expires=True)
		session.cookies = cookieJar
	pass
