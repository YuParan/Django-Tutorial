def get_logging_config(project_name, log_dir):
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'stack_info': True,
                'format':
                    '[%(levelname)s]  '
                    '%(process)d:%(processName)s  '
                    '%(asctime)s  '
                    '%(pathname)s:%(lineno)s  '
                    '%(funcName)s()  '
                    '%(message)s  '
            },
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },
            'debug': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': f'{log_dir}/{project_name}-debug.log',
                'maxBytes': 1024 * 1024 * 8,
                'backupCount': 5,
                'formatter': 'standard',
            },
            'request_handler': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': f'{log_dir}/request.log',
                'maxBytes': 1024 * 1024 * 8,
                'backupCount': 5,
                'formatter': 'standard',
            }
        },
        'loggers': {
            'django.db.backends': {
                'handlers': ['console'],
                'level': 'DEBUG'
            },
            'api': {
                'handlers': ['console', 'debug'],
                'level': 'DEBUG',
                'propagate': True
            },
            'django.server': {
                'handlers': ['console', 'request_handler'],
                'level': 'DEBUG',
                'propagate': False
            },
        }
    }
