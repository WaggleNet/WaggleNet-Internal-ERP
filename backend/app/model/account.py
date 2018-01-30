from .db import db
from ..utils.uuid import gen_uuid
from enum import Enum

class AccountStatus(Enum):
    active = 1
    inactive = 0

class Account(db.Model):
    """
    Stores records for funds
    """
    id = db.Column(db.String(40), primary_key=True, default=gen_uuid)
    name = db.Column(db.String)
    remarks = db.Column(db.String)
    balance = db.Column(db.Float)
    status = db.Column(db.Enum(AccountStatus), default=AccountStatus.active)
    created = db.Column(db.DateTime, index=True)
    updated = db.Column(db.DateTime, index=True)


