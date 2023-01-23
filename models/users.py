from .models import db
import os
import hashlib
from datetime import datetime


class User:
    def __init__(self, user_name, password, group='guest'):
        self.user_name = user_name
        self.password = password
        self.group = group
        self.date_create = datetime.today()

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

