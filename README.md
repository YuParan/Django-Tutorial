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
2. **CMD 'django-admin startproject nameless_server .'** ←
3. 서버 실행을 위한 환경변수 설정 (with yaml)
4. Logger 세팅
5. static & media URL/Directory 세팅
6. CORS, django-restframework 세팅
7. Health Check API
8. Runserver.sh Script 작성
9. CMD "django-admin startapp api"
10. API 작성을 위한 세팅
11. Sample-API 작성

### 2. CMD 'django-admin startproject nameless_server .'

장고 프로젝트 시작을 위한 첫번째 명령어 입니다

```shell
django-admin startproject {{프로젝트 이름}} .
# 프로젝트 이름은 snake_case 로 적절히 지정하면 됩니다. 
# (튜토리얼에선 'nameless_server' 를 프로젝트 명으로 지정하였습니다)
# 명령어 마지막에 . 을 찍어, 현재 경로에서 프로젝트를 시작합니다
```

명령어를 실행하면 지정된 경로(현재 경로 .)에 장고 프로젝트를 작성할 수 있도록 파일들이 생성됩니다.

> 현재 커밋에선 `django-admin startproject {{프로젝트 이름}} .` 명령어 실행에 따른 변경 사항과 </br>
> nameless_server/settings.py 파일 내부의 `SECRET_KEY` 파라미터의 대치, </br>
> README 가이드의 수정만을 포함하고 있습니다.

커밋의 변경사항을 토대로

- 새로 생성된 장고 프로젝트 파일들이 어떤 것들인지
- `django-admin startproject {{프로젝트 이름}} .` 명령어에 작성된 `프로젝트 이름`이 어떤 곳에 적용이 되는지

파악해보시면, Django 프로젝트의 구조를 이해하는데 도움이 될 수 있습니다.

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
    ├── .gitignore
    ├── manage.py
    ├── README.md
    └── requirements.txt
```

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