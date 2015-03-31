소개
===============

**ufp 라이브러리 python 버전. 각종, 편리한 함수들의 모음.**

.. image:: https://pypip.in/version/ufp/badge.png?text=version
    :target: https://pypi.python.org/pypi/ufp/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ufp/badge.png
    :target: https://pypi.python.org/pypi/ufp/
    :alt: Supported Python versions
    
.. image:: https://pypip.in/status/ufp/badge.png
    :target: https://pypi.python.org/pypi/ufp/
    :alt: Development Status
    
.. image:: https://pypip.in/license/ufp/badge.png
    :target: https://pypi.python.org/pypi/ufp/
    :alt: License

특징
-------------------

* PKCS#5 표준 패딩 제거
* html 문서 규격화시키기
* html 문서를 텍스트로 바꾸기
* 그레이 스케일 이미지에 Improved Gray Scale(IGS) 양자화 적용시키기
* 이미지 색상 깊이 바꾸기
* 이미지 가장자리에서 빈도 높게 나타나는 색상 추출하기
* 이미지의 여백 제거하기
* 탐색 깊이 제한하여 재귀적으로 경로 탐색하기
* 폴더의 모든 내용물을 옮기기
* 파일의 최근 수정시각을 지정된 포멧으로된 문자열로 얻기
* 부모 경로와 자식 경로들을 합치기
* 필터링된 디렉토리 내 파일 목록 얻기
* 경로를 url로 바꾸기
* 운영체제의 파일 경로에서 사용 불가능한 문자 대체시키기
* 부모 경로 추출
* 주어진 경로에서 중복되지 않는 유일한 경로 얻기
* 확장자를 제외한 파일명 추출하기
* 파일 경로에서 확장자 추출하기
* pdf파일을 bmp 이미지로 바꾸기
* 램덤 문자열 만들기
* 문자열을 쉘 콰우팅시키기
* 문자열에서 제어 문자 제거하기
* 파일을 휴지통에 버리기
* 웹 파일명을 다듬기
* 자바 스크립트 콰우팅을 콰우팅 해제하기
* requests 세션에 쿠키 파일 불러오기
* 기타 등등...

사용 환경
-------------------

Linux / Unix / MaxOS / POSIX 계열 

사용 예
-------------------

주어진 경로에서 유일한 경로를 생성하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

예제 : http://runnable.com/VQ5dcHQEFNQakHJ3/generate-unique-path-at-filepath-or-dirpath-for-python

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

pdf 파일을 bmp 변환하여 저장하기
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

예제 : http://runnable.com/VQ-PD6EuyEYfeJNo/convert-pdf-to-bmp-for-python

.. code-block:: python

	>>> import ufp.pdf
	>>> with open('page1.pdf') as f:
	>>> 	pdf = f.read()
	>>> for bmp in ufp.pdf.toBmps(pdf, dpi=200):
	>>> 	break
	>>> with open('page1.bmp') as f:
	>>> 	f.write(bmp)
	
이미지의 여백 제거하기
^^^^^^^^^^^^^^^^^^^^^^

예제 : http://runnable.com/VQ5WVo8OIogZ-_hv/trim-image-edge-whitespace-with-fuzz-for-python

.. code-block:: python

	>>> import ufp.image
	>>> import PIL.Image
	>>> im = PIL.Image.open('test.jpg', 'r')
	>>> ufp.image.trim(im, fuzz=13.3).save('trim.jpg')
	
Improved Gray Scale(IGS) 양자화
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

예제 : http://runnable.com/VQ5o_OpMIyQdA6zE/image-quantize-by-improved-gray-scale-for-python

.. code-block:: python

	>>> import ufp.image
	>>> import PIL.Image
	>>> im = PIL.Image.open('test.jpg', 'r')
	>>> im = im.convert('L')
	>>> ufp.image.quantizeByImprovedGrayScale(im).save('igs.jpg')
	
최대 탐색 깊이를 제한하여 탐색
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	>>> import ufp.path
	>>> for root, dirs, files in ufp.path.walk('.', maxDepth=0):
	...		print(root, dirs, files)
	...		
	'.', ['ufp'], []
	
html 문서를 text로 변환
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	>>> import ufp.html
	>>> import requests
	>>> html = requests.get('http://www.gnu.org/licenses/').content
	>>> ufp.html.toText(html.decode('utf8'))
	u"Licenses\\n- GNU Project - Free Software Foundation\\n\\n\\n ...

진행 표시 창 열기
^^^^^^^^^^^^^^^^^

.. code-block:: python

	>>> import ufp.gui
	>>> import time
	>>> a = ufp.gui.PulseProgress('title', 'message')
	>>> a.open(); time.sleep(3); a.close()

도움말
-------------------

다음 문서를 참조 하십시오: http://pyufp.readthedocs.org/index.html.

수정사항
-------------------

`changelog.rst <https://github.com/Thestars3/pyufp/blob/master/changelog.rst>`_ 문서를 참조하세요.

라이센스
-------------------

`GPL v3 <https://github.com/Thestars3/pyufp/blob/master/COPYING>`_

개발자
-------------------

별님 <w7dn1ng75r@gmail.com>

파이썬 환경
-------------------

오직 2.7 버전대에서만 사용 할 수 있습니다.

설치 방법
-------------------

설치 문서를 참조하십시오: http://pyufp.readthedocs.org/installation.html

소스 코드
-------------------

소스 코드는 다음 사이트에 올려져 있습니다: https://github.com/Thestars3/pyufp.
