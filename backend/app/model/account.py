from .db import db
from ..services.generate_id import generate_uuid
from enum import Enum
from sqlalchemy import func

class AccountStatus(Enum):
    active = 1
    inactive = 0

class Account(db.Model):
    """
    Stores records for funds
    """
    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    name = db.Column(db.String)
    remarks = db.Column(db.String)
    balance = db.Column(db.Float)
    status = db.Column(db.Enum(AccountStatus), default=AccountStatus.active)
    created = db.Column(db.DateTime(timezone=True), index=True, server_default=func.now())
    updated = db.Column(db.DateTime(timezone=True), index=True, onupdate=func.now())

    def __init__(self, name, remarks=''):
        self.balance = 0
        self.name = name
        self.remarks = remarks
