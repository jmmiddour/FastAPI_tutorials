# Import FastAPI from the fastapi library
from fastapi import FastAPI

# Initialize the FastAPI app
# This variable to be named whatever you want, just make sure that when you
#   start the uvicorn server, this variable name needs to go after
#   <file name>:<this variable>
# Also this variable is always after the @ decorator and before the
#   .<request method> when creating a path in the app.
app = FastAPI()


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
