#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import re
import os.path
import sys

if sys.version_info >= (3,):
	raise RuntimeError('this module not supporting Python 3 yet.')

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = ''
with open('ufp/__init__.py', 'r') as fd:
	reg = re.compile(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]')
	for line in fd:
		m = reg.match(line)
		if m:
			version = m.group(1)
			break
		pass
	pass

if not version:
	raise RuntimeError('Cannot find version information')

extra = dict()
#일부 외부 의존 패키지 때문에 사용 할 수  없음.
#if sys.version_info >= (3,):
    #extra['use_2to3'] = True
    ##extra['convert_2to3_doctests'] = ['src/your/module/README.txt']
    ##extra['use_2to3_fixers'] = ['your.fixers']
    #pass

buffer = read(os.path.join(os.path.dirname(__file__), 'requirements.txt'))
install_requires = filter(lambda x: x != '', buffer.split('\n'))

setup(
	name             = 'ufp',
	version          = version,
	author           = '별님',
	author_email     = 'w7dn1ng75r@gmail.com',
	url              = 'http://thestars3.tistory.com/',
	description      = 'ufp 라이브러리 python 버전. 각종, 편리한 함수들의 모음.',
	packages         = [
			'ufp',
			'ufp._compatibleness',
			'ufp._compatibleness.terminal',
			'ufp._compatibleness.terminal.color',
			'ufp.gui',
			'ufp.terminal',
		],
    package_dir      = {'ufp': 'ufp'},
    package_data     = {
		'': [
			'README.rst',
			'AUTHORS',
			'COPYING'
			]
		},
	zip_safe         = False,
	install_requires = install_requires,
	license          = "GPL v3",
	keywords         = ["path", "web", "html", "string", "image", "gui", "termianl"],
	long_description = read('README.rst'),
	classifiers      = [
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 2 :: Only",
		"Intended Audience :: Developers",
		"Development Status :: 5 - Production/Stable",
		"Environment :: X11 Applications",
		"Environment :: Console",
		"Topic :: Terminals :: Terminal Emulators/X Terminals",
		"Topic :: System :: Shells",
		"Topic :: Utilities",
		"Topic :: Text Processing :: General",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Operating System :: Unix",
		"Operating System :: POSIX",
		"Operating System :: MacOS",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		],
	download_url     = "https://github.com/Thestars3/pyufp/releases",
	platforms        = ['Unix', 'POSIX', 'MacOS'],
	include_package_data = True, # True : MANIFEST.in is used
	**extra
	)
