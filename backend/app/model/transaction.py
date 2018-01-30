from .db import db
from ..utils.uuid import gen_uuid

class Transaction(db.Model):
    """
    Stores itemized account activities. Transactions can be a transfer, plain debit / credit, or in the form a procurement order.
    """
    id = db.Column(db.String(40), primary_key=True, default=gen_uuid)
    created = db.Column(db.DateTime, index=True)
    type = db.Column(db.String(16), index=True)
    amount = db.Column(db.Float)
    account_id = db.Column(db.String(40), db.ForeignKey('account.id'))
    account = db.relationship('Account', backref='transactions')
    order_id = db.Column(db.String(40), db.ForeignKey('order.id'))
    order = db.relationship('Order', backref='transactions')

