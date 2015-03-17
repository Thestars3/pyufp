#!/usr/bin/env python
#-*- coding: utf-8 -*-

from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name             = 'ufp',
	version          = read('./version'),
	author           = '별님',
	author_email     = 'w7dn1ng75r@gmail.com',
	url              = 'http://thestars3.tistory.com/',
	description      = 'ufp Python 버전',
	packages         = ['ufp'],
    package_dir      = {'ufp': 'ufp'},
	install_requires = [
		'requests',
		'ANSIColors-balises',
		'PyQt4',
		'trashcli',
		'pillow',
		'chardet',
		'pattern',
		'tidylib'
		],
	license          = "GPL v3.0",
	keywords         = ["path", "web", "html", "string", "image", "gui", "termianl"],
	long_description = read('./README.md'),
	classifiers      = [
		"Programming Language :: Python :: 2",
		"Intended Audience :: Developers",
		"Development Status :: 5 - Production/Stable",
		"Environment :: X11 Applications",
		"Environment :: Console",
		"Topic :: Terminals :: Terminal Emulators/X Terminals",
		"Topic :: System :: Shells",
		"Topic :: Utilities",
		"Topic :: Text Processing :: General",
		"Topic :: Software Development :: Libraries",
		"Operating System :: Unix",
		"Operating System :: POSIX",
		"Operating System :: MacOS",
		"License :: OSI Approved :: GNU General Public License (GPL)",
		],
	download_url     = "https://github.com/Thestars3/pyufp/releases",
	platforms        = ['Unix', 'POSIX', 'MacOS']
	)
