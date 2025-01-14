# database.py
"""
Database configuration module for the Car Sales API.
Sets up SQLite database connection using SQLAlchemy and provides session management.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL (using file-based database for persistence)
SQLALCHEMY_DATABASE_URL = "sqlite:///./car_sales.db"

# Create SQLAlchemy engine with SQLite-specific configuration
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for declarative models
Base = declarative_base()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
