#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import PIL.Image
import PIL.ImageChops
import itertools
import math
import copy

RGB_COLOR_COUNT = 256
GRAYSCALE_COLOR_COUNT = 256 #PIL.Image의 L 모드를 의미.

def quantizeByImprovedGrayScale(image, colorCount=GRAYSCALE_COLOR_COUNT):
	"""
	주어진 이미지에 대해 Improved Gray Scale(IGS) 양자화시킵니다.
	
	이 함수는 원본을 변경시킵니다.
	
	다음과 같은 식으로 사용한다.
		
	.. code-block:: python

		>>> import ufp.image
		>>> import PIL.Image
		>>> im = PIL.Image.open('test.jpg', 'r')
		>>> im = im.convert('L')
		>>> ufp.image.quantizeByImprovedGrayScale(im).save('igs.jpg')
		
	..
	  @link http://stackoverflow.com/questions/14434963/change-number-of-gray-levels-in-a-grayscale-image-in-matlab change number of gray levels in a grayscale image in matlab - Stack Overflow
	  @link http://code.activestate.com/recipes/259112/ Improved Gray Scale Quantization (Python recipe)
	
	:raise ValueError: 사용 불가능한 모드의 이미지를 인자로 준 경우
	:param image: 이미지 객체. 이 이미지는 L 모드여야 합니다.
	:type image: PIL.Image
	:param colorCount: 원본의 색상 수.
		주어진 이미지의 색상 수를 목표로 하는 색상로 맞추는데 사용 할 수도 있습니다. 이 경우, 주어진 모드가 한 채널에서 가질 수 있는 최대 값을 상한선으로 하여, 목표로 하는 색상의 수를 정하십시오.
	:type colorCount: int
	:return: 변경된 이미지 객체
	:rtype: PIL.Image
	"""
	if image.mode != 'L':
		raise ValueError('L 모드의 이미지만 사용 할 수 없습니다.'.format(image.mode))
	
	raito = math.trunc(GRAYSCALE_COLOR_COUNT / colorCount)
	mask = raito - 1
	prev_sum = 0
	pixel = image.load()
	width, height = image.size
	for x in xrange(0, width):
		for y in xrange(0, height):
			value = pixel[x, y]
			if value/raito != mask:
				prev_sum = value + (prev_sum & mask)
			else:
				prev_sum = value
			pixel[x, y] = math.trunc(prev_sum/raito) * raito
			pass
		pass
	return image

def changeColorDepth(image, colorCount):
	"""
	이미지의 색 깊이를 감소시킵니다.
	
	이 함수는 원본을 변경시킵니다.
	
	..
	  @link http://en.wikipedia.org/wiki/List_of_monochrome_and_RGB_palettes List of monochrome and RGB palettes - Wikipedia, the free encyclopedia
	  @link http://stackoverflow.com/questions/14434963/change-number-of-gray-levels-in-a-grayscale-image-in-matlab change number of gray levels in a grayscale image in matlab - Stack Overflow
	
	:raise ValueError: 사용 불가능한 모드의 이미지를 인자로 준 경우
	:param image: PIL.Image 객체.
		L, RGB, RGBA 모드의 이미지를 처리 할 수 있습니다.
	:type image: PIL.Image
	:param colorCount: 결과물의 색상 수.
		주어진 모드가 한 채널에서 가질 수 있는 최대 값을 상한선으로 하여, 목표로 하는 색상의 수를 정하십시오.
	:type colorCount: int
	:return: 변경된 PIL.Image 이미지 객체
	:rtype: PIL.Image
	"""
	if image.mode == 'L':
		raito = GRAYSCALE_COLOR_COUNT / colorCount
		change = lambda value: math.trunc(value/raito)*raito
		return image.point(change)
	
	if image.mode == 'RGB' or image.mode == 'RGBA':
		raito = RGB_COLOR_COUNT / colorCount
		change = lambda value: math.trunc(value/raito)*raito
		return PIL.Image.eval(image, change)
	
	raise ValueError('{mode} 모드의 이미지는 사용 할 수 없습니다.'.format(mode=image.mode))

def mostPopularEdgeColor(image):
	"""
	이미지의 둘레(left,right,top,bottom)에서 가장 많이 나타나는 색깔이 무엇인지 계산한다.
	
	..
	  @link http://coreapython.hosting.paran.com/howto/sebsauvage_net-%20Snyppets%20-%20Python%20snippets.htm#autocrop 이 함수에 대해 참조한 자료가 있는 웹페이지
	
	:param image: PIL 이미지 객체
	:type image: PIL.Image
	:returns: 가장 많은 색상(정수 튜플 (R,G,B))
	:returns: L 모드 이미지인 경우 가장 많은 색상(정수)를 반환합니다.
	"""
	if image.mode not in ['RGB', 'L']:
		image = image.convert("RGB")
		pass
	
	# 이미지의 둘레에서 픽셀을 얻는다:
	width,height = image.size
	left   = image.crop((0, 1, 1, height-1))
	right  = image.crop((width-1, 1, width, height-1))
	top    = image.crop((0, 0, width, 1))
	bottom = image.crop((0, height-1, width, height))
	pixels = left.tostring() + right.tostring() + top.tostring() + bottom.tostring()
	
	if image.mode == 'RGB':
		# 어떤 RGB 삼중원소가 가장 많은지 계산한다
		counts = dict()
		for i in xrange(0, len(pixels), 3):
			rgb = pixels[i] + pixels[i+1] + pixels[i+2]
			if rgb in counts:
				counts[rgb] += 1
			else:
				counts[rgb] = 1
				pass
			pass
		
		# 가장 많은 색깔을 얻는다:        
		mostPopularColor = sorted([(count, rgba) for (rgba, count) in counts.items()], reverse=True)[0][1]
		r = ord(mostPopularColor[0])
		g = ord(mostPopularColor[1])
		b = ord(mostPopularColor[2])
		return (r, g, b)
	
	if image.mode == 'L':
		buffer = map(lambda i: ord(pixels[i]), xrange(0, len(pixels)))
		buffer = list(itertools.groupby(buffer))
		buffer.sort(key=lambda x: len(list(x[1])), reverse=True)
		return buffer[0][0]
	pass

def trim(image, backgroundColor=None, fuzz=0):
	"""
	이미지 주위에 있는 여백을 제거한다.
	
	이미지에 알파 채널이 있으면, 그것을 사용하여 무엇을 자를지 고른다. 그렇지 않으면, 이미지 둘레에서 가장 많은 색상을 찾으려고 시도한다. 그리고 이 색상을 여백으로 간주한다. (backgroundColor 매개변수로 이 색상을 오버라이드할 수 있다.)
	
	다음과 같은 식으로 사용한다.
	
	.. code-block:: python

		>>> import ufp.image
		>>> import PIL.Image
		>>> im = PIL.Image.open('test.jpg', 'r')
		>>> ufp.image.trim(im, fuzz=13.3).save('trim.jpg')
		
	.. warning:: fuzz옵션 사용시, 이미지가 여백과 유사한 색상일 경우 이미지의 경계를 넘어 이미지까지 잘리는 문제가 생길 수 있다.
	.. warning:: fuzz옵션 사용시, 여백에 잡음이 존재하는 경우 여백을 넘어 이미지를 자를 수 있습니다.
	
	:raise ValueError: fuzz값이 잘못된 경우
	:raise ValueError: 주어진 이미지가 처리 불가능한 모드인 경우
	
	..
	  @link http://coreapython.hosting.paran.com/howto/sebsauvage_net-%20Snyppets%20-%20Python%20snippets.htm#autocrop 이 함수에 대해 참조한 자료가 있는 웹페이지
	  @link http://stackoverflow.com/questions/10615901/trim-whitespace-using-pil 이 함수에 대해 참조한 자료가 있는 웹페이지
	  @link https://pillow.readthedocs.org/reference/ImageChops.html Pillow 사용자 문서 - ImageChops 모듈 API
	
	:param image: (PIL 이미지 객체) 다듬을 이미지.
		알파 채널이 포함된 이미지 또는, RGB, L 형식의 이미지만 처리 할 수 있습니다.
	:type image: PIL.Image
	:param backgroundColor: "다듬을 배경"으로 간주될 색상(RGB: 3개의 정수가 담긴 터플).
		예컨데, tuple(0,0,255)와 같은 형식으로 주어야 합니다. 이미지가 투명이면, 이 매개변수는 무시된다. 이미지가 투명이 아니고 이 매개변수가 주어지지 않으면, 자동으로 계산된다. 만약, L 모드라면 정수를 줘야 한다.
	:param fuzz: float 또는 int형(0~99.9). 배경색과 다른 색상을 동일하게 취급하는 정도를 설정합니다.
	:type fuzz: int, float
	
	:return: PIL.Image 객체.
	:return: 변경될 내용이 없는 경우, 원본을 반환합니다.
	:rtype: PIL.Image
	"""
	bbox = None
	
	#fuzz값 체크
	if not isinstance(fuzz, (float, int)) or not 0 <= fuzz or not fuzz <= 99.9:
		raise ValueError('fuzz에는 오직 0~99사이의 int 또는 float만 사용 할 수 있습니다.')
	
	#이미지에 투명 레이어가 있으면, 그걸 사용한다.
	if 'A' in image.getbands():
		#이는 투명 레이어가 있는 모든 모드에 작동한다
		buffer = image.getbands()
		buffer = list(buffer).index('A')
		buffer = image.split()[buffer]
		bbox = buffer.getbbox()
	#RGB 모드인 경우
	elif image.mode in ['RGB', 'L']:
		if not backgroundColor:
			backgroundColor = mostPopularEdgeColor(image)
			pass
		bg = PIL.Image.new(image.mode, image.size, backgroundColor) # 불투명 이미지를 다듬는다. .getbbox()는 언제나 검정색을 다듬는다. 그래서 이미지에서 "배경색"을 빼줄 필요가 있다.
		diff = PIL.ImageChops.difference(image, bg)  # 이미지에서 배경색을 뺀다.
		
		#차이를 감소시킨다.
		if fuzz > 0:
			if image.mode == 'L':
				max_ = GRAYSCALE_COLOR_COUNT
			else:
				max_ = RGB_COLOR_COUNT
			offset = - math.trunc(max_*fuzz/100)
			diff = PIL.ImageChops.add(diff, diff, 2.0, offset)
			pass
		
		bbox = diff.getbbox()  # 이미지의 진짜 둘레를 찾는다.
	else:
		raise ValueError('{mode} 모드의 이미지는 처리가 불가능 합니다.'.format(mode=image.mode))
	
	if bbox:
		image = image.crop(bbox)
		pass
	
	return image
