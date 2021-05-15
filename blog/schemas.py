"""
This file contains all of the "Pydandic" models/schemas.

This is often referred to as the "response model", whereas our `models.py`
	file is the "database model"

You use a Pydantic model to create the way the response body is returned,
	i.e. what the user will see from the database in the response body.
"""

# Import BaseModel from pydantic for the class
from pydantic import BaseModel


# Create a class for the blog
# This is considered the "Pydantic Model" or "Schema"
# Moved the class and BaseModel module to the schemas.py file
class Blog(BaseModel):
	# Define the data types of the fields returned to the user
	title: str
	body: str


# Create another schema to show the blog data to the user, and inherit from
#   the Blog class above because we only want to show the title and the body,
#   not the id to the user.
# class ShowBlog(Blog):
# 	# Create a new class for configuration
# 	class Config():
# 		# Need to set the orm_mode to True or it will raise an error
# 		orm_mode = True


# Another way to do it if you want the user to see only the title
class ShowBlog(BaseModel):
	# Define only what you want the user to see
	title: str

	# Create a new class for configuration
	class Config():
		# Need to set the orm_mode to True or it will raise an error
		orm_mode = True


# Create another class for the User schema
class User(BaseModel):
	# Define the data types of the fields to return to the user
	name: str
	email: str
	password: str


# Create another class for the User schema to return only name and email
class ShowUser(BaseModel):
	# Define the data types of the fields to return to the user
	name: str
	email: str
