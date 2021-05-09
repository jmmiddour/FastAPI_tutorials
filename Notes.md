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


- **Request Body:**


### Intermediate Concepts

- **Debugging FastAPI**


- **Pydantic Schemas**


- **SQLAlchemy Database Connection**


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
