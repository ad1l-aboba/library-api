from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="API для библиотеки книг")


# Модель данных (с проверкой корректности)
class BookIn(BaseModel):
    title: str = Field(..., min_length=1, description="Название книги")
    author: str = Field(..., min_length=1, description="Автор")
    year: int = Field(..., ge=0, le=2100, description="Год издания")


class Book(BookIn):
    id: int


# Хранилище в памяти
books: list[Book] = []
next_id = 1


def find_book(book_id: int) -> Book:
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


@app.get("/books", response_model=list[Book])
def get_books():
    """Возвращает список всех книг"""
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    """Возвращает информацию о книге по ID"""
    return find_book(book_id)


@app.post("/books", response_model=Book, status_code=201)
def add_book(data: BookIn):
    """Добавляет новую книгу (id назначается автоматически)"""
    global next_id
    book = Book(id=next_id, **data.model_dump())
    next_id += 1
    books.append(book)
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, data: BookIn):
    """Обновляет данные существующей книги"""
    book = find_book(book_id)
    book.title = data.title
    book.author = data.author
    book.year = data.year
    return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    """Удаляет книгу"""
    book = find_book(book_id)
    books.remove(book)
    return {"message": f"Книга {book_id} удалена"}
