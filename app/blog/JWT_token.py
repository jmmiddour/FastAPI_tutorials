"""
This file contains everything for generating the JWT_token
"""
# Imports
from datetime import datetime, timedelta
from jose import jwt, JWTError
from ..blog import schemas

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
	"""
	Function to create a JWT token.

	:param data: dict: the data to be encoded
	:return: data encoded as a JWT token
	"""
	to_encode = data.copy()
	expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

	return encoded_jwt


def verify_token(token, credentials_exception):
	"""
	Function to verify the token for the current session and user.

	:param token: str: the current user's session token
	:param credentials_exception: Error to raise token is invalid
	:return: bool: True if the token has been verified, False if not
	"""
	try:
		# Parses the long string into a token for that user
		# https://www.programcreek.com/python/example/62091/jwt.decode
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		# Get the email inputted
		email: str = payload.get("sub")

		# If there is no email entered...
		if email is None:
			# Raise the credentials exception error message
			raise credentials_exception

		# Set the token data schema for the email
		token_data = schemas.TokenData(email=email)

	except JWTError:  # Otherwise, raise the credentials exception error message
		raise credentials_exception
