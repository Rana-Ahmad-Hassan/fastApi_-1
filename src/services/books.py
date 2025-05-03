from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from src.models.books import Book
from src.schemas.book_schema import BookData


class BooksServices:
    async def get_all_books(self, session: AsyncSession):
        query = select(Book).order_by(desc(Book.created_at))
        result = await session.exec(query)
        return result.all()


    async def get_book_by_id(self, session: AsyncSession, book_id: str):
       query = select(Book).where(Book.id == book_id)
       result = await session.exec(query)
       return result.first()


    async def create_book(self, book_data: BookData, session: AsyncSession):
       book_data_dict = book_data.model_dump()
       new_book = Book(**book_data_dict)
       session.add(new_book)
       await session.commit()
       return new_book






