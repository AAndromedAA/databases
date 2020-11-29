from base import Base
from sqlalchemy import Column, Integer, REAL, String, ForeignKey
from sqlalchemy.orm import relationship


class Goods(Base):
    __tablename__ = 'Goods'

    goods_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    price = Column(REAL)
    discount = Column(REAL)
    guarantee = Column(Integer)
    category_id = Column(Integer, ForeignKey('Category.category_id'))
    category = relationship('Category', backref="Goods")

    def __init__(self, name, price, discount, guarantee, category_id, category):
        self.name = name
        self.price = price
        self.discount = discount
        self.guarantee = guarantee
        self.category_id = category_id
        self.category = category
