from base import Base
from sqlalchemy import Column, Integer, String, VARCHAR, ARRAY
class Customer(Base):
    __tablename__ = 'Customer'

    customer_id = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    father_name = Column(String)
    favourites = Column(ARRAY(VARCHAR(100)))

    def __init__(self, surname, name, father_name, favourites):
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.favourites = favourites
