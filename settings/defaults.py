# Since among loggers and handlers levels the one which wins is the highest,
# keep the 'base' logger level to DEBUG (low) and set the desired level in the
# handler to get just the needed logs on a per-handler basis
LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s [%(process)d:%(levelname)s:%(module)s:%(lineno)d] %(message)s'
        },
        'json': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/daemon.log',
            'formatter': 'default',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 7,
        },
        'dev_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/daemon_dev.log',
            'formatter': 'json',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 3
        }
    },
    'loggers': {
        'base': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
