# Task Manager

A task management application built with Python, featuring a CLI interface, REST API, JSON persistence, object-oriented design, and automated testing.

## Features

* Add tasks
* View tasks
* Search tasks
* Edit tasks
* Complete tasks
* Delete tasks
* Persistent task storage using JSON
* REST API using FastAPI
* Request and response validation with Pydantic
* HTTP error handling
* Automated unit tests with pytest

## Project Structure

```text
task-manager/
├── main.py                  # CLI application
├── api.py                   # FastAPI REST API
├── task.py                  # Task model
├── task_manager.py          # Task management logic
├── tasks.json               # Persistent task storage
└── tests/
    ├── __init__.py
    ├── test_task.py
    └── test_task_manager.py
```

## Technologies

* Python
* FastAPI
* Pydantic
* pytest
* JSON
* Git & GitHub

## Architecture

The application separates responsibilities into different layers:

```text
CLI / REST API
      ↓
 TaskManager
      ↓
    Task
      ↓
  JSON Storage
```

* **Task** — Represents an individual task and handles task-level operations.
* **TaskManager** — Handles task creation, searching, editing, completion, deletion, and persistence.
* **CLI** — Provides a command-line interface for interacting with the application.
* **FastAPI** — Provides REST API endpoints for interacting with tasks.
* **Tests** — Verifies task and task manager behavior using pytest.

## REST API

The application exposes the following endpoints:

| Method | Endpoint                    | Description         |
| ------ | --------------------------- | ------------------- |
| GET    | `/`                         | API welcome message |
| GET    | `/tasks`                    | Get all tasks       |
| GET    | `/tasks/{task_id}`          | Get a task by ID    |
| POST   | `/tasks`                    | Create a task       |
| PUT    | `/tasks/{task_id}`          | Update a task       |
| PATCH  | `/tasks/{task_id}/complete` | Complete a task     |
| DELETE | `/tasks/{task_id}`          | Delete a task       |

FastAPI automatically provides interactive API documentation at:

```text
/docs
```

## Running the CLI

Run:

```bash
python main.py
```

## Running the API

Start the FastAPI server with:

```bash
uvicorn api:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

to interact with the API through the Swagger UI.

## Running Tests

Run the complete test suite with:

```bash
pytest
```

The tests cover:

* Task creation
* Task completion
* Task editing
* Task serialization/deserialization
* Task management operations
* JSON persistence
* Save/load behavior using isolated temporary files

## What I Learned

This project helped me practice:

* Python OOP
* Classes and class methods
* Separation of concerns
* JSON serialization and deserialization
* File persistence
* REST API development
* FastAPI
* Pydantic models
* HTTP status codes and error handling
* Automated testing with pytest
* Pytest fixtures such as `tmp_path`
* Git and GitHub workflow

## Future Improvements

Possible future improvements include:

* Replace JSON storage with SQLite
* Add database-backed persistence
* Add authentication
* Add pagination and filtering
* Improve API test coverage
* Containerize the application with Docker
