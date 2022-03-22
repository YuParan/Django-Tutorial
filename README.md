---

# Django-Tutorial

Python Django (3.2.6 LTS) 프레임워크를 활용해 Django Project 를 생성하고,

기본적인 API 서버를 구성한 뒤, Docker-Container 로 배포하는 전 과정을 포함하는

Django 튜토리얼 Repository 입니다.

커밋 로그를 통해 초기 세팅이 어떤 순서로 이루어지는지 파악할 수 있습니다.

---

## 가이드

### 목차

0. 소개
1. Repository 초기 세팅
2. CMD 'django-admin startproject nameless_server .'
3. **서버 실행을 위한 환경변수 설정 (with yaml)** ←
4. Logger 세팅
5. static & media URL/Directory 세팅
6. CORS, django-restframework 세팅
7. Health Check API
8. Runserver.sh Script 작성
9. CMD "django-admin startapp api"
10. API 작성을 위한 세팅
11. Sample-API 작성

### 3. 서버 실행을 위한 환경변수 설정 (with yaml)

보안 관련 사항을 포함한 시스템 환경변수들을 관리하기 편하도록 외부에 yaml 포맷으로 작성합니다.

system 경로의 하위에,
- environments.yaml
- keys.yaml
- keys-sample.yaml

파일들을 생성.
  
- environments.yaml

  ```text
  Django 서버 구동에 필요한 기본적인 시스템 변수들을 작성합니다.
  (프로젝트 이름, 버전, 포트, 언어, TimeZone ... 등)
  * 직접적으로 보안에 영향을 줄 수 있는 
    django-secret-key 및 DB 접속 정보등은 이곳에 작성하지 않습니다 ! 
  ```
  
- keys.yaml

  ```text
  Django 서버 구동에 필요한 시스템 변수들 중 보안이 필요한 것들을 작성합니다.
  (django-secret-key 및 DB 접속 정보 ... 등)
  * gitignore 로 저장소에 올리지 않고 별도 관리 합니다 ! (.gitignore 에 추가)
  ```

- keys-sample.yaml

  ```text
  keys.yaml 과 동일한 구조를 갖지만 내용은 공백문자 처리된 yaml 파일 입니다.
  keys.yaml 은 gitignore 되므로, 추적되지 않는 변경 내용을 파악하기 위해 따로 작성합니다.
  * keys.yaml 변경시, 동일한 구조를 갖도록 상시 관리 합니다 ! 
  ```

---

## Skeleton

```
└── django-tutorial
    ├── /nameless_server
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    │
    ├── /system
!   │   ├── environments.yaml
    │   ├── keys-sample.yaml
*   │   └── keys.yaml
    │
    ├── .gitignore
    ├── manage.py
    ├── README.md
    └── requirements.txt
```
Repository 에는 다음과 같이 `*` 표시된 경로 & 파일들이 빠져있습니다.
( 미 세팅시 서버가 동작하지 않습니다 )
- /system 이하 경로에 `keys.yaml` 세팅 (django-secret-key, DB 및 기타 중요 key 값을 기록)

프로젝트 서버 구성을 위해 `!` 표시된 파일들의 내용 수정이 필요합니다.
- 대부분 시스템 환경 세팅은 environments.yaml 수정으로 변경됩니다.
- Main Project Name 인 settings.py 가 있는 폴더의 이름 (현재는 `/nameless_server`) 은 environments.yaml 에 작성된 server name 과 동일해야 합니다.

---

## Dependency

```
Django==3.2.6
djangorestframework==3.12.4
django-cors-headers==3.7.0
pyyaml
Pillow==8.3.1  # 이미지 처리 예시를 위한 라이브러리
pandas==1.3.1  # CSV 처리 예시를 위한 라이브러리
numpy==1.20.3
```

---

## Run

서버 실행을 위한 명령어

### 개발 서버로 구동
```
# Python 직접 실행
python manage.py runserver 0.0.0.0:5050  # environments.yaml 의 host 와 port 참조
```

---