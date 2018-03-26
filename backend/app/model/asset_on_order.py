from .db import db
from app.services.generate_id import generate_uuid


class AssetOnOrder(db.Model):
    """
    Stores all assets associated to an order after order completion. Types of records include
    replenishment and creation. Replenishment only works for consumable inventories, as every
    nonconsumable asset should have a tag associated to each unit.
    """
    __tablename__ = 'asset_on_order'
    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    asset_id = db.Column(db.String(40), db.ForeignKey('asset.id'))
    asset = db.relationship('Asset', backref='onorder')
    order_id = db.Column(db.String(40), db.ForeignKey('order.id'))
    order = db.relationship('Order', backref='assets')
    is_replenishment = db.Column(db.Boolean, index=True)