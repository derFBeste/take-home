from sqlalchemy import Column, DateTime, String, Text
import datetime
from app import db

class Message(db.Model):
    id = Column(String(36), primary_key=True)
    source_id = Column(String(36))
    message = Column(Text)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Source(db.Model):
    id = Column(String(36), primary_key=True)
    name = Column(String(255))
    environment = Column(String(255))
    encoding = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
