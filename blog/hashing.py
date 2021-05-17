"""
This file holds the code for hashing passwords
	for user accounts.
"""


# Import CryptContext from passlib to hash the passwords
from passlib.context import CryptContext


# Instantiate CryptContext to hash passwords
pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash():
	def bcrypt(password: str):
		# Hash the password when it is passed in by the user
		return pwd_cxt.hash(password)

	def verify(hashed_pwd, plain_pwd):
		"""
		Function to verify the stored hashed password matches the hash for
			the inputted password.
		:param hashed_pwd: str: hashed password that is stored in the database
		:param plain_pwd: user inputted password through the API
		:return: bool: True if there is a match, False if there is no match.
		"""
		return pwd_cxt.verify(plain_pwd, hashed_pwd)
