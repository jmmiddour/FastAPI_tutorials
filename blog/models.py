"""
This file contains the SQLAlchemy database model/schema.
"""

# Need to import column, integer, and string from sqlalchemy
from sqlalchemy import Column, Integer, String

# Need to import Base from local database file
from .database import Base


# Create a class for the table blog, inherit from Base
class Blog(Base):
	# Create the name of the table for this class
	__tablename__ = 'blogs'

	# Create the id column, make it the primary key and the index
	id = Column(Integer, primary_key=True, index=True)
	# Create the title column as a column of strings
	title = Column(String)
	# Create the body column as a column of strings
	body = Column(String)


# Create a new class for the table user, inherit from Base
class User(Base):
	# Define the table's name
	__tablename__ = 'users'

	# Create the id column, make it the primary key and the index
	id = Column(Integer, primary_key=True, index=True)
	# Create the name column as a column of strings
	name = Column(String)
	# Create the email column as a column of strings
	email = Column(String)
	# Create the password column as a column of strings
	password = Column(String)
