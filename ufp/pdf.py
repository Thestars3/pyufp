#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess

def toBmp(pdf, format='bmp32b', dpi=200):
	"""
	pdf 파일을 bmp로 바꾸어 저장합니다.
	
	다음과 같은 식으로 사용합니다.
	
	.. code-block:: python
	
		import pyPdf
		from io import BytesIO
		import ufp.pdf
		
		#PDF 파일을 준비
		buffer = file(srcPath, 'rb')
		pdf = pyPdf.PdfFileReader(buffer)
		
		#각 페이지 마다
		for pageNumber in xrange(pdf.getNumPages()):
			#현재 페이지의 pdf 데이터를 추출
			page = pdf.getPage(pageNumber)
			pdfFileWriter = pyPdf.PdfFileWriter()
			pdfFileWriter.addPage(page)
			with BytesIO() as outputStream:
				pdfFileWriter.write(outputStream)
				pageBinary = outputStream.getvalue()
				pass
			
			#PDF를 BMP(24-bit RGB Color)로 변환
			imageBinary = ufp.pdf.toBmp(pageBinary, format='bmp16m', dpi=200)
			
			#저장
			with open('{0}.bmp'.format(pageNumber), 'w') as f:
				f.write(imageBinary)
			pass
	
	.. 고스트 스크립트 문서 : http://www.ghostscript.com/doc/current/Readme.htm
	
	:param pdf: pdf 바이너리 데이터.
		오직 낱장(1 페이지)만 존재하는 pdf 데이터여야 합니다.
	:param format: 출력 포멧.\n
		bmp16m: 24-bit RGB Color\n
		bmpmono: Black-and-White Color\n
		bmpgray: Grayscale Color\n
		bmpsep1:\n
		bmpsep8:\n
		bmp16: 4-bit Color\n
		bmp256: 8-bit Color\n
		bmp32b: 32-bit RGBA Color (기본값)
	:param dpi: DPI.
		기본값은 200DPI입니다.
		양의 정수만을 취합니다.
	:raise Exception: pdf 변환에 문제가 발생했을때.
	:return: BMP 이미지 바이너리 데이터
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
	bmp = process.communicate(pdf)[0]
	if process.returncode != 0:
		raise Exception('pdf -> bmp 변환에 문제가 있습니다.')
	
	return bmp
	