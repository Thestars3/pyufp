설치
============

.. note:: ufp 모듈이 지원하는 파이썬 버전은 2.7입니다.

.. note:: ufp 모듈이 지원하는 운영체제는 Linux / Unix / MaxOS / POSIX 계열입니다.

의존 패키지 설치
-------------------

ufp 모듈을 사용하기 위해서는 다음 외부 패키지가 필요합니다.

데비안 계열인 경우 필요 패키지를 설치하기 위해, 다음 명령을 쉘에서 실행시키십시오.

.. code-block:: sh

	$ sudo apt-get install w3m kate ghostscript zenity python-qt4 python-tidylib

레드헷인 경우 필요 패키지를 설치하기 위해, 다음 명령을 쉘에서 실행시키십시오.

.. code-block:: sh

	$ sudo yum install w3m kate ghostscript zenity python-qt4 python-tidylib
	
그외의 경우, 각자의 환경에 알맞는 방법으로 다음 패키지를 설치하십시오. w3m, kate, ghostscript, zenity, python-qt4, python-tidylib

ufp 모듈 설치
-----------------

**pip** 명령을 통해 설치하려면, 다음 명령을 쉘에서 실행시키십시오.

.. code-block:: sh

    $ pip install ufp

또는 `PyPI에 올려진 모듈 묶음`_을 다운받아 압축을 해제한뒤 압축을 해제한 폴더에서 다음 명령을 실행하십시오.

.. code-block:: sh

    $ python setup.py install
    
구 버전
------------

구 버전은 `PyPI`_ 에서 받을 수 있습니다.

.. _PyPi: https://pypi.python.org/pypi/ufp

또는 `Github`_ 에서도 받을 수 있습니다.

.. _Github: https://github.com/Thestars3/pyufp
