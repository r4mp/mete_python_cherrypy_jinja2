from models.model import Model
from db import Base
from sqlalchemy import Column, Integer, String, DateTime, func

class Audit(Base, Model):

    __tablename__ = 'audits'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    @staticmethod
    def list(session):
        return session.query(Audit).all()

