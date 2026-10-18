
# SWYNEX Python API Project

## 1. Project Overview
This project is a REST API built using Python and Flask.
It is a Task Manager API that allows users to create,
view, update, and delete tasks using HTTP requests.

## 2. Objectives
- Learn the basics of REST API development.
- Understand HTTP methods and status codes.
- Handle JSON requests and responses.
- Implement input validation and error handling.

## 3. Technologies Used
- Python 3
- Flask
- REST API
- JSON
- Postman / PowerShell for testing

## 4. Features
- Retrieve all tasks.
- Retrieve a task by its ID.
- Create a new task.
- Update task details or completion status.
- Delete an existing task.
- Validate user input.
- Return meaningful error messages.
- Handle invalid endpoints and HTTP methods.

## 5. Project Structure

SWYNEX-Python-API-Project/
├── app.py
├── requirements.txt
└── README.md

## 6. Installation

Make sure Python 3 is installed.

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required dependency:

```bash
python -m pip install -r requirements.txt
```

## 7. How to Run

Start the Flask application:

```bash
python app.py
```

Open the following URL in your browser:

http://127.0.0.1:5000/

The API runs locally on your computer.

## 8. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Check API status |
| GET | /tasks | Retrieve all tasks |
| GET | /tasks/<id> | Retrieve a task by ID |
| POST | /tasks | Create a task |
| PUT | /tasks/<id> | Update a task |
| DELETE | /tasks/<id> | Delete a task |

## 9. Example POST Request

URL:
http://127.0.0.1:5000/tasks

JSON request body:

```json
{
  "title": "Learn Python API"
}
```

Example response:

```json
{
  "id": 1,
  "title": "Learn Python API",
  "completed": false
}
```

## 10. Validation and Error Handling

The API validates task titles and JSON request bodies.

Examples of HTTP status codes:
- 200: Request successful.
- 201: Task created successfully.
- 400: Invalid input.
- 404: Task or endpoint not found.
- 405: HTTP method not allowed.

## 11. Testing

The API can be tested using Postman or PowerShell.

Test the following:
- Retrieve all tasks.
- Create a task.
- Update a task.
- Delete a task.
- Send invalid input.
- Request a task that does not exist.

## 12. Limitations

Task data is stored in memory.
All tasks are reset when the application restarts.
A database can be added in a future version.

## 13. Learning Outcomes

Through this project, I practised:
- Python functions and dictionaries.
- Flask routes and HTTP methods.
- JSON request and response handling.
- Input validation and error handling.
- REST API testing.

## 14. Internship

Project created as part of Task 3 of the
SWYNEX Python Internship.
