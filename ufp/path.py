#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function
import os
import re
import urllib
import urlparse
import os.path
import datetime
import shutil

def remove(path, force=False):
	"""
	주어진 경로에 존재하는 대상을 삭제합니다.
	
	심볼릭 링크는 링크를 제거합니다. 
	폴더의 경우 재귀적으로 폴더 내용을 삭제한뒤 폴더를 삭제합니다.
	
	:param path: 삭제 대상의 경로
	:type path: unicode
	:param force: 오류를 무시할지 여부.\n
		True : 오류를 무시함.\n
		False : Exception이 발생하면, 그대로 던짐.
	:type force: bool
	"""
	try:
		if os.path.islink(path):
			os.unlink(path)
		elif os.path.isdir(path):
			shutil.rmtree(path, force)
		else:
			os.remove(path)
	except Exception, e:
		if force:
			return
		raise e
	pass

def walk(top, maxDepth=None, onerror=None, followlinks=False):
	"""
	재귀적으로 경로 탐색하기
	
	'.'를 인자로 주었다면, './a', './b' 순으로 점점 더 깊게 탐색합니다.
	
	이 함수는 다음과 같은 식으로 사용한다.
		
	.. code-block:: python

		>>> import ufp.path
		>>> for root, dirs, files in ufp.path.walk('.', maxDepth=0):
		...		print(root, dirs, files)
		...		
		'.', ['ufp'], []
		
	:param top: 탐색 대상 경로
	:type top: unicode
	:param onerror: 오류가 발생하면, 주어진 주소의 함수를 호출하여 오류 인자를 넘겨줍니다.
	:type onerror: function
	:param followlinks: 심볼릭 링크된 경로를 포함하여 탐색합니다.
	:type followlinks: bool
	:param maxDepth: 탐색 할 최대 깊이.
		0이상의 정수여야 함.\n
		ex) 0 : 지정된 폴더만.
	:type maxDepth: int
	:yield: 현재 탐색 중인 위치(unicode), 폴더 이름([unicode, ...]), 파일 이름([unicode, ...])
	"""
	top = top.rstrip(os.path.sep)
	assert os.path.isdir(top)
	num_sep = top.count(os.path.sep)
	for root, dirs, files in os.walk(top, onerror=onerror, followlinks=followlinks):
		yield root, dirs, files
		if maxDepth is not None and num_sep + maxDepth <= root.count(os.path.sep):
			del dirs[:]
	pass

def remove_all_content(dir, force=False):
	"""
	dir에 존재하는 모든 요소를 삭제합니다.
	
	:param dir: 삭제 할 대상 파일들이 담긴 폴더
	:type dir: unicode
	:param force: 오류를 무시할지 여부.\n
		True : 오류를 무시함.\n
		False : Exception이 발생하면, 그대로 던짐.
	:type force: bool
	"""
	for file in os.listdir(dir):
		remove(file, force=force)
	pass

def moveAllContent(dirPath, destPath):
	"""
	dirPath에 존재하는 모든 파일을 destPath로 옮깁니다.
	
	만약 중복 파일이 존재한다면 자동으로 중복 회피한 이름을 새 이름으로 지정하여 옮깁니다. 중복 회피 대상은 각 디렉토리 바로 아래의 파일들입니다.
	
	:param dirPath: 이동 할 대상 파일들이 담긴 폴더
	:type dirPath: unicode
	:param destPath: 파일들이 옮겨져갈 위치
	:type destPath: unicode
	"""
	for src in listdir(dirPath, fullpath=True):
		#이동 경로 설정
		buffer = os.path.basename(src)
		buffer = os.path.join(destPath, buffer)
		dest = unique(buffer)
		
		shutil.move(src, dest) #이동
	pass

def mergeDir(dirPaths, destPath):
	"""
	dirPaths에 존재하는 모든 파일을 destPath로 옮긴 뒤, dirPath를 삭제합니다.
	
	만약 중복 파일이 존재한다면 자동으로 중복 회피한 이름을 새 이름으로 지정하여 옮깁니다. 중복 회피 대상은 각 디렉토리 바로 아래의 파일들입니다.
	
	:param dirPaths: 이동 할 대상 파일들이 담긴 디렉토리 경로, 또는 디렉토리 경로 목록.
	:type dirPaths: unicode, list(unicode, ...), tuple(unicode, ...)
	:param destPath: 파일들이 옮겨져갈 위치
	:type destPath: unicode
	"""
	if isinstance(dirPaths, unicode):
		dirPaths = [dirPaths]
	
	for dirPath in dirPaths:
		moveAllContent(dirPath, destPath)
		os.rmdir(dirPath)
	pass

def mtime(path, format):
	"""
	path에 해당하는 파일의 최근 수정 시각을 지정된 format형식으로 작성하여 반환합니다.
	
	:param path: 경로 문자열
	:type path: unicode
	:param format: 형식 문자열(datetime strftime에서 지원하는 형식)
	:type format: unicode
	:return: path에 존재하는 파일의 최근 수정 시각의 format에 지정된 형식
	:rtype: unicode
	"""
	buffer = os.path.getmtime(path)
	return datetime.datetime.fromtimestamp(buffer).strftime(format)
	
def pjoin(parentPath, filenames):
	"""
	parentPath를 각 filenames의 아이템과 결합합니다.
	
	:param parentPath: 부모 경로
	:type parentPath: unicode
	:param filenames: 파일명 리스트.
	:type filenames: list(unicode, ...)
	:return: 결합된 리스트.
		[parentPath/filename, parentPath/filename, ...]
	:rtype: list(unicode, ...)
	"""
	result = list()
	for filename in filenames:
		buffer = os.path.join(parentPath, filename)
		result.append(buffer)
		pass
	return result

def listdir(path, **options):
	"""
	지정된 폴더에서 pattern에 해당하는 파일 및 폴더의 목록을 가져옵니다.
	
	:param path: 목록을 가져올 폴더 경로
	:type path: unicode
	:param pattern: 필터 패턴(대소문자를 구분하지 않습니다)\n
		string : 패턴 문자열\n
		[string, ...]: 패턴 문자열 리스트\n
		None: 필터링 하지 않음
	:param patternReverse: \n
		True : 필터에 매칭되지 않는 대상만 얻습니다.\n
		False : 필터에 매칭되는 대상만 얻습니다.
	:type patternReverse: bool
	:param fullpath: 반환시 주어진 경로를 포함한 경로를 반환합니다.\n
		True : [path + filename, ...]\n
		False : [filename, ...]
	:type fullpath: bool
	:param sortKey: 정렬키 함수\n
		해당 함수에는 전체 경로가 전달 됩니다.
	:type sortKey: function
	
	:return: 필터링된 폴더 내용
	:rtype: list(unicode, ...)
	"""
	options.setdefault('pattern', None)
	options.setdefault('patternReverse', False)
	options.setdefault('fullpath', False)
	options.setdefault('sortKey', None)
	
	if options['pattern'] is not None:
		pattern = options['pattern']
		
		#만약 패턴이 문자열이라면 리스트에 담기.
		if isinstance(pattern, unicode):
			pattern = [pattern]
		
		#패턴 컴파일
		pattern = map(lambda x: re.compile(x, re.IGNORECASE), pattern)
	
	#목록 작성
	listdir = list()
	iterator = os.listdir(path)
	#패턴 옵션이 설정된 경우 필터링
	if options['pattern'] is not None:
		for filename in iterator:
			for p in pattern:
				#패턴 역전 옵션이 꺼진 경우
				if p.search(filename) and not options['patternReverse']:
					listdir.append(filename)
					break
				
				#패턴 역전 옵션이 켜진 경우
				if options['patternReverse']:
					listdir.append(filename)
					break
	else:
		listdir.extend(iterator)
	
	#sortKey 옵션이 사용된 경우
	if options['sortKey']:
		key = options['sortKey']
		buffer = lambda x: key(os.path.join(path, x))
		listdir.sort(key=buffer)
	
	#fullpath 옵션이 켜진 경우
	if options['fullpath']:
		listdir = pjoin(path, listdir)
	
	#결과 반환
	return listdir
	
def toUrl(path):
	"""
	path를 file:///형식으로된 주소로 되돌려줍니다.
	
	:param path: 경로 문자열.\n
		ex) ../home/ufp
	:type path: unicode
	:return: file:///형식으로된 주소
	:rtype: unicode
	"""
	buffer = path.encode('UTF-8')
	buffer = urllib.pathname2url(buffer)
	return urlparse.urljoin('file:', buffer)

def replaceSpiecalChar(string, **options) :
	"""
	운영체제의 경로에서 사용 불가능한 문자열을 대체문자로 치환합니다.
	
	윈도우 및 유닉스 계열 운영체제에서 파일에 포함되면 문제가 되는 특수문자를 대체문자로 치환합니다. 경로 구분자를 대체 문자로 치환합니다.
	
	.. note::
		윈도우에서 파일명으로 사용 할 수 없는 문자들(파일 이름에 다음 문자를 사용할 수 없습니다):\n
		\\\\ / : * ? " < > |
	.. note::
		리눅스에서 파일명으로 사용 할 수 없는 문자들(파일 이름에 다음 문자를 사용할 수 없습니다):\n
		/
	
	:param string: 치환 될 문자열
	:tpye string: unicode
	:param **options: \n
		type: u'windows', u'unix'.
		윈도우의 경로 구분 문자는 리눅스에서 표시되는 모양이 다릅니다. 지정된 OS에서 보여지는 문자 모양과 유사한 대체문자로 치환하도록 지정합니다. 기본값은 unix입니다.\n
		keep_path_characters(bool): 경로 구분자를 치환하지 않습니다. 이 설정은 type 설정에 의존합니다. 기본 값은 False입니다.
	:rtype: 
	"""
	UNIX_PATH_CHARACTER_RE = ("/", "／");
	ESCAPE_CHARTER_UNIX_TYPE_RE = ("\\", "＼")
	WINDOWS_PATH_CHARACTER_RE = ("\\", "￦")
	DEFAULT_REGEXS = [
		("?", "？"),
		(":", "："),
		("*", "＊"),
		('"', "＂"),
		("<", "〈"),
		(">", "〉"),
		("|", "│"),
		("'", "＇"),
		("$", "＄"),
		("!", "！")
	]
	
	#옵션 초기값 설정
	options.setdefault('type', 'unix')
	options.setdefault('keep_path_characters', False)
	
	#옵션 처리
	regexs = DEFAULT_REGEXS
	if options['type'] == 'unix':
		regexs.append(ESCAPE_CHARTER_UNIX_TYPE_RE)
		if not options['keep_path_characters']:
			regexs += [UNIX_PATH_CHARACTER_RE]
	elif options['type'] == 'windows':
		regexs += [UNIX_PATH_CHARACTER_RE]
		if not options['keep_path_characters']:
			regexs += [WINDOWS_PATH_CHARACTER_RE]
	
	for before, after in regexs:
		string = string.replace(before, after)
	
	return string

def dirname(path):
	"""
	주어진 경로의 부모 경로를 추출해냅니다.
	
	만약 'abc'가 주어졌다면, 반환값은 '.'입니다.
	
	.. note:: os.path.dirname('asd') -> ''이 되는 문제를 해결하기 위해 만들어졌습니다.
	
	:param path: 경로 문자열.
	:type path: unicode
	:return: 부모 경로
	:rtype: unicode
	"""
	dirnameRe = re.compile(r'(?P<dirname>^.*)/', re.DOTALL | re.UNICODE).search(path);
	if dirnameRe :
		return dirnameRe.group('dirname');
	return '.';

def unique(targetPath, spliteExt = True) :
	"""
	해당 경로에서 유일한 경로를 만들어 냅니다.
	
	대소문자를 구분하지 않습니다. 만약 'a/b/c'를 인자로 준다면, `a/b/c d(1)`식으로 충복을 회피처리한 결과를 반환합니다.
	
	다음과 같은 식으로 사용합니다.
	
	.. code-block:: python
	
		>>> import ufp.path
		>>> import os
		>>> os.listdir('.')
		['test.file']
		>>> ufp.path.unique('./test.file')
		./test (d1).file
		>>> f.open('./test (d1).file', 'w').close()
		>>> ufp.path.unique('./test.file')
		./test (d2).file
	
	:param targetPath: 주어지는 값은 유니코드 문자열이여야 함.
	:type targetPath: unicode
	:return: 만약, 주어진 경로가 충돌하지 않는다면 주어진 경로를 그대로 반환합니다.
	:return: 만약 주어진 경로의 부모 경로가 존재하지 않는다면, 주어진 문자열 그대로 반환합니다.
	:return: 유일한 경로.
	"""
	#경로 분할
	targetDirname = dirname(targetPath)
	targetBasename = os.path.basename(targetPath)
	
	#부모 경로가 존재하는지 확인
	if not os.path.exists(targetDirname):
		return targetPath
	
	#해당 경로의 목록을 작성
	fileList = ['.', '..']
	for dirpath, dirnames, filenames in os.walk(targetDirname):
		fileList.extend(filenames)
		break
		
	#중복되는 대상이 존재하는지 확인
	existDuplicateFile = False;
	buffer = re.escape(targetBasename);
	fullmatchRe = re.compile(r"^{targetBasename}$".format(targetBasename=buffer), re.IGNORECASE | re.UNICODE)
	for fileName in fileList:
		if fullmatchRe.search(fileName):
			existDuplicateFile = True;
			break
		pass
	
	#중복되는 대상이 존재하고 있지 않다면 이름을 그대로 돌려줌.
	if not existDuplicateFile:
		return targetPath;
		
	#파일명과 확장자를 추출
	if spliteExt :
		targetFileExt = extension(targetBasename);
		if targetFileExt :
			targetFileName = filename(targetBasename);
		else :
			targetFileName = targetBasename;
			spliteExt = False;
	else :
		targetFileName = targetBasename;
	
	#중복 파일들의 숫자를 가져옴.
	escapedTargetFileName = re.escape(targetFileName);
	if spliteExt :
		extractDupCountRe = re.compile(r"^{escapedTargetFileName} \(d(?P<number>[0-9]+)\)\.{targetFileExt}$".format(escapedTargetFileName=escapedTargetFileName, targetFileExt=targetFileExt), re.DOTALL | re.IGNORECASE | re.UNICODE);
	else :
		extractDupCountRe = re.compile(r"^{escapedTargetFileName} \(d(?P<number>[0-9]+)\)$".format(escapedTargetFileName=escapedTargetFileName), re.DOTALL | re.IGNORECASE | re.UNICODE);
	counts = [];
	for fileName in fileList :
		m = extractDupCountRe.search(fileName);
		if m :
			buffer = m.group('number')
			buffer = int(buffer)
			counts.append(buffer);
		pass
	
	#중복 숫자를 설정
	if counts :
		counts.sort();
		notDuplicatedNumber = counts[-1] + 1;
	else :
		notDuplicatedNumber = 1;
		
	#중복 회피 이름 생성
	if spliteExt :
		uniqueName = "{targetFileName} (d{notDuplicatedNumber}).{targetFileExt}".format(targetFileName=targetFileName, notDuplicatedNumber=notDuplicatedNumber, targetFileExt=targetFileExt)
	else :
		uniqueName = "{targetFileName} (d{notDuplicatedNumber})".format(targetFileName=targetFileName, notDuplicatedNumber=notDuplicatedNumber)
	
	return os.path.join(targetDirname, uniqueName);

def filename(filePath) :
	"""
	파일 경로로 부터 확장자를 제외한 파일명을 추출해냅니다.
	
	:param filePath: 주어지는 값은 유니코드 문자열이여야 함.\n
		예를 들어, '../asd/.qwe.tar.bz2'가 인자로 주어진 다면 반환값은 '.qwe.tar' 입니다.
	:type filePath: unicode
	:return: 파일 이름
	:rtype: unicode
	"""
	rx = re.compile(r"^(.*/)?(?P<name_space>.+?)?(?P<ext_space>\.[a-z0-9]+)?$", re.DOTALL | re.IGNORECASE | re.UNICODE);
	
	result = rx.search(filePath)
	if not result:
		return unicode()
	
	nameSpace = result.group('name_space');
	if nameSpace :
		return nameSpace;
	
	extSpace = result.group('ext_space')
	if extSpace:
		return extSpace;
		
	return unicode()

def extension(fileName) :
	"""
	주어진 파일명의 확장자를 추출합니다.
	
	:param fileName: 주어지는 값은 유니코드 문자열이여야 함.
	:type fileName: unicode
	:return: '../asd/.qwe'가 인자로 주어진 다면 반환값은 (빈 값) 입니다.
	:return: 만약 확장자가 없다면, (빈 값)을 리턴합니다.
	:rtype: unicode
	"""
	extRe = re.compile(r"[^/]+\.(?P<ext>[a-z0-9]+)$", re.DOTALL | re.IGNORECASE | re.UNICODE);
	result = extRe.search(fileName);
	if result :
		return result.group('ext');
	return unicode();
