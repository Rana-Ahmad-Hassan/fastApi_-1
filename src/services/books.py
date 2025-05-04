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

    async def create_book(self, book_data: BookData, session: AsyncSession) -> Book:
        book_data_dict = book_data.model_dump()
        new_book = Book(**book_data_dict)
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book

    async def update_book(self, book_id: str, book_data: BookData, session: AsyncSession) -> Book | None:
        book = await self.get_book_by_id(session, book_id)
        if not book:
            return None

        for field, value in book_data.model_dump(exclude_unset=True).items():
            setattr(book, field, value)

        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book

    async def delete_book(self, book_id: str, session: AsyncSession) -> bool:
        book = await self.get_book_by_id(session, book_id)
        if not book:
            return False
        await session.delete(book)
        await session.commit()
        return True
