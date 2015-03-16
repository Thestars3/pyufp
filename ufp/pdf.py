#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess

def toBmp(pdf, format='BMP32B', dpi=200):
	"""
	@brief pdf 파일을 bmp로 바꾸어 저장합니다.
	
	@note 참조 :\n
		고스트 스크립트 문서 : http://www.ghostscript.com/doc/current/Readme.htm
	
	@param pdf pdf 바이너리 데이터
		오직 낱장(1 페이지)만 존재하는 pdf 데이터여야 합니다.
	@param format 출력 포멧\n
		BMP16M: 24-bit RGB Color\n
		BMPMONO: Black-and-White Color\n
		BMPGRAY: Grayscale Color\n
		BMPSEP1:\n
		BMPSEP8:\n
		BMP16: 4-bit Color\n
		BMP256: 8-bit Color\n
		BMP32B: 32-bit RGBA Color (기본값)
	@param dpi DPI\n
		기본값은 200DPI입니다.\n
		양의 정수만을 취합니다.
	
	@return BMP 이미지 바이너리 데이터
	"""
	cmd = [
		'gs',
		'-q',
		'-dQUIET',
		'-dSAFER',
		'-dBATCH',
		'-dNOPAUSE',
		'-dNOPROMPT',
		'-dMaxBitmap=500000000',
		'-dAlignToPixels=0',
		'-dGridFitTT=2',
		'-dUseCropBox', # PDF 페이지 박스 내의 내용만 저장
		'-sDEVICE={0}'.format(format), #출력 형식
		'-dTextAlphaBits=4',
		'-dGraphicsAlphaBits=4',
		'-r{0}x{0}'.format(dpi), #DPI
		'-sOutputFile=%stdout', #출력을 표준출력으로
		'-', #입력을 표준입력에서
		]
	process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	bmp = process.communicate(inData)[0]
	
	return bmp
	