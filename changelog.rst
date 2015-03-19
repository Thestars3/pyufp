변경사항 (ufp)
==============

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
