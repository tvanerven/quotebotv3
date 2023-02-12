from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base

class QuoteTable(Base):
    __tablename__ = 'quote_quote'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    context = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("quote_author.id"))
    created = Column(DateTime)
    hit_count = Column(Integer)
    last_hit = Column(DateTime)
    text_english = Column(String, default='')
    context_english = Column(String, default='')

    relationship("AuthorsTable", back_populates="quotes")

class AuthorsTable(Base):
    __tablename__ = 'quote_author'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
