#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess
import tempfile
import pattern.web
import tidylib

def clean(html, inputEncoding = "utf8") :
	"""
	html 문서를 보다 규격화된 xhtml로 변환합니다.
	
	:param html: html 내용
	:type html: unicode, str
	:param inputEncoding: 입력 문자열의 인코딩
	:type inputEncoding: unicode
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

def toText(html, converter='pattern.web', linebreaks=10, strip=False) :
	"""
	html 문서를 텍스트 문서로 변환합니다.
	
	이 함수는 다음과 같이 사용합니다.
		
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
		pattern.web : pattern(http://www.clips.ua.ac.be/pattern) 라이브러리를 사용합니다.
	:type converter: unicode
	:param linebreaks: 줄바꿈 문자가 이어질 최대 라인 수. '\\\\n'가 linebreaks이상 연속되지 않도록 합니다. 그 이상의 '\\\\n'은 자동으로 제거됩니다. 만약 None으로 설정될 경우 이 옵션은 비활성됩니다. None 또는 1 이상의 값이어야 합니다.
	:type linebreaks: int, None
	:raise ValueError: 지원하지 않는 변환기를 입력 한 경우
	:return: text
	:rtype: unicode
	"""
	if converter == 'w3m':
		with tempfile.NamedTemporaryFile('wb', prefix='.tmp_', suffix='.html') as tempFile:
			tempFile.write(html.encode('UTF-8'))
			tempFile.flush()
			text = subprocess.check_output(['w3m', '-cols', '98304', '-dump', tempFile.name])
		if linebreaks is not None:
			text = pattern.web.collapse_linebreaks(text, linebreaks)
		if strip:
			text = text.strip()
		return text.deocde('UTF-8')
	
	if converter == 'pattern.web':
		html = pattern.web.strip_javascript(html)
		html = pattern.web.strip_inline_css(html)
		html = pattern.web.strip_forms(html)
		html = pattern.web.strip_comments(html)
		html = html.replace("\r", "\n")
		html = pattern.web.strip_tags(html, exclude=[], replace=pattern.web.blocks)
		html = pattern.web.decode_entities(html)
		html = pattern.web.collapse_spaces(html, True)
		text = pattern.web.collapse_tabs(html, True)
		if linebreaks is not None:
			text = pattern.web.collapse_linebreaks(text, linebreaks)
		if strip:
			text = text.strip()
		return text
	
	raise ValueError("'{converter}'는 지원하지 않는 변환기입니다.".format(converter=converter))
