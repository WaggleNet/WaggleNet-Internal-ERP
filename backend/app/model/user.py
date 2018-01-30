from .db import db
from ..utils.uuid import gen_uuid

class User(db.Model):
    """
    Stores user records
    """
    id = db.Column(db.String(40), primary_key=True, default=gen_uuid)
    role = db.Column(db.String(16))
    profile = db.Column(db.JSON)
    permissions = db.Column(db.JSON)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

