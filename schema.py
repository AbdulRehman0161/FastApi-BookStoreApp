from pydantic import BaseModel  # Import BaseModel to create validation schemas

# Base schema for a book. This has the common fields every book uses.
class BookBase(BaseModel):
    title: str  # Book title
    description: str  # Book summary or detail
    author: str  # Book author name
    year: int  # Book publication year


# This is used when creating a new book.
# It uses the same fields as BookBase.
class BookCreate(BookBase):
    pass


# This is used when returning a book from the database or API.
# It adds the book's id.
class Book(BookBase):
    id: int  # Unique book id

    class Config:
        orm_mode = True  # Allows conversion from SQLAlchemy objects
        from_attributes = True  # Allows reading data from object attributes