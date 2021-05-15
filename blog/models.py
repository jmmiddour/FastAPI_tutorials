# Need to import column, integer, and string from sqlalchemy
from sqlalchemy import Column, Integer, String

# Need to import Base from local database file
from .database import Base


# Create a class for the table blog
class Blog(Base):
	# Create the name of the table for this class
	__tablename__ = 'blogs'

	# Create the id column, make it the primary key and the index
	id = Column(Integer, primary_key=True, index=True)
	# Create the title column as a column of strings
	title = Column(String)
	# Create the body column as a column of strings
	body = Column(String)
