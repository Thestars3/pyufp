변경사항
==============

v1.14
-------

+ ufp.path 모듈에 remove_all_content 함수를 추가. [`tb69wn6127`_]
+ ufp.path.listdir 함수에서 pattern을 string으로 지정할시 발생하던 'sre_constants.error: bogus escape (end of line)' 오류 수정. [`tb69wn6127`_]
+ ufp.path.remove 함수를 통해 심볼릭 링크가 있는 경로를 지우려 할 경우 발생하던 'OSError: Cannot call rmtree on a symbolic link' 오류를 수정. [`tb69wn6127`_]
+ ufp.path.mtime 함수에서 발생하던 "AttributeError: 'module' object has no attribute 'fromtimestamp'" 오류 수정. [`tb69wn6127`_]
+ ufp.process 모듈을 추가함. [`tb69wn6127`_]
	+ pgrep 함수 추가됨. [`tb69wn6127`_]
	+ pkill 함수 추가됨. [`tb69wn6127`_]
	+ nohup 함수 추가됨. [`tb69wn6127`_]
+ ufp.logging 모듈을 추가함. [`tb69wn6127`_]
	+ StreamLogger 클래스 추가됨. [`tb69wn6127`_]

v1.13.1
-------

+ ufp.repr 모듈의 make_object 함수에서 항상 형식명이 str로 설정되던 버그 수정. [`tb69wn6127`_]

v1.13
-------

+ descriptor 모듈의 CachedProperty 클래스에 is_seted 메소드를 추가함. [`tb69wn6127`_]
+ repr 모듈을 추가. [`tb69wn6127`_]
	+ ufp.make_repr 함수를 repr 모듈에 make_object라는 이름으로 이동. [`tb69wn6127`_]
	+ make_type 함수를 추가. [`tb69wn6127`_]

v1.12
-------

+ descriptor 모듈에 cached_property를 추가함. [`tb69wn6127`_]
+ pyqt4 모듈을 추가함. [`tb69wn6127`_]
	+ QNetworkCookie 모듈을 추가함. [`tb69wn6127`_]
		+ toPyCookie 함수 추가함. [`tb69wn6127`_]
	+ QNetworkCookieJar 모듈을 추가함. [`tb69wn6127`_]
		+ toPyCookieJar 함수를 추가함. [`tb69wn6127`_]

v1.11
-------

+ ufp.html 모듈의 toText 함수에 replace 옵션을 추가함. [`tb69wn6127`_]

v1.10.1
-------

+ ufp 모듈의 make_repr 함수에서 발생하던 "ValueError: need more than 1 value to unpack" 오류를 수정. [`tb69wn6127`_]
+ ufp 모듈의 make_repr 함수의 *args 인자가 제거됨. [`tb69wn6127`_]

v1.10
-------

+ ufp 모듈에 make_repr 함수가 추가됨. [`tb69wn6127`_]
+ ufp.descriptor 모듈의 classproperty 함수에서 발생하던 "UnboundLocalError: local variable 'obj' referenced before assignment" 오류 수정. [`tb69wn6127`_]

v1.9.1
-------

+ ufp.html.toText 함수에서 converter를 w3m으로 사용시 발생하던 "AttributeError: 'str' object has no attribute 'deocde'"오류 수정. [`tb69wn6127`_]

v1.9
-------

+ ufp.random 모듈에 bytes함수를 추가. [`tb69wn6127`_]
+ ufp.web.trimFilename 함수에 유니코드 문자열을 전달 할시 발생하던 UnicodeDecodeError 오류 수정. [`tb69wn6127`_]
+ ufp.bs4 모듈을 추가. [`tb69wn6127`_]
	+ copy 함수를 추가. [`tb69wn6127`_]
	+ deepcopy 함수를 추가. [`tb69wn6127`_]

v1.8.1
-------

+ ufp.web 모듈의 trimFilename 함수의 **option인자를 그대로 노출 하도록 수정. [`tb69wn6127`_]
+ ufp.web 모듈의 trimFilename 함수 사용시, 전달되는 filename 인자에 퍼센트 인코딩된 문자열이 존재하는 경우 정상적으로 디콰우팅하지 못하던 점 버그 수정. [`tb69wn6127`_]
+ ufp.web 모듈의 trimFilename 함수에서 filename 인자로 전달되는 값의 타입에 대해 보다 명확하게 처리하도록 개선. [`tb69wn6127`_]

v1.8
-------

+ ufp.math 모듈 추가함. [`tb69wn6127`_]
+ ufp.math 모듈에 rshift함수 추가함. [`tb69wn6127`_]
+ ufp.list 모듈에 preallocate 함수 추가함. [`tb69wn6127`_]

v1.7.1
-------

+ ufp 모듈의 cleanSubtitle 함수에 type 매개변수를 추가. [`tb69wn6127`_]
+ smi 파일에 sami태그가 빠진 경우 추가시켜 주도록 함. [`tb69wn6127`_]

v1.7.0
-------

+ list 모듈을 추가함. [`tb69wn6127`_]
+ descriptor 모듈을 추가함. [`tb69wn6127`_]

v1.6.1
-------

+ ufp.path 모듈의 mergeDir, moveAllContent 함수 사용시 중복 회피 처리되지 않던 점 수정. [`tb69wn6127`_]

v1.6.0
-------

+ ufp.path 모듈의 listdir 함수에서 발생하던 "UnboundLocalError: local variable 'pattern' referenced before assignment" 오류 수정. [`tb69wn6127`_]
+ ufp.path 모듈의 moveAllContent 함수 사용시, 이름이 충돌하는 파일은 자동으로 중복 회피된 새 이름으로 옮기도록 함. [`tb69wn6127`_]
+ ufp.path 모듈에 mergeDir 함수를 추가함. [`tb69wn6127`_]

v1.5.1
-------

+ tempfile.mkstemp로 생성한 파일 디스크립터가 닫기지 않았던 버그 수정. [`tb69wn6127`_]
+ 'UnicodeEncodeError: 'ascii' codec can't encode character' 버그 수정. [`tb69wn6127`_]
+ ufp.html.toText 함수에서 converter 옵션을 'w3m'으로 할 경우, 반환되는 텍스트가 bytes이던 점 수정. [`tb69wn6127`_]

v1.5.0
-------

+ ufp.dict 모듈에 Lazy 클래스를 추가함. [`tb69wn6127`_]
+ ufp.terminal.debug 모듈의 print_ 함수에서 '[디버그]'라 출력되는 문구를 '[DEBUG]'문구로 수정. [`tb69wn6127`_]

v1.4.0
-------

+ ufp.dict 모듈을 추가함. [`tb69wn6127`_]
+ ufp.shell에 pgrep 함수를 추가함. [`tb69wn6127`_]

v1.3.3
-------

+ ufp.html 모듈의 toText 함수에 linebreaks, strip 옵션을 추가함. [`tb69wn6127`_]
+ ufp.html 모듈의 toText 함수의 linebreaks 옵션이 None일 경우, pattern.web 변환기의 경우에도 작동하지 않도록 수정. [`tb69wn6127`_]
+ ufp.html 모듈의 toText 함수에서 converter가 pattern.web으로 지정되더라도 strip옵션이 False면 앞 뒤 공백을 제거하지 않도록 수정. [`tb69wn6127`_]

v1.3.2
-------

+ ufp.terminal.debug 모듈의 print 함수에서 발생하던 'SyntaxError: invalid syntax' 수정. [`tb69wn6127`_]
+ ufp.terminal.debug 모듈의 print 함수의 이름을 print_로 변경. [`tb69wn6127`_]
+ ufp.terminal.debug 모듈의 print 함수에 __builtin__.print 함수의 kwargs를 사용 할 수 있도록 수정. [`tb69wn6127`_]

v1.3.1
-------

+ ufp.gui 모듈의 PulseProgress, Notepad클래스와 ufp.pdf 모듈의 toBmps, toBmp 함수에서 표준에러로 메시지를 출력하지 않도록 수정. [`tb69wn6127`_]

v1.3.0
-------

+ ufp.web 모듈의 trimFilename 함수에서 인코딩 변환이 모두 utf8로 이뤄지던점 수정. [`tb69wn6127`_]
+ ufp.pdf 모듈에 toBmps 함수를 추가함. [`tb69wn6127`_]

v1.2.0
-------

+ ufp.path 모듈에 remove 함수를 추가함. [`tb69wn6127`_]

v1.1.5
-------

+ ufp.web 모듈의 trimFilename 함수에서 발생하던 "AttributeError: 'module' object has no attribute" 오류 수정. [`tb69wn6127`_]
+ ufp.web 모듈의 trimFilename 함수에서 파일 경로에 사용불가능한 문자 치환이 이뤄지지 않던 점 수정. [`tb69wn6127`_]
+ ufp.html 모듈의 clean 함수에서 발생하던 "ValueError: (tidylib) Config: unknown option: s" 오류 수정. [`tb69wn6127`_]
+ ufp.pdf 모듈의 toBmp 함수에서 발생하던 "NameError: global name 'inData' is not defined" 오류 수정. [`tb69wn6127`_]
+ ufp.pdf 모듈의 toBmp 함수에서 변환에 문제가 생겼을시 Exception을 raise하도록 함. [`tb69wn6127`_]

v1.1.4
-------

+ ufp.gui.Notepad class의 write 함수의 입력 허용 타입을 늘렸습니다. unicode외의 타입도 입력 할 수 있습니다. [`tb69wn6127`_]

v1.1.3
-------

+ image 모듈의 mostPopularEdgeColor 함수에서 L 모드의 이미지를 처리할 때 잘못된 색상값을 추출하던 점 수정 [`tb69wn6127`_]
+ image 모듈의 changeColorDepth 함수의 처리 속도를 향상 [`tb69wn6127`_]
+ image 모듈의 quantizeByImprovedGrayScale 힘수의 처리 속도를 향상. [`tb69wn6127`_]
+ image 모듈의 quantizeByImprovedGrayScale 힘수의 버그를 수정. [`tb69wn6127`_]
+ image 모듈의 quantizeByImprovedGrayScale 힘수에 사용 불가능한 모드의 이미지를 인자로 줄 경우 발생하던 예외 메시지를 수정. [`tb69wn6127`_]
+ image 모듈의 quantizeByImprovedGrayScale, changeColorDepth 함수가 원본을 변경하게 됨. [`tb69wn6127`_]
+ ufp 모듈의 cleanSubtitle 함수에서 발생하던 디코딩 에러 수정. [`tb69wn6127`_]

v1.1.2
-------

+ ufp.image 모듈의 mostPopularEdgeColor, trim 함수에서 PIL.Image L 모드의 이미지를 처리 할 수 있도록 개선 [`tb69wn6127`_]
+ image 모듈의 RGB_MIN_VALUE, RGB_MAX_VALUE, GRAYSCALE_MIN_VALUE, GRAYSCALE_MAX_VALUE 상수를 앞으로 사용하지 않을 것임. 이 변수들을 호환성 유지 부로 이동시킴. [`tb69wn6127`_]

v1.1.1
-------

+ ufp.gui.Notepad 사용시, 창이 무한히 대기하는 현상 수정. [`tb69wn6127`_]
+ ufp.gui 모듈의 PulseProgress, Notepad 사용시 터미널에 불필요한 출력이 발생하지 않도록 수정. [`tb69wn6127`_]

v1.1.0
-------

+ 자막 파일을 깨끗하게 정리하는 함수를 추가 [`tb69wn6127`_]

v1.0.5
-------

+ 설치 파일 오류 수정 [`tb69wn6127`_]

v1.0.4
------

+ 설치 파일 오류 수정 [`tb69wn6127`_]

v1.0.3
------

+ 설치 파일 오류 수정 [`tb69wn6127`_]

v1.0.2
------

+ 설치 파일 오류 수정 [`tb69wn6127`_]

v1.0.1
------

+ 설치 파일 수정 [`tb69wn6127`_]
+ 기존에 터미널을 제어하던 부분에서 ANSIColors-balises을 사용하도록 수정 [`tb69wn6127`_]
+ ufp.terminal.color 부분을 호환성 유지를 위한 항목으로 이동 [`tb69wn6127`_]

v1.0.0
------

+ pyufp 정식 버전 릴리즈. [`tb69wn6127`_]

.. _tb69wn6127: https://github.com/tb69wn6127
