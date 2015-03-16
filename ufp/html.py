#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess
import tidylib
import tempfile
import os
import pattern.web

def clean(html, inputEncoding = "utf8") :
	"""
	@brief html 문서를 보다 규격화된 xhtml로 변환합니다.
	@link http://tidy.sourceforge.net/docs/quickref.html HTML Tidy 설정 옵션 빠른 참조
	@link http://countergram.com/open-source/pytidylib/docs/index.html#small-example-of-use Html Tidy에 관한 파이썬 인터페이스 pytidylib.moudule
	"""
	tidyOptions = {
		"output-xhtml": True, #"output-xml" : True
		"quiet": True,
		"show-errors": 0,
		"force-output": True,
		"numeric-entities": True,
		"show-warnings": False,
		"input-encoding": inputEncoding,
		"output-encoding": "utf8",
		"indent": False,
		"tidy-mark": False,
		"wrap": 0
		};
	document, errors = tidylib.tidy_document(html, options = tidyOptions)
	return document

def toText(html, converter='pattern.web') :
	"""
	@brief html 문서를 텍스트 문서로 변환합니다.
	
	@param html 원본 html 텍스트
	@param converter 변환에 사용할 변환기\n
		w3m : w3m 외부 프로그램을 불러와 작업을 하기 때문에 속도가 상당히 느립니다.\n
		pattern.web : pattern(http://www.clips.ua.ac.be/pattern) 라이브러리를 사용합니다. (10개 초과의 공백라인은 자동으로 10개의 공백라인으로 치환됩니다. 앞 뒤 공백은 자동으로 제거됩니다.)
	
	@throw ValueError 지원하지 않는 변환기를 입력 한 경우
	
	@return text
	"""
	if converter == 'w3m':
		tempPath = tempfile.mkstemp(prefix='.tmp_', suffix='.html')[1]
		with open(tempPath, 'w+b') as temp:
			temp.write(html)
			pass
		cmd = ['w3m', '-cols', '98304', '-dump' ,tempPath]
		text = subprocess.check_output(cmd)
		os.remove(tempPath)
		return text
	
	if converter == 'pattern.web':
		text = pattern.web.plaintext(html, linebreaks=10, indentation=True)
		return text
	
	raise ValueError("'{0}'는 지원하지 않는 변환기입니다.".format(converter))
