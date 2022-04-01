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
3. 서버 실행을 위한 환경변수 설정 (with yaml)
4. Logger 세팅
5. static & media URL/Directory 세팅
6. CORS, django-restframework 세팅
7. Health Check API
8. Runserver.sh Script 작성
9. CMD "django-admin startapp api"
10. API 작성을 위한 세팅
11. **Sample-API 작성** ←

### 11. Sample-API 작성

Test 용 Sample API 작성

EndPoints

- api/ample/get_query_string

  Django 에서 GET Request 와 query_parameter parsing 처리를 위한 예시 API
  
  URL query_parameter 형식으로 `parameter` 를 입력받아 내용을 파싱한 후, json 포맷으로 지정한 메시지와 함께 응답


- api/sample/json_api

  Django 에서 json Request 와 그 처리를 위한 예시 API
  
  application/json (raw) 형식으로 `parameter` 를 입력받아 내용을 파싱한 후, json 포맷으로 동일하게 응답


- api/sample/upload_form_data

  Django 에서 파일 Request 와 그 처리를 위한 예시 API

  form-data 형식으로 `parameter` 와 `file` 을 입력받아, 업로드 된 file 의 내부 정보를 응답
            

---

## Skeleton

```
└── django-tutorial
    ├── /api
    │   ├── /migrations
    │   │
    │   ├── /sample
    │   │   ├── get_query_string.py
    │   │   ├── json_api.py
    │   │   └── upload_form_data.py
    │   │
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── response.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── /bin
    │   ├── pip.conf
    │   ├── run_dev_server.sh
    │   └── yaml_reader.sh
    │
    ├── /common
    │   ├── /logs
    │   ├── /media
    │   └── /static
    │
    ├── /nameless_server
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── logger_config.py
    │   ├── settings.py
    │   ├── system_api.py
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
# environments.yaml 의 server 파라미터를 참조하여 서버 구동
./bin/run_dev_server.sh
```

---