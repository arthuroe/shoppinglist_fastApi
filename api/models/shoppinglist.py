from sqlalchemy import Column, Integer, String, ForeignKey

from db.db_setup import Base

class ShoppingList(Base):
    """
    Create a shopping table
    """

    __tablename__ = 'shoppinglists'

    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
