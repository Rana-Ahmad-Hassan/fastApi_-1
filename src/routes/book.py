from fastapi import APIRouter, status, Depends
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config.db import get_session
from src.schemas.book_schema import BookData
from src.services.books import BooksServices

book_router = APIRouter()
book_service = BooksServices()

@book_router.get("/books", status_code=status.HTTP_200_OK)
async def get_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

@book_router.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookData, session: AsyncSession = Depends(get_session)):
    new_book = await book_service.create_book(book_data, session)
    return new_book

@book_router.put("/update-book/{book_id}", status_code=status.HTTP_200_OK)
async def update_book(book_id: str, updated_data: BookData, session: AsyncSession = Depends(get_session)):
    updated_book = await book_service.update_book(book_id, updated_data, session)
    return updated_book  # Only this line should remain

@book_router.delete("/delete-book/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: str, session: AsyncSession = Depends(get_session)):
    deleted_book = await book_service.delete_book(book_id, session)
    return deleted_book  # Remove unreachable second return
