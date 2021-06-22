"""
Define custom log stuff.

"""

import copy
import logging
import json
from pythonjsonlogger.jsonlogger import JsonFormatter

class DatabaseLogHandler(logging.Handler):

    def emit(self, record):
        from .models import Log

        msg = self.format(record)
        project_id = None
        json_msg = {}
        try:
            json_msg = json.loads(msg)
            project_id = json_msg.get('project_id')
        except ValueError as e:
            logmsg = "msg is not in correct json format {}".format(msg)
            logger.warning(logmsg)
        kwargs = {
            'level': record.levelno,
            'msg': msg,
            'project_id': project_id
        }

        Log.objects.create(**kwargs)


class JsonInMessageFormatter(JsonFormatter):
    """This formatter embeds the json as the tail of the message
    attribute preserving in this way the record original format.

    """
    def __init__(self, *args, **kwargs):
        self.msg_in_json = kwargs.pop('msg_in_json', False)
        super().__init__(*args, **kwargs)

    def format(self, record):
        # get the json from its parent
        json_record = super().format(record)

        # remove the 'message' attribute
        if not self.msg_in_json:
            decoded = json.loads(json_record)
            decoded.pop('message', None)
            json_record = json.dumps(decoded)

        # perform a deep copy in order not to affect the original
        # log record which will be passed to other handlers
        record_copy = copy.deepcopy(record)
        record_copy.msg = "{} {}".format(record.getMessage(), json_record)

        return logging.Formatter.format(self, record_copy)
