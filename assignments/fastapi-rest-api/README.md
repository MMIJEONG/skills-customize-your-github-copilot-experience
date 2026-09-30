# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for managing books with FastAPI. Practice defining HTTP endpoints, validating request data, and using appropriate status codes for create, read, update, and delete operations.

## 📝 Tasks

### 🛠️ Run the API and List Books

#### Description
Install the project dependencies and start the FastAPI development server. Complete the book-list endpoint so it returns all books currently stored in the in-memory collection.

Run the API with:

```bash
pip install -r requirements.txt
uvicorn starter-code:app --reload
```

Open `http://127.0.0.1:8000/docs` to explore and try the endpoints.

#### Requirements
Completed program should:

- Start with Uvicorn and expose the interactive API documentation at `/docs`
- Return a JSON welcome message from `GET /`
- Return the current collection as a JSON array from `GET /books`


### 🛠️ Create and Read Books

#### Description
Implement endpoints to add a book and retrieve one book by its ID. Use the provided Pydantic models to validate incoming book details.

#### Requirements
Completed program should:

- Accept a book title, author, and positive publication year in `POST /books`
- Assign each new book a unique ID and return the created book with status code `201`
- Return a book by ID from `GET /books/{book_id}`
- Return status code `404` when the requested book does not exist


### 🛠️ Update and Delete Books

#### Description
Complete the remaining endpoints so a client can replace an existing book and remove a book from the collection. Try each operation in `/docs` and check what happens when you use an unknown ID.

#### Requirements
Completed program should:

- Replace a book's title, author, and publication year with `PUT /books/{book_id}`
- Remove a book with `DELETE /books/{book_id}` and return a confirmation message
- Return status code `404` when trying to update or delete a book that does not exist
- Keep data in memory and note that it resets when the server restarts