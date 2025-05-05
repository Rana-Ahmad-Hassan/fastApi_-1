from pydantic import BaseModel
from datetime import date

class BookData(BaseModel):
    title: str
    author: str
    publisher: str
    publish_date: date
    page_count: int
