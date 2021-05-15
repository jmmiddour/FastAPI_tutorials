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
