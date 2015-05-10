from models.model import Model
from db import Base
from sqlalchemy import Column, Integer, String, DateTime, func, orm

class Drink(Base, Model):

    __tablename__ = 'drinks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    bottle_size = Column(Integer)
    caffeine = Column(Integer)
    logo_url = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    @orm.reconstructor
    def init_on_load(self):
        self.price_eur = self.round_decimal(self.price/100)

    @staticmethod
    def list(session):
        return session.query(Drink).all()

