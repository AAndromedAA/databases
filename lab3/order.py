from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'Order'

    order_id = Column(Integer, primary_key=True)
    date = Column(Date)
    goods_id = Column(Integer, ForeignKey('Goods.goods_id'))
    goods = relationship('Goods', backref='Order')
    customer_id = Column(Integer, ForeignKey('Customer.customer_id'))
    customer = relationship('Customer', backref='Order')
    confirming_method = Column(String)

    def __init__(self, date, goods_id, customer_id, confirming_method, goods, customer):
        self.date = date
        self.goods_id = goods_id
        self.customer_id = customer_id
        self.confirming_method = confirming_method
        self.goods = goods
        self.customer = customer
