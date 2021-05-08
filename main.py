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
	return {'data': {'name': 'Joanne'}}


@app.get('/about')
def about():
	return {'data': 'about page'}
