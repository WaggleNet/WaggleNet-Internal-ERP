from .db import db
from app.services.generate_id import generate_uuid
from sqlalchemy import func
from enum import Enum

class TransactionType(Enum):
    none = 0
    purchase = 1
    fee = 2
    refund = 3
    reconciliation = 4
    transfer = 5
    misc = 20


class Transaction(db.Model):
    """
    Stores itemized account activities. Transactions can be a transfer, plain debit / credit, or in the form a procurement order.
    """
    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    created = db.Column(db.DateTime(timezone=True), index=True, server_default=func.now())
    type = db.Column(db.Enum(TransactionType), index=True, default=TransactionType.none)
    payee = db.Column(db.String(40), index=True)
    amount = db.Column(db.Float)
    account_id = db.Column(db.String(40), db.ForeignKey('account.id'))
    order_id = db.Column(db.String(40), db.ForeignKey('order.id'))
    description = db.Column(db.String(120))
    agent_id = db.Column(db.String(40), db.ForeignKey('user.id'))

    account = db.relationship('Account', backref='transactions')
    order = db.relationship('Order', backref='transactions')
    agent = db.relationship('User', backref='transactions')

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
