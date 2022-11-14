import datetime
from typing import Optional

from pydantic import BaseModel


class Author(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class Quote(BaseModel):
    id: int
    quote: str
    author: Author
    added_date: datetime.datetime = datetime.datetime.now()
    hit_count: int
    translation: Optional[str]

    class Config:
        orm_mode = True
