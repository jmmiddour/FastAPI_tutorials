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


### Basic Concepts

- Path Parameters:


- API Docs - Swagger/Redocs:


- Query Parameters:


- Request Body:


### Intermediate Concepts

- Debugging FastAPI


- Pydantic Schemas


- SQLAlchemy Database Connection


- Models and Table


### Database Tasks

- Store blog to database


- Get blogs from database


- Delete


- Update


### Responses

- Handling Exceptions


- Return Response


- Define response model


### User and Password

- Create user


- Hash user password


- Show single user


- Define docs tags


### Relationship

- Define User to Blog relationship


- Define Blog to User relationship


### Refactor for Bigger Application

- API Router


- API Router with Parameters


### Authentication using JWT (JSON Web Token)

- Create Login Route


- Login and verify password


- Return JWT access token


- Routes behind authentication


### Deploy FastAPI

- Using Deta.sh website to deploy
