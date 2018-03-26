from flask.json import JSONEncoder
from enum import Enum
import datetime

class AppJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            # Encodes date and time
            if isinstance(obj, datetime.datetime):
                return obj.strftime('%Y-%m-%dT%%H:%M:%SZ')
            elif isinstance(obj, Enum):
                return obj.name
        except TypeError:
            pass
        return JSONEncoder.default(self, obj)