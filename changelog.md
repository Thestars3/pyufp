변경사항
=============

## v1.0.0

+ pyufp 정식 버전 릴리즈.

#### v1.0.1

+ 설치 파일 수정
+ 기존에 터미널을 제어하던 부분에서 ANSIColors-balises을 사용하도록 수정
+ ufp.terminal.color 부분을 호환성 유지를 위한 항목으로 이동

#### v1.0.2

+ 설치 파일 오류 수정

#### v1.0.3

+ 설치 파일 오류 수정

#### v1.0.4

+ 설치 파일 오류 수정

#### v1.0.5

+ 설치 파일 오류 수정

#### v1.0.5b

+ 설치 파일 오류 수정

#### v1.0.5b1

+ 설치 파일 오류 수정

#### v1.0.5b2

+ 설치 파일 오류 수정

#### v1.0.5b3

+ 설치 파일 오류 수정

#### v1.0.5b4

+ 설치 파일 오류 수정

### v1.1.0

+ 자막 파일을 깨끗하게 정리하는 함수를 추가

#### v1.1.1

+ ufp.gui.Notepad 사용시, 창이 무한히 대기하는 현상 수정.
+ ufp.gui 모듈의 PulseProgress, Notepad 사용시 터미널에 불필요한 출력이 발생하지 않도록 수정.

#### v1.1.2

+ ufp.image 모듈의 mostPopularEdgeColor, trim 함수에서 PIL.Image L 모드의 이미지를 처리 할 수 있도록 개선
+ image 모듈의 RGB_MIN_VALUE, RGB_MAX_VALUE, GRAYSCALE_MIN_VALUE, GRAYSCALE_MAX_VALUE 상수를 앞으로 사용하지 않을 것임. 이 변수들을 호환성 유지 부로 이동시킴.
