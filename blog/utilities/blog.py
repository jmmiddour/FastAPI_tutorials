"""
This file contains all the functions for the blog routes/paths
"""

# Imports
from fastapi import status, HTTPException
from .. import schemas, models


def get_all(db):
	"""
	Function to get all the blogs from the database.

	:param db: connection to database
	:return: JSON: file with all blog entries from the database
	"""
	# Query the database to get all the blogs
	blogs = db.query(models.Blog).all()
	# Return all the blogs to the user
	return blogs


def create(request: schemas.Blog, db):
	"""
	Function to create a new blog record in the database.

	:param request: input from the user through the API
	:param db: connection to the database
	:return: JSON: file with the newly create blog data
	"""
	# Create the new blog
	new_blog = models.Blog(
		title=request.title, body=request.body, user_id=request.user_id
	)
	# Add the new blog to the database
	db.add(new_blog)
	# Commit the changes to the database
	db.commit()
	# Refresh the database with the new blog added to it
	db.refresh(new_blog)
	# Return to the user, the newly created blog
	return new_blog


def destroy(blog_id, db):
	"""
	Function to remove a blog record from the database.

	:param blog_id: int: the blog id number to be removed
	:param db: connection to the database
	:return: status code: 204 if blog was successfully removed
	"""
	# Use the query function to locate the blog
	blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

	# Check edge case of invalid blog id entered
	if not blog.first():
		# Return not found status code and message to the user
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f'Blog with the id {blog_id} is not available. Please '
			       f'try '
			       f'another blog id number.'
		)

	# Now we know the blog exists, we can use the delete function to
	# remove it
	blog.delete(synchronize_session=False)
	# Commit the changes to the database
	db.commit()
	# Don't need to return anything, just closing the function
	# return {'detail': f"Blog {blog_id} has been successfully deleted!"}
	return f'Blog with id #{blog_id} has been successfully deleted.'


# Create the method to update the blog
# The request: schemas.Blog is just getting the schema of the blog table to
#   create the proper output format on the api.
def update(blog_id, request, db):
	"""
	Function to update a blog record based on the blog id specified.

	:param blog_id: int: the id number of the blog to be updated
	:param request: input from the user through the API
	:param db: connection to the database
	:return: JSON: file with updated blog record
	"""
	# Use the query function to locate the blog
	blog = db.query(models.Blog).filter(models.Blog.id == blog_id)

	# Check edge case of invalid blog id entered
	if not blog.first():
		# Return not found status code and message to the user
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f'Blog with the id {blog_id} is not available. Please try '
			       f'another blog id number.'
		)

	# Now use the update function to update the blog if it exists
	# Can use `vars()` or `dict()` to fix error here
	blog.update(dict(request))
	# Commit the changes to the database
	db.commit()
	# Return a message letting the user know it was successful
	return f'Blog {blog_id} has been successfully updated!'


def show_blog(blog_id, db):
	"""
	Function to show a single blog record, based on the blog id specified.

	:param blog_id: int: the id number of the blog to be returned
	:param db: connection to the database
	:return: JSON: file with the single blog record specified
	"""
	# Query the database to get the 1st instance of the blog at specified id
	# Using .filter() is like using the WHERE condition in SQL
	# Using .first() returns only the 1st occurrence
	blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()

	# Check for the edge case of the user entering an invalid id number
	if not blog:
		# Return a NOT FOUND response code to the user
		# This will override the default status code only if the
		#   above if statement is True
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f'Blog with the id {blog_id} is not available. Please try '
			       f'another blog id number.'
		)

	# Return the blog to the user
	return blog
