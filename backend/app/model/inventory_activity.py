from .db import db
from ..utils.uuid import gen_uuid
from enum import Enum

class InventoryActivityType(Enum):
    create = 0
    decommission = 1
    update = 2


class InventoryActivity(db.Model):
    """
    Stores activities that have occurred to assets. Possible activities include:
	- Creation of new asset tag
	- Decommission of asset tag
	- Updating metadata of the asset tag
    - Date updated
    """
    __tablename__ = 'inventory_activity'
    id = db.Column(db.String(40), primary_key=True, default=gen_uuid)
    asset_id = db.Column(db.String(40), db.ForeignKey('asset.id'))
    asset = db.relationship('Asset', backref='activities')
    inventory_id = db.Column(db.String(40), db.ForeignKey('inventory.id'))
    inventory = db.relationship('Inventory', backref='activities')
    activity_type = db.Column(db.Enum(InventoryActivityType), index=True, default=InventoryActivityType.create)
    updated = db.Column(db.DateTime, index=True)
