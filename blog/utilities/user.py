"""
This file contains all the user routes/paths
"""
# Imports
from fastapi import status, HTTPException
from .. import schemas, models
from ..hashing import Hash


def create_user(request: schemas.User, db):
	"""
	Function to create a new user and store their data in the database.

	:param request: input from the user through the API
	:param db: connection to the database
	:return: JSON: file with the new user's data
	"""
	# # Hash the password when it is passed in by the user
	# hashed_pwd = pwd_cxt.hash(request.password)
	# ^-- Comment the above out because we moved it to hashing.py
	# Create the new user
	# new_user = models.User(name=request.name, email=request.email,
	#                        password=hashed_pwd)
	# ^-- Commented the above out because we created a class in hashing.py
	new_user = models.User(name=request.name, email=request.email,
	                       password=Hash.bcrypt(request.password))
	# Add the new user to the database
	db.add(new_user)
	# Commit the changes to the database
	db.commit()
	# Refresh the database to reflect the changes
	db.refresh(new_user)
	# Return the new user just entered to the user
	return new_user


def get_user(user_id, db):
	"""
	Function to get the data from a database, based on the user id inputted.
	:param user_id: int: the id number of the user
	:param db: the connection to the database
	:return: JSON: file with the data for the specified user from the database
	"""
	# Query the database to the get the user data by the user id
	user = db.query(models.User).filter(models.User.id == user_id).first()

	# Check edge case of invalid user id entered
	if not user:
		# Return not found status code and message to the user
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail=f'The user with the id {user_id} is not available. Please '
			       f'try another user id number.')

	# Return the user specified by the id entered
	return user
