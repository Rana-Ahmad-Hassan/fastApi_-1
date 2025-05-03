from pydantic import BaseModel

class BookData(BaseModel):
    title: str
    author: str
    publisher: str
    publish_date: str
    page_count: int
