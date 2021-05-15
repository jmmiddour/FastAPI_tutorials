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

- First set up a virtual environment, not a requirement, but it is best practice to do so in order to avoid any conflicts.

  - Do the following commands in the terminal:
    
    - `python3 -m venv <name of environment>` creates a new folder in the current directory with the name of the environment. This creates your new environment variables for this project specifically.
  
    - `<name of environment>\Scripts\activate.bat` to activate the virtual environment on a Windows machine or if using the bash command line tool you need to enter `source <name of environment>/Scripts/activate` in the command line. Or `source <name of environment>/bin/activate` on Unix, or MacOS.
  
    - Need to install fastapi via the command prompt: `pip install fastapi`

    - Need to install uvicorn via the command prompt: `pip install uvicorn`
  
    - If you have an older version of pip installed on your computer, run this command to update it: `python -m pip install --upgrade pip` while in your virtual environment.

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
  
  - Need to create a new file `requirements.txt` and in this file, need to add `fastapi`, `uvicorn`, and `sqlalchemy`.
  
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
  
  - Create a session by first importing `sessionmaker` from `sqlalchemy.orm`
  
    - Create the session using the above module: `LocalSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)`

  - Import `declarative_base` from `sqlalchemy.ext.declarative` to declare the mapping for the database
  
    - Declare the mapping to the database using the above method

- **Models and Table**

  - Open TablePlus and click on "Create a new connection..." on the bottom of the window

    - Click on SQLite
  
    - Only fields that are required is the name and the file location.
  
  - In FastAPI the schema is called the model. So you need to create a model (class) for each table you are going to have in your database.
  
    - Create a `models.py` file in the blog directory to hold all the code for the tables your database.
  
      - Create your table classes in the `models.py` file.
  
  - In the `main.py` in blog directory, need to add the following code at the top: `models.Base.metadata.create_all(engine)` to create the database.

  - Then in the `models.py` file need to import `Column`, `Integer`, and `String` from `sqlalchemy` and from the `database.py` file, `Base`.
  
  - Create a class for the table blog:
    ```
    class Blog(Base):
        __tablename__ = 'blogs'
        id = Column(Integer, primary_key=True, index=True)
        title = Column(String)
        body = Column(String)
    ```


### Database Tasks

- **Store blog to database**
  
  - In the `main.py` file, need to import some new libraries:
  
    - `from sqlalchemy.orm import Session`
  
    - `from fastapi import Depends`
  
    - `from .database import LocalSession`
  
  - In the `main.py` file, need to add some parameters to the method `create()` in the post request method for `'/blog'`
  
    - `db: Session = Depends(get_db)` this turns the Session into a pydantic session using the `Depends` from `fastapi`.
  
      - `get_db` is a function we will need to create above the post request method to get the database connection.
  
  - In the `main.py` file, need to add some new functionality to the `create()` method, so it now looks like this:
  
    ```
    def create(request: schemas.Blog, db: Session = Depends(get_db)):
        new_blog = models.Blog(title=request.title, body=request.body)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return new_blog
    ```

- **Get blogs from database**

  - Add a new get request method to the `main.py` file to list all of the blogs in the database in a JSON format:
  
    ```
    @app.get('/blog')
    def get_blogs(db: Session = Depends(get_db)):
        blogs = db.query(models.Blog).all()
        return blogs
    ```

  - Add a new get request method to the `main.py` file to show a single blog by its id number:
  
    ```
    @app.get('/blog/{id}')
    def show_blog(id, db: Session = Depends(get_db)):
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()
        return blog
    ```

- **Delete**

  - In the `main.py` file, add the following code:
  
    ```
    @app.delete('/blog/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
        def destroy(blog_id, db: Session = Depends(get_db)):
            blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    
            if not blog.first():
                raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			        detail=f'Blog with the id {blog_id} is not available. Please try '
			               f'another blog id number.')
    
            blog.delete(synchronize_session=False)
            db.commit()
            return None
    ```
    
    - `database.query()` has its own `.delete()` method. Need to read up further on the different inputs for `synchronize_session=` in the [sqlalchemy documentation](https://docs.sqlalchemy.org/en/14/orm/session_basics.html#orm-expression-update-delete) but for now we are just going to set it to False.
  
      - `False` - don't synchronize the session. This option is the most efficient and is reliable once the session is expired, which typically occurs after a `commit()`, or explicitly using `expire_all()`. Before the expiration, objects that were updated or deleted in the database may still remain in the session with stale values, which can lead to confusing results.
        
      - `fetch` - Retrieves the primary key identity of affected rows by either performing a `SELECT` before the `UPDATE` or `DELETE`, or by using `RETURNING` if the database supports it, so that in-memory objects which are affected by the operation can be refreshed with new values (updates) or expunged from the `Session` (deletes). Note that this synchronization strategy is not available if the given `update()` or `delete()` construct specifies columns for UpdateBase. `returning()` explicitly.
  
      - `evaluate` - Evaluate the `WHERE` criteria given in the `UPDATE` or `DELETE` statement in Python, to locate matching objects within the `Session`. This approach does not add any round trips and in the absence of `RETURNING` support is more efficient. For `UPDATE` or `DELETE` statements with complex criteria, the `evaluate` strategy may not be able to evaluate the expression in Python and will raise an error. If this occurs, use the `fetch` strategy for the operation instead.
  
        - **WARNING:**
  
          The `evaluate` strategy should be avoided if an `UPDATE` operation is to run on a `Session` that has many objects which have been expired, because it will necessarily need to refresh those objects as they are located which will emit a `SELECT` for each one. The Session may have expired objects if it is being used across multiple `Session.commit()` calls, and the `Session.expire_on_commit` flag is at its default value of `True`.

- **Update**

  - In the `main.py` file do the following code:
    
    ```
    @app.put('/blog/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
        def update(blog_id, request: schemas.Blog, db: Session = Depends(get_db)):
            blog = db.query(models.Blog).filter(models.Blog.id == blog_id)
    
            if not blog.first():
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f'Blog with the id {blog_id} is not available. Please try '
                           f'another blog id number.')
    
            blog.update(dict(request))
            db.commit()
            return f'Blog {blog_id} has been successfully updated!'
    ```
    
    - Ran into an issue with the update query. On the video he states to code it `...update(request)` but when trying to run it that way, I was getting an error: 

      ```
      AttributeError: 'Blog' object has no attribute 'items'
      ```
      
      After doing some research on this issue, I found out that it has something to do with the differences in the version of SQLAlchemy that he is using versus me. He is using v1.3, and I am using the newest version which is v1.4.
  
      In order to fix this bug, I just need to code it as: `...update(vars(request))` which the `vars()` function is a python builtin and returns the `__dict__` attribute of the given object, if it has one, otherwise, it will raise a `TypeError` exception. 

### Responses

- **Exception and Status Code**

  - When creating something the response code should be `201` not `200`.
  
    - You will first need to import `status` from `fastapi`.

    - Then all you have to do to change this is to add `status_code=status.HTTP_201_CREATED` in the parameters when you create the path request with `@app.post('<path>', status_code=status.HTTP_201_CREATED)`

  - If you want your user to see a customized response code if they enter an invalid `id` number for a blog, do the following the `main.py` file:
  
    - Need to import `Response` from `fastapi`
  
    - The go to the `@app.get('/blog/{id})` path method and put in the parameter `status_code=200` as the default status code.
  
    - Then need to add `response: Response` after `blog_id` as a parameter in the `def show_blog` function.
  
    - After you query the database for the blog, add the following code block:
  
      ```
      if not blog:
          response.status_code = status.HTTP_404_NOT_FOUND
          return {
              'detail':
                  f'Blog with the id {blog_id} is not available. Please '
                  f'try another blog id number.'
          }
      ```
      
    - The above code will override the default status code if the if statement is True and returns the 404 status, and a customized message in the response body for the user.

- **Handling Exceptions**

  - If you want to add an exception to the status code the user is give you can do so as follows:
  
    - Import `HTTPException` from fastapi
  
    - Say you have a `user` database, and you want to raise an exception to the status code if the user is already in the database to avoid duplicates. You could code it like this:
  
      ```
      if user:
          raise HTTPException(status_code=400, detail=f'User {user} is already registered.')
      ```
      
    - Or if you go with the blog example we have been working with, and check for the edge case of the user entering an invalid blog id number. You could code it like this:
  
      ```
      if not blog:
          raise HTTPException(
              status_code=status.HTTP_404_NOT_FOUND,
              detail=f'Blog with the id {blog_id} is not available. Please try '
                     f'another blog id number.')
      ```

- **Define response model**

  - [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/response-model/)

  - A response model is pydantic model that determines what is returned to the user from the database.
  
  - The code for the response model will be found in the `schemas.py` file.
  
  - The way that you define what response model you want for each path is: `@app.<method>('<path>', response_model=schemas.<schema class>`
  
  - If you have multiple queries that you need to show the user at once:
  
    - Import the `List` method from the `typing` library
  
    - Then the way you would define the response model for multiples is: `@app.<method>('<path>', response_model=List[schemas.<schema class>]`

### User and Password

- **Create user**

  - In the `schemas.py` file, need to create a schema for user:
    
    ```
    class User(BaseModel):
        name: str
        email: str
        password: str
    ```
    
  - In the `models.py` file, need to define a new model for the user table in the database:
  
    ```
    class User(Base):
        __tablename__ = 'users'
    
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String)
        email = Column(String)
        password = Column(String)
    ```

  - Now in the `main.py` file, create the path for creating the user:
  
    ```
    @app.post('/user')
    def create_user(request: schemas.User, db: Session = Depends(get_db)):
        new_user = models.User(name=request.name, email=request.email,
                               password=request.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    ```

- **Hash User Password**

  - [Hash the Password in Video](https://youtu.be/7t2alSnE2-I?t=8588)
  
  - [FastAPI Documentation - OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=hash)
  
  - First need to install `passlib` and `bcrypt`. This can be done by just adding to your `requirements.txt` file or you can `pip install passlib bcrypt` into your virtual environment. If you add it to your `requirements.txt` file then you also need to reinstall your requirements file in your terminal in your virtual environment with `pip install -r requirements.txt`.
  
  - In `main.py` file, import `CryptContext` from `passlib.context`
  
  - Add a variable to instantiate the CryptContext function: `pwd_cxt = CryptContext(schemas=['bcrypt'], deprecated='auto')`
  
  - Then need to change the path to the following in order to use the hashing function:
  
    ```
    @app.post('/user')
    def create_user(request: schemas.User, db: Session = Depends(get_db)):
        hashed_pwd = pwd_cxt.hash(request.password)
        new_user = models.User(name=request.name, email=request.email,
                               password=hashed_pwd)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    ```
    
  - Another way to hash the passwords:
  
    - Create another file called `hashing.py`
  
    - Move the import `CryptContext` from `passlib.context` to `hashing.py`
  
    - Move the variable to instantiate the CryptContext function: `pwd_cxt = CryptContext(schemas=['bcrypt'], deprecated='auto')` to `hashing.py`
  
    - Then need to change the path, slightly, to the following in order to use the hashing function:
  
      ```
      @app.post('/user')
      def create_user(request: schemas.User, db: Session = Depends(get_db)):
          new_user = models.User(name=request.name, email=request.email,
                                 password=Hash.bcrypt(request.password))
          db.add(new_user)
          db.commit()
          db.refresh(new_user)
          return new_user
      ```

- **Show single user**

  - [Show a User in Video](https://youtu.be/7t2alSnE2-I?t=9036)
  
  - In the `schemas.py` file, create a pydantic model to return only the user name and password to the user:
    
    ```
    class ShowUser(BaseModel):
        name: str
        email: str
    
        class Config():
            orm_mode = True
    ```
    
  - In the `main.py`, modify the code for the user path: `@app.post('/user', response_model=schemas.ShowUser)`

  - Also need to add another path to the `main.py` file to get the user information by the id number:
  
    ```
    @app.get('/user/{user_id}', response_model=schemas.ShowUser)
    def get_user(user_id: int, db: Session = Depends(get_db)):
        user = db.query(models.User).filter(models.User.id == user_id).first()
    
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'The user with the id {user_id} is not available. Please '
                       f'try another user id number.')
    
        return user
    ```

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
