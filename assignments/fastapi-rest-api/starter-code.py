# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    published_year: int = Field(gt=0)


class Book(BookCreate):
    id: int


app = FastAPI(title="Book Library API")
books: dict[int, Book] = {}
next_book_id = 1


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Library API"}


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return all books in the collection.
    return []


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    # TODO: Create a book, assign its ID, and add it to the collection.
    raise NotImplementedError


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Return the requested book or raise HTTPException with status 404.
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate):
    # TODO: Replace an existing book or raise HTTPException with status 404.
    raise NotImplementedError


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Delete an existing book or raise HTTPException with status 404.
    # Return a JSON confirmation message after a successful deletion.
    raise NotImplementedError