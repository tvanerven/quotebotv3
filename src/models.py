from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class QuoteTable(Base):
    __tablename__ = 'quote_quote'
    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String, index=True)
    author = Column(Integer, ForeignKey("quote_author.id"))
    added_date = Column(DateTime)
    hit_count = Column(Integer)
    translation = Column(String, default='')

    relationship("AuthorsTable", back_populates="authors")

class AuthorsTable(Base):
    __tablename__ = 'quote_author'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
