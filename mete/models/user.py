from models.model import Model
from db import Base
from sqlalchemy import Column, Integer, String, DateTime, func

class User(Base, Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    balance = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    def deposit(self, uid, amount):
        self.balance += amount

    def payment(self, session, amount):
        #session.query(User).filter_by(id=self.id).update({ "balance": session.query(User).filter_by(id=self.id).first.balance - amount })
        session.query(User).filter_by(id=self.id).update({ "balance": self.balance - amount })

    @staticmethod
    def list(session):
        return session.query(User).all()

