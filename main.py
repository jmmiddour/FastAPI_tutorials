# Import FastAPI from the fastapi library
from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()


# Creates a "get" route for the app
@app.get('/')
# Use a function to create the return for the route
def index():
	# Can simply return a string
	# return 'Hello'
	# Or you can return it in JSON (dictionary) format like this:
	return {'data': {'name': 'Joanne'}}


@app.get('/about')
def about():
	return {'data': 'about page'}
