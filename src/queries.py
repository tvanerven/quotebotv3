from sqlalchemy.orm import Session
import random

from pydantic_models import *
import pydantic_models
from models import (
    AuthorsTable,
    QuoteTable
)

def get_quotes(db: Session, query: str):
    return db.query(QuoteTable).filter(QuoteTable.quote.in_(query))

def get_users(db: Session):
    return AuthorsTable.name.all()

def get_random_quote(db: Session):
    return random.choice(db.query(QuoteTable).all())

def add_quote(db: Session, quote: Quote, author: str):
    quote_author = db.query(AuthorsTable).filter(AuthorsTable.name == author.lower())
    quote = QuoteTable(**quote.dict(), author_id = quote_author.id)
    db.add(quote)
    db.commit()
    db.refresh(quote)
    return quote
