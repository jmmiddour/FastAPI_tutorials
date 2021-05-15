"""
This file contains all of the routes/paths for the API.
"""

# Import the List type from typing
from typing import List

# Import FastApi
from fastapi import FastAPI, Depends, status, Response, HTTPException

# Import the classes from the schemas and models files
from . import schemas, models

# Import the engine and local session from the database file
from .database import engine, LocalSession

# Import Session from SQLAlchemy
from sqlalchemy.orm import Session

# Instantiate FastAPI
app = FastAPI()

# Create the database
models.Base.metadata.create_all(engine)


# # Create a post request method
# @app.post('/blog')
# # Create a function to create a new blog post, taking in the title and body
# #   of the blog
# # Doing it this way will give you request fields (boxes) on the SwaggerUI
# def create(title, body):
# 	# Return to the user, the title and body of their blog post.
# 	return {'title': title, 'body': body}


# Create a function to get the get the database connection to create a
#   current session
def get_db():
	# Create a variable to hold the local session in
	db = LocalSession()

	# Try this first...
	try:
		# A "generator" function to keep the database connection alive
		yield db

	# Lastly, do this...
	finally:
		# Close the database connection when finished
		db.close()


# Create a post request method
# If you add the parameter status_code=201, it will return status code 201 if
#   a valid request is returned.
# If you do not know the correct status code, you can use the status method
#   from fastapi that has a list of all the status codes and their meanings,
#   like below.
@app.post('/blog', status_code=status.HTTP_201_CREATED)
# Create a function to create a new blog post, taking in the title and body
#   of the blog using pydantic.
# Doing it this way will give you a request body
# Doing the `db: Session = Depends(get_db)` makes the default value for the
#   db parameter dependent upon the `get_db` function defined above.
def create(request: schemas.Blog, db: Session = Depends(get_db)):
	# # Return to the user, the title and body of their blog post.
	# return request
	# Create the new blog
	new_blog = models.Blog(title=request.title, body=request.body)
	# Add the new blog to the database
	db.add(new_blog)
	# Commit the changes to the database
	db.commit()
	# Refresh the database with the new blog added to it
	db.refresh(new_blog)
	# Return to the user, the newly created blog
	return new_blog


# Create a new path request method to remove a blog
@app.delete('/blog/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
# Create the method to remove it from the database
def destroy(blog_id, db: Session = Depends(get_db)):
	# Use the query function to locate the blog
	blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

	# Check edge case of invalid blog id entered
	if not blog.first():
		# Return not found status code and message to the user
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f'Blog with the id {blog_id} is not available. Please try '
			       f'another blog id number.')

	# Now we know the blog exists, we can use the delete function to remove it
	blog.delete(synchronize_session=False)
	# Commit the changes to the database
	db.commit()
	# Don't need to return anything, just closing the function
	# return {'detail': f"Blog {blog_id} has been successfully deleted!"}
	return None


# Create a new path to update a blog based on its id
@app.put('/blog/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
# Create the method to update the blog
# The request: schemas.Blog is just getting the schema of the blog table to
#   create the proper output format on the api.
def update(blog_id, request: schemas.Blog, db: Session = Depends(get_db)):
	# Use the query function to locate the blog
	blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

	# Check edge case of invalid blog id entered
	if not blog.first():
		# Return not found status code and message to the user
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f'Blog with the id {blog_id} is not available. Please try '
			       f'another blog id number.')

	# Now use the update function to update the blog if it exists
	# Can use `vars()` or `dict()` to fix error here
	blog.update(dict(request))
	# Commit the changes to the database
	db.commit()
	# Return a message letting the user know it was successful
	return f'Blog {blog_id} has been successfully updated!'


# Add a new route/path request method to get all the blogs from the database
@app.get('/blog', response_model=List[schemas.ShowBlog])
# Define the method to get all the blogs
def get_blogs(db: Session = Depends(get_db)):
	# Query the database to get all the blogs
	blogs = db.query(models.Blog).all()
	# Return all the blogs to the user
	return blogs


# Add a new route/path request to get a single blog by its id
@app.get('/blog/{blog_id}', status_code=200, response_model=schemas.ShowBlog)
# Define the method to get the 1st blog by the id
def show_blog(blog_id, response: Response, db: Session = Depends(get_db)):
	# Query the database to get the 1st instance of the blog at specified id
	# Using .filter() is like using the WHERE condition in SQL
	# Using .first() returns only the 1st occurrence
	blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()

	# Check for the edge case of the user entering an invalid id number
	if not blog:
		# # Return a NOT FOUND response code to the user
		# # This will override the default status code only if the
		# #   above if statement is True
		# response.status_code = status.HTTP_404_NOT_FOUND
		# # Return a custom message in the response body to the user
		# return {
		# 	'detail':
		# 		f'Blog with the id {blog_id} is not available. Please '
		# 		f'try another blog id number.'
		# }
		# Could also do the same thing with one line of code using the
		#   fastapi's HTTPException method.
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f'Blog with the id {blog_id} is not available. Please try '
			       f'another blog id number.')

	# Return the blog to the user
	return blog


@app.post('/user')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
	# Create the new user
	new_user = models.User(name=request.name, email=request.email,
	                       password=request.password)
	# Add the new user to the database
	db.add(new_user)
	# Commit the changes to the database
	db.commit()
	# Refresh the database to reflect the changes
	db.refresh(new_user)
	# Return the new user just entered to the user
	return new_user
