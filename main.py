# Import FastAPI from the fastapi library
from fastapi import FastAPI

# Import Optional to use with parameters to make it an optional parameter
from typing import Optional

# Import the BaseModel from pydantic to create a request body
from pydantic import BaseModel

# Import uvicorn to run the server when main is ran
import uvicorn

# Initialize the FastAPI app
# This variable to be named whatever you want, just make sure that when you
#   start the uvicorn server, this variable name needs to go after
#   <file name>:<this variable>
# Also this variable is always after the @ decorator and before the
#   .<request method> when creating a path in the app.
app = FastAPI()

"""
# Creates a "get route" for the app, in FastAPI it is called the "path"
# The @ is called the "path operation decorator" in FastAPI
# The available request methods are: get(), post(), put(), delete()
#   ^-- called "operation" in FastAPI
@app.get('/')
# Use a function to create the return for the route
# Called the "path operation function" in FastAPI
def index():
	# Can simply return a string
	# return 'Hello'

	# Or you can return it in JSON (dictionary) format like this:
	# return {'data': {'name': 'Joanne'}}

	# Going to return a "blog list"
	return {'data': 'blog list'}
"""


# Static way of using a query
# @app.get('/blog?limit=10')
# Another route using multiple queries at once
# @app.get('/blog?limit=10&published="true"')
# def index():
# 	# Will only show the first 10 published blogs.
# 	return {'data': 'blog list'}


# Dynamic way of using a query
@app.get('/')
# def index(limit, published: bool):
# 	# Doing it this way will require that the user types into the url:
# 	#   `.../blogs?limit=<number>&published=<true or false only>`
# 	# If the user does not add both as stated above, they will get an error
# 	#   message stating that the field is required.
def index(limit=10, published: bool = True, sort: Optional[str] = None):
	# Doing it this way, if the user does not type in anything in the url, and
	#   just types `.../blog` it will default to showing 10 published blogs
	# When adding parameters with defaults, if you want to add a parameter
	#   that the user can use but is not required, you need to use the
	#   Optional method from the typing library. Like we did with the `sort`
	#   parameter in the above code. With the Optional method you still need
	#   to define the data type but in [] as above and still need to assign it
	#   a default value, even None will work.
	if published:
		return {'data': f'{limit} published blogs from the database.'}
	else:
		return {'data': f'{limit} blogs from the database.'}


# @app.get('/about')
# def about():
# 	return {'data': 'about page'}


# To get a list of all the unpublished blogs via a "static" route (path)
# Have to make sure that this is before the one that takes in an id or will
#   get the type mismatch error because it is reading the code line by line,
#   so it would read the unpublished as the id if after that path in code.
@app.get('/blog/unpublished')
def unpublished():
	return {'data': 'all unpublished blogs'}


# To get a blog by the id, dynamically, need the {} around the variable
# By default, will get a string if pulling from the URL
#   i.e. .../blog/100 --> returns '100' as the blog_id
@app.get('/blog/{blog_id}')
def show(blog_id: int):  # blog_id: int --> defines the type for the param
	"""
	By defining the type of the parameter as an integer, if the user
		tries to type in a non-integer value in the URL, they will get an
		error message that is already built-in to FastAPI:
	{
		"detail": [
			{
				"loc": [
					"path",
					"blog_id"
				],
				"msg": "value is not a valid integer",
				"type": "type_error.integer"
			}
		]
	}
	"""
	# Can fetch the blog with the id = to the id inputted in the path
	return {'data': blog_id}


# To get the blog comments by the id number of the blog
#   This route (path) is both dynamic and static
@app.get('blog/{blog_id}/comments')
def comments(blog_id):
	# Fetch comments of blog where id = id
	return {'data': {'1', '2'}}


# Create a class for creating a new blog post
class Blog(BaseModel):
	title: str
	body: str
	published: Optional[bool]


# Create a route (path) to create a new blog post
@app.post('/blog')
def create_blog(blog: Blog):
	return {'data': f'Blog is created with title as {blog.title}'}


# # For debugging purposes
# if __name__ == '__main__':
# 	uvicorn.run(app, host='127.0.0.1', port=9000)