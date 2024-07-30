from config import db
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Contact(db.Model):
    __tablename__ = 'modals'
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(50))
    last_name = db.Column(String(50))
    email = db.Column(String(50), unique=True)
    created_at = db.Column(DateTime, default=datetime.utcnow)

    def to_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'created_at': self.created_at
        }
        # return {'id': self.id, 'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email, 'created_at': self.created_at}

    
    