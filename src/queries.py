from sqlalchemy.orm import Session
import random

from . import pydantic, models

def get_quotes(db: Session, query: str):
    return db.query(models.QuoteTable).filter(models.QuoteTable.quote.in_(query))

def get_users(db: Session):
    return models.AuthorsTable.name.all()

def get_random_quote(db: Session):
    return random.choice(db.query(models.QuoteTable).all())

def add_quote(db: Session, quote: pydantic.Quote, author: str):
    quote_author = db.query(models.AuthorsTable).filter(models.AuthorsTable.name == author.lower())
    quote = models.QuoteTable(**quote.dict(), author_id = quote_author.id)
    db.add(quote)
    db.commit()
    db.refresh(quote)
    return quote
