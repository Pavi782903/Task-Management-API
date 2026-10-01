# Task Management API

A REST API developed using:

- FastAPI
- Python
- Pydantic
- SQLAlchemy
- SQLite
- Uvicorn

## Features

- Create task
- Get all tasks
- Get task by ID
- Update task
- Delete task
- Filter by status
- Filter by priority
- Search by assigned person
- Pydantic validation
- Enum validation
- Date validation
- Proper HTTP status codes
- Exception handling
- Swagger UI
- SQLite database

## Project Structure

```text
TASK_MANAGEMENT_API/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   │
│   └── routes/
│       ├── __init__.py
│       └── tasks.py
│
├── task_management.db
├── requirements.txt
├── README.md
└── .gitignore