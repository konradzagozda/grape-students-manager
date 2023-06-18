from uuid import uuid4
from database import db

class Student(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)