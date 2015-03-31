#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import subprocess
import struct
import time
import os

_ghostscriptCommand = [
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
	'-dTextAlphaBits=4',
	'-dGraphicsAlphaBits=4',
	'-sOutputFile=%stdout', #출력을 표준출력으로
	'-' #입력을 표준입력에서
	]

def toBmps(pdf, format='bmp16m', dpi=200):
	"""
	pdf 파일을 bmp로 바꾸어 저장합니다.
	
	각 페이지의 bmp는 제너레이터 형식으로 각각 반환됩니다. 예를 들어 다음과 같이 작동합니다.
	
	.. code-block:: python
	
		import ufp.pdf
		
		with open('test.pdf', 'r') as f:
			pdf = f.read()
		
		buffer = ufp.pdf.toBmps(pdf, format='bmp16m')
		for page, bmp in enumerate(buffer, start=1):
			with open('{0}.bmp'.format(page), 'w') as f:
				f.write(bmp)
	
	..
	   비트맵 파일 구조 : http://yagi815.tistory.com/242
	   enumerate 내장 함수 설명 : https://docs.python.org/2/library/functions.html#enumerate
	
	:param pdf: pdf 바이너리 데이터.
		여러 페이지가 포함된 파일도 허용합니다.
	:type pdf: bytes
	:param format: 출력 포멧.\n
		bmp16m: 24-bit RGB Color\n
		bmpmono: Black-and-White Color\n
		bmpgray: Grayscale Color\n
		bmpsep1:\n
		bmpsep8:\n
		bmp16: 4-bit Color\n
		bmp256: 8-bit Color\n
		bmp32b: 32-bit RGBA Color
	:type format: unicode
	:param dpi: DPI.
		기본값은 200DPI입니다.
		양의 정수만을 취합니다.
	:type dpi: int
	:raise Exception: pdf 변환에 문제가 발생했을때.
	:yield: BMP 이미지 바이너리 데이터(bytes)
	"""
	#명령 설정
	cmd = _ghostscriptCommand[:]
	cmd.insert(-2, '-sDEVICE={format}'.format(format=format)) #출력 형식
	cmd.insert(-2, '-r{dpi}x{dpi}'.format(dpi=dpi))  #DPI
	
	try:
		#실행
		devnull = open(os.devnull, 'w')
		gs = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=devnull)
		
		#pdf 파일 입력
		gs.stdin.write(pdf)
		gs.stdin.close()
		
		preBytes = None
		while True:
			#만약 출력 버퍼가 닫겼다면 종료.
			if gs.poll() is not None:
				if gs.returncode != 0:
					raise Exception('pdf -> bmp 변환에 문제가 있습니다.')
				raise StopIteration
			
			# bfType, bfSize 읽어오기
			if preBytes:
				bytes = preBytes + gs.stdout.read(6 - len(preBytes))
				preBytes = None
			else:
				bytes = gs.stdout.read(6)
			
			#못 읽어왔으면 기다렸다 다시 시도
			if len(bytes) != 6:
				time.sleep(0.1)
				preBytes = bytes
				continue
			
			# bfType, bfSize 파싱
			bfType, bfSize = struct.unpack(b'<2sI', bytes)
			
			if bfType != 'BM':
				raise Exception('pdf -> bmp 변환에 문제가 있습니다.')
			
			#bmp 파일 작성
			bmp = bytes
			bmp += gs.stdout.read(bfSize-6)
			
			#값을 반환
			yield bmp
	except GeneratorExit:
		if gs.poll() is not None:
			gs.terminate()
		devnull.close()
	pass

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
		오직 1 페이지만 존재하는 pdf 데이터여야 합니다.
	:type pdf: bytes
	:param format: 출력 포멧.\n
		bmp16m: 24-bit RGB Color\n
		bmpmono: Black-and-White Color\n
		bmpgray: Grayscale Color\n
		bmpsep1:\n
		bmpsep8:\n
		bmp16: 4-bit Color\n
		bmp256: 8-bit Color\n
		bmp32b: 32-bit RGBA Color
	:type format: unicode
	:param dpi: DPI.
		기본값은 200DPI입니다.
		양의 정수만을 취합니다.
	:type dpi: int
	:raise Exception: pdf 변환에 문제가 발생했을때.
	:return: BMP 이미지 바이너리 데이터
	:rtype: bytes
	"""
	cmd = _ghostscriptCommand[:]
	cmd.insert(-2, '-sDEVICE={format}'.format(format=format)) #출력 형식
	cmd.insert(-2, '-r{dpi}x{dpi}'.format(dpi=dpi))  #DPI
	devnull = open(os.devnull, 'w')
	gs = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=devnull)
	bmp = gs.communicate(pdf)[0]
	devnull.close()
	if gs.returncode != 0:
		raise Exception('pdf -> bmp 변환에 문제가 있습니다.')
	return bmp
	