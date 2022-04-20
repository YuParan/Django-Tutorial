---

# Django-Template

Python Django (3.2.6 LTS) 프레임워크를 활용해 빠르게 서버를 띄울 수 있도록 만들어 둔 Django-Template 입니다.

여기까지의 세팅이 이루어진 과정은 [장고 튜토리얼 repository](https://github.com/YuParan/Django-Tutorial) 를 참고 바랍니다.

---

## 개요

### 기본적인 구성

- 주요 파라미터는 `environments.yaml` 을 참조 하도록 구성 (at `settings.py` & `RunServer(with docker)`)
  
  docker 는 프로젝트 경로와 컨테이너 내부를 Bind-Mount 하여 코드 동기화
  
- rest_framework, corsheaders(CORS) 를 포함한 django settings.py

- HealthCheck API 를 포함하여, 기본적인 URL-parameter, JSON, Form-Data(File) 포멧의 Request parameter 입력에 대응하는 SampleAPI 구성
  
  - Response 포맷 통일
    
    `{'code': status_code, 'message': message, 'payload': payload}`

---

## 초기 실행

### Dependency

```
Django==3.2.6
djangorestframework==3.12.4
django-cors-headers==3.10.0
pyyaml
Pillow==8.3.2  # 이미지 처리 예시를 위한 라이브러리
pandas==1.4.0  # CSV 처리 예시를 위한 라이브러리
numpy==1.22.2
```

### Skeleton

```
└── django-template
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
!   │   ├── response.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    │
    ├── /bin
    │   ├── build_docker_image.sh
    │   ├── docker_run_container.sh
    │   ├── docker_stop_container.sh
    │   ├── pip.conf
    │   ├── run_dev_server.sh
    │   └── yaml_reader.sh
    │
    ├── /common
    │   ├── /logs
    │   ├── /media
    │   └── /static
    │
!   ├── /nameless_server
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
    ├── Dockerfile
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
  
  프로젝트 이름을 커스텀하려면 environments.yaml 에 작성된 Project Name 을 변경한 뒤, IDE 를 활용해 `nameless_server` 를 모두 찾아 변경하는것을 권장합니다

- 프로젝트의 이름에 따라 `/api/response.py` 파일에 작성된 Response Class (탬플릿에선 `NamelessServer_Response`) 의 이름을 변경하는 것을 권장합니다.

---

## Run

서버 실행을 위한 명령어

### Python 가상환경에서 개발서버 구동
```
# environments.yaml 의 server 파라미터를 참조하여 서버 구동
./bin/run_dev_server.sh
```

### Docker Container 로 구동
```
# Docker Image 빌드
./bin/build_docker_image.sh
# Container 실행
./bin/docker_run_container.sh
# Container 중지
./bin/docker_stop_container.sh
```

---
