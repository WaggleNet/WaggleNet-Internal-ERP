from .db import db
from ..utils.uuid import gen_uuid

class Inventory(db.Model):
    """
    Stores inventory items in a list.
    """
    id = db.Column(db.String(40), primary_key=True, default=gen_uuid)
    stocking_level = db.Column(db.Integer, default=0)
    availability_level = db.Column(db.Integer, default=0)
    consumable = db.Column(db.Boolean, nullable=False, default=False, index=True)
    created = db.Column(db.DateTime, index=True)
    updated = db.Column(db.DateTime, index=True)
    name = db.Column(db.String)
