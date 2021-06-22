## Copy this file to a new file in settings/ and valorize it with your
## settings

from settings.defaults import *

# Logging
LOGGING['loggers']['base']['handlers'].append('dev_file')
LOGGING['handlers']['file']['filename'] = '/path/to/file.log'
LOGGING['handlers']['dev_file']['filename'] = '/path/to/file_dev.log'

# Database
DATABASE = {
    'NAME': 'db_name',
    'USER': 'user_name',
    'PASSWORD': 's3cr3t',
    'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
    'PORT': '3306',
}
