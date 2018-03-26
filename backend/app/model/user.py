from .db import db
from app.services.generate_id import generate_uuid, generate_user_invcode


class User(db.Model):
    """
    Stores user records
    """
    id = db.Column(db.String(40), primary_key=True, default=generate_uuid)
    role = db.Column(db.String(16))
    profile = db.Column(db.JSON)
    permissions = db.Column(db.JSON)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=True)
    inv_code = db.Column(db.String)

    def __init__(self, username=None, inv_code=None, permissions=None, profile=None, **kwargs):
        if permissions is None:
            permissions = {'role': 'admin', 'access': ['admin']}
        if profile is None:
            profile = {'name': 'Unnamed User', 'netid': 'unknown'}
        profile.update(**kwargs)
        self.inv_code = generate_user_invcode() if inv_code is None else inv_code
        self.username = username
        self.profile = profile
        self.permissions = permissions
        self.role = permissions['role']
