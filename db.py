"""Database setup for the bookstore application.

This file configures the SQLAlchemy database connection, creates the session
factory used by FastAPI, and provides helpers for creating database tables.
"""

# Import the typing helper for clearer session annotations.
from typing import Any

# Import SQLAlchemy tools needed to connect to the database and create ORM models.
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

# Load environment variables from a .env file so configuration stays out of code.
from dotenv import load_dotenv

# Import the OS module to read environment variables like the database URL.
import os

# Load variables from the .env file into the current environment.
load_dotenv()

# Read the database connection string from the environment.
# This should look like: postgres://user:password@host:port/database_name
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# Make sure the database URL actually exists before trying to connect.
# If it is missing, the app will fail early with a clear message.
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("SQLALCHEMY_DATABASE_URL is not set")

# Build the SQLAlchemy engine that manages database connections.
# This is the main object used to talk to the database.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory that produces database sessions.
# Each session is used for one unit of work, such as a request or a transaction.
SessionLocal = sessionmaker(
    autocommit=False,  # Prevent automatic commit; commit is controlled manually.
    autoflush=False,  # Prevent automatic flush before queries.
    bind=engine  # Bind the session factory to the database engine.
)

# Base class for all ORM models.
# Every database model should inherit from this class.
Base = declarative_base()


def get_db():
    """Provide a database session to a FastAPI route or dependency.

    This pattern creates a session for the request, yields it to the endpoint,
    and then closes it after the work is finished.
    """
    # Create a new database session for this request.
    db: Session = SessionLocal()

    try:
        # Yield the session so the caller can use it.
        yield db
    except Exception as e:
        print(f"Database session error: {e}")
    finally:
        # Always close the session so database connections are released.
        db.close()


def create_table():
    """Create all database tables defined by the ORM models.

    Base.metadata includes every model that inherits from Base.
    Creating all metadata binds the schema to the configured database engine.
    """
    # Create tables in the database if they do not already exist.
    Base.metadata.create_all(bind=engine)