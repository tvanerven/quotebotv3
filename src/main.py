from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from queries import (
    get_quotes,
    get_users
)

models.Base.metadata.create_all(bind=engine)

from . import models, pydantic_models
from .database import SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

from database import SessionLocal

@app.get("/quote")
def get_quote(search_term: str, db: Session = Depends(get_db)):
    return get_quotes(db=db, query=search_term)

@app.get("/users")
def get_authors_list():
    return get_users
