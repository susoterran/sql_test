## 개요

MySQL/MariaDB 에서 테스트 목적으로 사용할 대용량 더미 데이터를 생성하기 위해 만들었다.

## 사용 방법

### 환경
- CentOS 7
- Python 3.6
- MySQL 5.6

### 테이블 생성 순서

- 데이터베이스 생성
    - 파이썬 코드 상에선 data 데이터베이스 생성하여 테스트함 
- tb_area
- tb_affiliation
- tb_school
- tb_student
- tb_grade

### 더미 데이터 생성

- 고등학교 정보는 아래의 링크에서 추출함

<a href="https://www.sen.go.kr/web/services/bbs/bbsList.action?bbsBean.bbsCd=115">서울시 교육청 학교안내</a>

- import_grade.py와 high.xlsx는 같은 위치에 있어야 한다.
    - 다른 지역의 고등학교 목록까지 포함하려 하였으나 서울시 고등학교만 우선 사용하였다.
- import_grade.py를 실행하면 CLI 상에서 메뉴가 나오는데 숫자 순서대로 진행하면 된다.

### 주의사항

- tb_grade 의 경우 실행 환경에 따라 데이터 생성 시간의 차이가 있다.
- VM에서 진행하였을 때 약 1주일 정도 소요되었으며, 중간에 import_grade.py 실행이 끊기지 않도록 주의한다.
