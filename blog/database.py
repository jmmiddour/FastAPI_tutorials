# Import create_engine
from sqlalchemy import create_engine

# Import declarative_base from SQLAlchemy to declare the mapping for the db
from sqlalchemy.ext.declarative import declarative_base

# Import sessionmaker to create a local session
from sqlalchemy.orm import sessionmaker


# Create a global variable for the database url
SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# Create the database engine
# `connect_args=` is a FastAPI requirement
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={'check_same_thread': False})

# Create the local session global variable
LocalSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Declare a mapping to the database global varaible
Base = declarative_base()
