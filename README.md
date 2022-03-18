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
1. **Repository 초기 세팅** ←
2. CMD "django-admin startproject nameless_server ."
3. 서버 실행을 위한 환경변수 설정 (with yaml)
4. Logger 세팅
5. static & media URL/Directory 세팅
6. CORS, django-restframework 세팅
7. Health Check API
8. Runserver.sh Script 작성
9. CMD "django-admin startapp api"
10. API 작성을 위한 세팅
11. Sample-API 작성

### 1. Repository 초기 세팅

저장소 관리를 위한 초기 세팅입니다.

`.gitignore` 파일을 작성하였고,

장고 서버 개발에 필요한 라이브러리는 `requirements.txt` 에 작성하였습니다.

라이브러리는 `conda install ~~~` 명령어를 사용해 설치할 수 있습니다. </br>
(버전에 따른 의존성에 유의해주세요!)

---

## Skeleton

```
└── django-tutorial
    ├── .gitignore
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