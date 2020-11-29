from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Phone(Base):
    __tablename__ = 'Phone'

    phone = Column(String, primary_key=True)
    customer_id = Column(Integer, ForeignKey('Customer.customer_id'))
    customer = relationship('Customer', backref='Phone')

    def __init__(self, phone, customer_id, customer):
        self.phone = phone
        self.customer_id = customer_id
        self.customer = customer
