from fastapi import APIRouter, status
from src.books.book_data import books
from src.schemas.book_schema import Book


book_router = APIRouter()


@book_router.get("/books", status_code=status.HTTP_200_OK)
async def get_books():
    return books

@book_router.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_data: Book):
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@book_router.put("/update-book/{book_title}", status_code=status.HTTP_200_OK)
async def update_book(book_title: str, updated_data: Book):
    for book in books:
        if book["title"] == book_title:
            book.update(updated_data.model_dump())
            return book
    return {"error": "Book not found"}


@book_router.delete("/delete-book/{book_title}", status_code=status.HTTP_200_OK)
async def delete_book(book_title:str):
    for book in books:
        if book["title"] == book_title:
            books.remove(book)
            return book
    return {"error": "Book not found"}