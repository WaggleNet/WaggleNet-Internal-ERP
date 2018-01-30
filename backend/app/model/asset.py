from .db import db
from ..utils.uuid import gen_uuid
from enum import Enum

class AssetStatus(Enum):
    pending = 0
    available = 1
    commissioned = 2
    perished = 3


class Asset(db.Model):
    """
    Stores stocking units that have an Asset tag.
    """
    id = db.Column(db.String(40), primary_key=True, default=gen_uuid)
    inventory_id = db.Column(db.String(40), db.ForeignKey('inventory.id'))
    inventory = db.relationship('Inventory', backref='assets')
    status = db.Column(db.Enum(AssetStatus), index=True, default=AssetStatus.pending)
    location_id = db.Column(db.String(40), db.ForeignKey('stocking_location.id'))
    location = db.relationship('StockingLocation', backref='assets')
    created = db.Column(db.DateTime, index=True)
    amount = db.Column(db.Integer)
