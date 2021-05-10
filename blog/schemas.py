# Import BaseModel from pydantic for the class
from pydantic import BaseModel


# Create a class for the blog
# Moved the class and BaseModel module to the schemas.py file
class Blog(BaseModel):
	title: str
	body: str
