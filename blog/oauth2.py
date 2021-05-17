"""
This file contains the code needed for oauth2 authentication.
"""

# Imports:
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import JWT_token


# Create the oauth2_scheme to get the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_scheme)):
	"""
	Function to get the current logged in user based on the token passed in.

	:param token: str: gets the token from the oauth2_scheme
	:return: the current user after verification
	"""
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Could not validate credentials",
		headers={"WWW-Authenticate": "Bearer"},
	)

	return JWT_token.verify_token(token, credentials_exception)
