from app import db
from datetime import datetime

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.Numeric(10), nullable=False, unique=True)
    address = db.Column(db.String(50), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"<Contact {self.id}|{self.last_name}, {self.first_name}>"