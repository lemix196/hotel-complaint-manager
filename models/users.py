from .models import db
import os
import hashlib
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(30))
    group = db.Column(db.String(15), default='GUEST')
    date_create = db.Column(db.DateTime, default=datetime.today())


    def hash_password(self, password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            110996
        )
        return salt + key

    def verify_password(self, stored_password, provided_password):
        salt = stored_password[:32]
        provided_password = salt + hashlib.pbkdf2_hmac(
            'sha256',
            provided_password.encode('utf-8'),
            salt,
            110996
        )
        return provided_password == stored_password

