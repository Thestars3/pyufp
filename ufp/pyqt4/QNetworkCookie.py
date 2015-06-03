#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import cookielib

def toPyCookie(QtCookie):
	"""
	qt 쿠키를 python 쿠키로 바꿉니다.
	
	.. 참조: 
		http://pyqt.sourceforge.net/Docs/PyQt4/qnetworkcookie.html
		https://github.com/jeanphix/Ghost.py/blob/dev/ghost/ghost.py
	
	:param QtCookie: qt 쿠키.
	:type QtCookie: :py:class:`PyQt4.QtNetwork.QNetworkCookie`
	:return: python 쿠키.
	:rtype: :py:class:`cookielib.Cookie`
	"""
	port=None
	port_specified=False
	secure=QtCookie.isSecure()
	name=str(QtCookie.name())
	value=str(QtCookie.value())
	v = str(QtCookie.path())
	path_specified = bool( v != "" )
	path = v if path_specified else None
	v = str(QtCookie.domain())
	domain_specified = bool( v != "" )
	domain = v
	domain_initial_dot = v.startswith('.') if domain_specified else None
	v = long(QtCookie.expirationDate().toTime_t())
	# Long type boundary on 32bit platfroms; avoid ValueError
	expires = 2147483647 if v > 2147483647 else v
	rest = {}
	discard = False
	return cookielib.Cookie(0, name, value, port, port_specified, domain, domain_specified, domain_initial_dot, path, path_specified, secure, expires, discard, None, None, rest)
