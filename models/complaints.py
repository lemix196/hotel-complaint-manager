from .models import db

class Complaint(db.Model):
    """Model for complaint table in DB"""
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(50))
    room_number = db.Column(db.Integer)
    message = db.Column(db.String(500))
    urgency = db.Column(db.String(15))
    add_date = db.Column(db.DateTime)