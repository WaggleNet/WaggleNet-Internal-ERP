from .db import db
from ..utils.uuid import gen_uuid

class StockLocation(db.Model):
    """
    Stores stocking locations that ties to an asset. Each created user come
    with a default stocking location tied to that user.
    """
    __tablename__ = 'stocking_location'
    id = db.Column(db.String(40), primary_key=True, default=gen_uuid)
    name = db.Column(db.String)
    is_warehouse = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.String(40), db.ForeignKey('user.id'))
    owner = db.relationship('User', backref='location')
