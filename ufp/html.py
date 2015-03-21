#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess
import tempfile
import os
import pattern.web
import tidylib

def clean(html, inputEncoding = "utf8") :
	"""
	html 문서를 보다 규격화된 xhtml로 변환합니다.
	
	:param html: html 내용
	:type html: unicode, str
	:param inputEncoding: 입력 문자열의 인코딩
	:type inputEncoding: unicode, str
	:returns: xhtml 문서
	:rtype: unicode
	.. 
	  @link http://tidy.sourceforge.net/docs/quickref.html HTML Tidy 설정 옵션 빠른 참조
	  @link http://countergram.com/open-source/pytidylib/docs/index.html#small-example-of-use Html Tidy에 관한 파이썬 인터페이스 pytidylib.moudule
	"""
	options = {
		str("output-xhtml"): True, #"output-xml" : True
		str("quiet"): True,
		str("show-errors"): 0,
		str("force-output"): True,
		str("numeric-entities"): True,
		str("show-warnings"): False,
		str("input-encoding"): inputEncoding,
		str("output-encoding"): "utf8",
		str("indent"): False,
		str("tidy-mark"): False,
		str("wrap"): 0
		};
	document, errors = tidylib.tidy_document(html, options=options)
	return document

def toText(html, converter='pattern.web') :
	"""
	html 문서를 텍스트 문서로 변환합니다.
	
	이 함수는 다음과 같이 사용한다.
		
	.. code-block:: python

		>>> import ufp.html
		>>> import requests
		>>> html = requests.get('http://www.gnu.org/licenses/').content
		>>> ufp.html.toText(html.decode('utf8'))
		u"Licenses\\n- GNU Project - Free Software Foundation\\n\\n\\n ...

	:param html: 원본 html 텍스트
	:type html: unicode
	:param converter: 변환에 사용할 변환기\n
		w3m : w3m 외부 프로그램을 불러와 작업을 하기 때문에 속도가 상당히 느립니다.\n
		pattern.web : pattern(http://www.clips.ua.ac.be/pattern) 라이브러리를 사용합니다. (10개 초과의 공백라인은 자동으로 10개의 공백라인으로 치환됩니다. 앞 뒤 공백은 자동으로 제거됩니다.)
	:type converter: unicode
	:raise ValueError: 지원하지 않는 변환기를 입력 한 경우
	:return: text
	:rtype: unicode
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
