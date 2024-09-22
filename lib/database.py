from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for the SQLite database
db_URL = "sqlite:///tasks.db" 

# Create the SQLAlchemy engine for the database
engine = create_engine(db_URL)

# Create a declarative base class for our models
Base = declarative_base()
# Create a session factory for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def tables():
    """Create all tables in the database based on the defined models."""
    Base.metadata.create_all(bind=engine)