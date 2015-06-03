#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import cookielib

from .QNetworkCookie import toPyCookie

def toPyCookieJar(QtCookieJar):
	"""
	qt 쿠키 묶음을 python 쿠키 묶음으로 바꿉니다.
	
	.. 참조: 
		http://pyqt.sourceforge.net/Docs/PyQt4/qnetworkcookiejar.html
		https://github.com/jeanphix/Ghost.py/blob/dev/ghost/ghost.py
	
	:param QtCookieJar: qt 쿠키 묶음.
	:type QtCookieJar: :py:class:`PyQt4.QtNetwork.QNetworkCookieJar`
	:return: python 쿠키 묶음.
	:rtype: :py:class:`cookielib.CookieJar`
	"""
	PyCookieJar = cookielib.CookieJar()
	for c in QtCookieJar.allCookies():
		PyCookieJar.set_cookie(toPyCookie(c))
	return PyCookieJar
