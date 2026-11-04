"""Define the database model for books."""

from db import Base  # Reuse the shared SQLAlchemy model base.
from Sqlalchemy import Column, Integer, String  # Import ORM column tools.

class Book(Base):  # Define the book database model.
    """Map book records to the books table."""

    __tablename__ = 'books'  # Map this model to the books table.

    id: Column[int] = Column(Integer, primary_key=True, index=True)  # Unique indexed identifier.
    title: Column[str] = Column(String, index=True)  # Indexed book title.
    author: Column[str] = Column(String, index=True)  # Indexed author name.
    description: Column[str] = Column(String, index=True)  # Indexed book description.
    year: Column[int] = Column(Integer, index=True)  # Indexed publication year.