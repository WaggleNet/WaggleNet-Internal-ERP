from .db import db
from ..utils.uuid import gen_uuid
from enum import Enum


class OrderStatus(Enum):
    pending = 0
    in_progress = 1
    completed = 2


class Order(db.Model):
    """
    Stores pending, in-progress and completed procurement orders. When order is processed,
    a transaction corresponding to the order should be automatically created. When order is
    fulfilled, corresponding asset records are created.

    Shopping List Schema:
    	○ Order Source
		○ Status
		○ (F) Inventory ID (if replenishes)
		○ Stocking Qty
		○ MOQ
		○ Order qty
		○ Non-inventory orders (service fees, shipping)
    """
    id = db.Column(db.String(40), primary_key=True, default=gen_uuid)
    status = db.Column(db.Enum(OrderStatus), index=True, default=OrderStatus.pending)
    created = db.Column(db.DateTime, index=True)
    updated = db.Column(db.DateTime, index=True)
    milestones = db.Column(db.JSON)
    user_id = db.Column(db.String(40), db.ForeignKey('user.id'))
    user = db.relationship('User')
    shopping_list = db.Column(db.JSON)
