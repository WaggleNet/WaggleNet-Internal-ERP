from flask.json import JSONEncoder
from enum import Enum
from ..model.db import db
import datetime

class AppJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            # Encodes date and time
            if isinstance(obj, datetime.datetime):
                return obj.strftime('%Y-%m-%dT%%H:%M:%SZ')
            elif isinstance(obj, Enum):
                return obj.name
            elif isinstance(obj, db.Model):
                return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
        except TypeError:
            pass
        return JSONEncoder.default(self, obj)