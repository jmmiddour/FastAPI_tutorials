"""
This file contains all the user routes/paths
"""
# Imports
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..hashing import Hash

# Initialize the APIRouter
router = APIRouter(tags=['Users'])

# Create a variable for the get_db function
get_db = database.get_db

"""
Need to go to the `main.py` file and copy all of the paths for the blogs.
Then paste them below and change `app` to `router` --v
"""


# Create the user path with hashing of passwords
@router.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
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


# Create a new path to show user by their id
@router.get('/user/{user_id}', response_model=schemas.ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
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
