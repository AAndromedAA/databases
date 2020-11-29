from base import Base
from sqlalchemy import Column, Integer, REAL, String, ForeignKey

class Category(Base):
    __tablename__ = 'Category'

    category_id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_category_id = Column(Integer, ForeignKey('Category.category_id'))

    def __init__(self, name, parent_category_id=None):
        self.name = name
        self.parent_category_id = parent_category_id
