# My Notes

[FastAPI - A python framework | Full Course](https://youtu.be/7t2alSnE2-I)

## Features of using FastAPI

- Automatic Docs using Swagger UI
  
    - Makes it user-friendly with a "try it out" feature.
      
    - Also have the option of static docs.

- Modern Python using Python 3.6 typing for type casting variables and Pydantic.

- Based on Open Standards
  
    - JSON Schema (Cross-functional)
      
    - Open API (Linux-Based)

- Security and Authentication
  
    - HTTP Basic
      
    - OAuth2 (also with JWT tokens)
      
    - API keys in:
      
        - Headers
          
        - Query Parameters
          
        - Cookies, etc.

- Dependency Injection

- Unlimited "plug-ins"

- Testing - Has it's own testing system using pytest

- Uses Starlette (another framework through Python) Features
  
    - WebSocket support
      
    - GraphQL support
      
    - In-process background tasks
      
    - Startup and shutdown events
      
    - Test client built on requests
      
    - CORS, GZip, Static Files, Streaming responses
      
    - Session and Cookie support

- Other Supports:
  
    - SQL databases
      
    - NoSQL databases
      
    - GraphQL


## Getting Started

The creator of FastAPI [Sebastian Ramirez's GitHub](https://github.com/tiangolo/)

### Install and Setup

- Verify that you have Python 3.6 or greater installed on your machine

- Need to install fastapi via the command prompt: `pip install fastapi`

- Need to install uvicorn via the command prompt: `pip install uvicorn`

- Create the `main.py` file for the app (See the `main.py` file in this directory for notes in what to do there)

- To run the app on a local server, in the command prompt: `uvicorn main:app --reload` (the `--reload` flag will allow the server to automatically reload when you update something in any of the files)

### Break it Down... How is it Structured?

- Create a `.gitignore` file and add any files that are not needed to upload to GitHub

- Start by initializing a git repository, with the following commands in the terminal:
  
    - `git init`
      
    - `git add .`
      
    - `git commit -m "<commit message>"`

- When calling up the `uvicorn` server `main:app` is the `<file name>:<variable FastAPI was assigned to>` and the `--reload` flag tells the server to automatically reload when any changes are made to the files within the app.


### Basic Concepts

- **Path Parameters:**
  
  - If you want to have both dynamic and static routes (paths) you have to be mindful of placement within the code base.
    
  - For a dynamic path, the user can change the path by simply adding the parameter in to the url like so:
    
    - `.../blogs/100`
      
      - If the route (path) is set up as:
        
        - `@app.get('/blog/{blog_id}')`
  
        - A dynamic path parameter needs to have `{}` around it, this tells FastAPI that this is a path parameter.
        
      - The above url would show the blog at blog id 100.
    
  - For a static path, the url must be entered exactly as it is set up in the routing (path) code, like so:
    
    - `@app.get('/blog/unpublished')`
      
    - The url must be typed as:
      
      - `.../blog/unpulished` in order for it to be valid.
    
  - If you have a static path that is a subpath of another path that is a dynamic subpath of the same parent path, the static subpath needs to be first in the code base or it will read the dynamic subpath first and run the code for it and will never make it to the static subpath code.
    
  - FastAPI reads code / paths from top to bottom. Similar to how Python reads if statements. It will first look at the first path, if the path entered does not match, it ignores the code for that path and moves to the next path. If that path still does not match, it moves to the next path, and so on until it finds the matching path or reaches the end of the code. This is why placement of static and dynamic paths are so important.

- **API Docs - Swagger/Redoc:**

  - ***Swagger UI:***
    
    - Is accessed via url `.../docs`
      
    - Is dynamic and interactive
      
    - Shows all routes (paths) within the app.
      
    - Allows the user to "try out" each path individually.
      
      - When the user "tries it out", they will get the following responses:
        
        - cURL: client URL: command line tool for file transfer with a URL syntax
          
        - The Request URL
          
        - The Server Response:
          
          - The Response Code 
            
          - The Response Body
            
          - The Response Headers
            
            - content-length
              
            - content-type
              
            - date
              
            - server
          
        - Responses:
          
          - The Response Code
            
          - The Response Description
      
    - Has a nice user-friendly interface.
      
    - Is build out automatically with FastAPI
  
  - ***ReDoc:***
    
    - Is accessed via url `.../redoc`
      
    - Is static and just shows the basic documentation of the API
      
    - This is also automatically created when using FastAPI

- **Query Parameters:**
  
  - Can add a query parameter to the url to limit the number of results like so:
    
    - `@app.get('/blog?limit=10')` will limit the amount of results to 10
    
  - Can add more than one query to the url like so:
    
    - `@app.get('/blog?limit=10&published=True')` will limit the results to only the first 10 published blogs
    
  - You can also make it dynamic where the user can enter any value that they want as the query parameters, like so:
    
    ```
    @app.get('blog')
    def index(limit, published: bool):
        if published:
		    return {'data': f'{limit} published blogs from the database.'}
        else:
            return {'data': f'{limit} blogs from the database.'}
    ```
    
    - With the above code the user will need to enter the url as follows:
      
      - `.../blog?limit=<number>&published=<true or false only>`
      
    - However, the above code will return an error message stating that the field(s) are required if the user does not enter anything in the url other than `.../blog` or only enters one of the parameters.
      
    - To make this more user-friendly, you can add default values, like so:
    
    ```
    @app.get('/blog')
    def index(limit=10, published: bool = True):
    	if published:
            return {'data': f'{limit} published blogs from the database.'}
        else:
            return {'data': f'{limit} blogs from the database.'}
    ```
    
    - Now when the user types just `.../blog` it will show the first 10 published blogs by default, while still giving the user the ability to change those parameters through the url.
      
    - What if you want the user to have a parameter they can set, such as way to sort the blogs, but do not want it to be a required parameter?
    
    ```
    from typing import Optional  # Gives you the ability to create an optional parameter
    
    
    @app.get('/blog')
    def index(limit=10, published: bool = True, sort: Optional[str] = None):
    	if published:
            return {'data': f'{limit} published blogs from the database.'}
        else:
            return {'data': f'{limit} blogs from the database.'}
    ```
    
    - You can use the `Optional` method from the `typing` library to do this.
      
      - You still need to define the data type, but you do so in `[]`
        
      - Then assign it a default value, which `None` will work becuase it will not be a required parameter.
  
  - How does FastAPI know the differance between a path parameter and a query parameter? 
    
    - A "path parameter" will have `{}` surrounding it in the `app.get()` path
  
    - A "query parameter" is added onto the url by the user after adding `?` at the end of the url.

- **Request Body:**

  - `@app.post()` use this request method to "create" something.
  
  - When you need to send data from the client (browser) to your API, you send it as a **"request body"**. A **request body** is data sent by the client to your API. A **response body** is the data your API sends to the client. Your API almost always has to send a **response body** but the clients don't necessarily need to send **request bodies** all the time.
  
  - To declare a **request body** you use `BaseModel` from the `pydantic` library.
  
  - Whenever you create a new `class` item, you have to inherit from the `pydantic` `BaseModel` and that will tell FastAPI that `class` is a model
  
    - Then you define the parameters that are needed for that class. Example:
      
      ```
      class Item(BaseModel):
          name: str
          description: Optional[str] = None
          price: float
          tax: Optional[float] = None
      ```
      
    - Then you will declare it as a request body, like so:
  
      ```
      @app.post('/items/')
      async def create_item(item: Item):
          return item
      ```
      
  


### Intermediate Concepts

- **Debugging FastAPI**
  
  - Using the "breakpoint" dot in your IDE:

    - When you add the red "breakpoint" dot between the number and your code, that means that when you run the debugger it will show what your code has done up to that point and that is where it will stop until you tell it to continue on.

- **Pydantic Schemas**

  - FastAPI does not require you to use a SQL (relational) database. You can use any database you want to. 
  
  - Using `SQLAlchemy` you can easily adapt it to any database supported, like:
    
    - PostgreSQL
      
    - MySQL
      
    - SQLite
      
    - Oracle
      
    - Microsoft SQL Server, etc.
  
  - SQLAlchemy is a Python SQL Toolkit and Object Relational Mapper (ORM). It gives application developers the full power and flexibility of SQL.
  
  - Need to create a new file `requirements.txt` and in this file, need to add fastapi and uvicorn.
  
  - Then, in the terminal, `python -m venv blog-env` to create a virtual environment called "blog-env"
  
  - Then, in the terminal, `pip install -r requirements.txt` to install all the packages in the requirements file.
  
  - Create a new directory "blog"
  
    - Inside "blog", create a new blank file `__init__.py`
    
    - Also, inside "blog", create a new file `main.py`
  
  - If you want the server to run the `main.py` file in the blog directory, you will have to do it like this: `uvicorn blog.main:app --reload`, otherwise it will run the server based on the `main.py` file in the root directory.

- **SQLAlchemy Database Connection**

  - Create a new file (`database.py`) in the blog directory for your database code.
  
  - Import `create_engine` from `sqlalchemy`.
  
    - Create a global variable for the database url
  
    - Create the engine using the global variable defined above and `connect_args={'check_same_thread': False}` which is something that is used by FastAPI

  - Import `declarative_base` from `sqlalchemy.ext.declarative` to declare the mapping for the database
  
    - Declare the mapping to the database using the above method
  
  - Create a session by first importing `sessionmaker` from `sqlalchemy.orm`
  
    - Create the session using the above module: `session = sessionmaker(bind=engine, autocommit=False, autoflush=False)`

- **Models and Table**

  


### Database Tasks

- **Store blog to database**


- **Get blogs from database**


- **Delete**


- **Update**


### Responses

- **Handling Exceptions**


- **Return Response**


- **Define response model**


### User and Password

- **Create user**


- **Hash user password**


- **Show single user**


- **Define docs tags**


### Relationship

- **Define User to Blog relationship**


- **Define Blog to User relationship**


### Refactor for Bigger Application

- **API Router**


- **API Router with Parameters**


### Authentication using JWT (JSON Web Token)

- **Create Login Route**


- **Login and verify password**


- **Return JWT access token**


- **Routes behind authentication**


### Deploy FastAPI

- **Using Deta.sh website to deploy**
