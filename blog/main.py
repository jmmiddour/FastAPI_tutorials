# Import FastApi
from fastapi import FastAPI

# Import the classes from the schemas file
from . import schemas

# Import BaseModel from pydantic for the class
# from pydantic import BaseModel


# Instantiate FastAPI
app = FastAPI()


# # Create a class for the blog
# # Moved the class and BaseModel module to the schemas.py file
# class Blog(BaseModel):
# 	title: str
# 	body: str


# # Create a post request method
# @app.post('/blog')
# # Create a function to create a new blog post, taking in the title and body
# #   of the blog
# # Doing it this way will give you request fields (boxes) on the SwaggerUI
# def create(title, body):
# 	# Return to the user, the title and body of their blog post.
# 	return {'title': title, 'body': body}


# Create a post request method
@app.post('/blog')
# Create a function to create a new blog post, taking in the title and body
#   of the blog using pydantic
# Doing it this way will give you a request body
def create(request: schemas.Blog):
	# Return to the user, the title and body of their blog post.
	return request
