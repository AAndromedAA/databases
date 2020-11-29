from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Email(Base):
    __tablename__ = 'Email'

    email = Column(String, primary_key=True)
    customer_id = Column(Integer, ForeignKey('Customer.customer_id'))
    customer = relationship('Customer', backref='Email')

    def __init__(self, email, customer_id, customer):
        self.email = email
        self.customer_id = customer_id
        self.customer = customer
