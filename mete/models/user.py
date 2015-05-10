from models.model import Model
from db import Base
from sqlalchemy import Column, Integer, String, DateTime, func, orm

class User(Base, Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    balance = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    @orm.reconstructor
    def init_on_load(self):
        self.balance_eur = self.round_decimal(self.balance/100)

    @staticmethod
    def deposit(session, uid, amount):
        session.query(User).filter_by(id=int(uid)).update({ "balance": session.query(User).filter_by(id=int(uid)).first().balance + int(amount) })
        
    @staticmethod
    def payment(session, uid, amount):
        session.query(User).filter_by(id=int(uid)).update({ "balance": session.query(User).filter_by(id=int(uid)).first().balance - int(amount) })

    @staticmethod
    def get(session, uid):
        return session.query(User).filter_by(id=int(uid)).first()

    @staticmethod
    def delete(session, uid):
        session.query(User).filter_by(id=int(uid)).delete()

    @staticmethod
    def count(session):
        return session.query(User).count()

    @staticmethod
    def balance_sum(session):
        return User.round_decimal(session.query(func.sum(User.balance)).scalar()/100)

    @staticmethod
    def list(session):
        return session.query(User).all()

