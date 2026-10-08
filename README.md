# Smart Service Request & Integration API

A REST API project using Python, FastAPI, REST APIs, MySQL/SQLite, JWT authentication, SQLAlchemy and an external API.

## Features
- User registration and login
- JWT authentication
- Protected REST endpoints
- Service request CRUD
- Request status updates
- MySQL support with SQLite fallback for easy testing
- External REST API integration
- Pydantic validation
- Swagger/OpenAPI documentation

## Run
1. `python -m venv venv`
2. Windows: `venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. Copy `.env.example` to `.env`
5. For quick testing use `DATABASE_URL=sqlite:///./service_requests.db`
6. Start: `uvicorn app.main:app --reload`
7. Open `http://127.0.0.1:8000/docs`

## MySQL
Create a database named `service_requests`, then set:
`DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/service_requests`

## Endpoints
POST `/api/v1/auth/register`
POST `/api/v1/auth/login`
POST `/api/v1/requests`
GET `/api/v1/requests`
GET `/api/v1/requests/{request_id}`
PUT `/api/v1/requests/{request_id}`
PATCH `/api/v1/requests/{request_id}/status`
DELETE `/api/v1/requests/{request_id}`
GET `/api/v1/external/posts/{post_id}`

External API: JSONPlaceholder.

## Interview topics to understand
FastAPI, REST, HTTP methods/status codes, JWT and bearer tokens, authentication vs authorization, SQLAlchemy, MySQL, Pydantic validation, external API calls, error handling, and environment variables.

**Important:** Run and test this project and understand the code before presenting it in an interview.
