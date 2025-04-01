# Todo API Backend

## Description

This is a Django-based REST API for a Todo application. It provides user authentication and CRUD operations for managing todos. The API follows RESTful principles and includes user registration, login, and logout functionalities.
This API was created as part of Assignment 1 for my CI/CD course. I am currently studying at the Auckland Institute of Studies.

## Table of Contents

- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Demo

A live API demo is available here:
[Live API Demo](#https://backend-todo-list-btp5n3r8h-niraj-paudels-projects.vercel.app/)

## Installation

Ensure you have Python installed. Then, clone the repository and set up the project:

```sh
git clone https://github.com/NPZlatu/Backend-TodoList
cd <project-name>
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage

### Run Development Server

```sh
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

### Run Migrations

```sh
python manage.py migrate
```

## Features

- User authentication (register, login, logout)
- Create, read, update, and delete (CRUD) operations for todos
- Token-based authentication
- Environment-based configuration management

## API Endpoints

### Authentication

- `POST /register/` - Register a new user
- `POST /login/` - Login user and obtain an authentication token
- `POST /logout/` - Logout the authenticated user

### Todo Management

- `GET /todos/` - Retrieve all todos
- `POST /todos/` - Create a new todo
- `GET /todos/<id>/` - Retrieve a specific todo
- `PUT /todos/<id>/` - Update an existing todo
- `DELETE /todos/<id>/` - Delete a todo

## Environment Variables

Create a `.env` file in the project root with the following if needed, otherwise use default SQLite:

```
SECRET_KEY=<your-secret-key>
DB_HOST=<database-host>
DB_NAME=<database-name>
DB_USER=<database-user>
DB_PASSWORD=<database-password>
DB_PORT=<database-password>
```

## Project Structure

```
📦 Backend-TodoList
├── 📂 todo                # Main API application
│   ├── 📂 migrations      # Database migrations
│   ├── 📂 tests
        ├── 📂 unit         # unit tests
        ├── 📂 integration  # integration-tests
│   ├── 📜 views.py        # API views
│   ├── 📜 serializers.py  # API serializers
│   ├── 📜 urls.py         # API routes
│   ├── 📜 models.py       # Database models
├── 📂 todo_project        # Main API project
    ├── 📜 manage.py       # Django entry point
    ├── 📜 settings.py     # Django setting config file
    ├── 📜 urls.py         # URL entry point
    ├── 📜 wsgi.py         # Connecting Django to WSGi servers
├── 📜 .env                # Environment variables
├── 📜 requirements.txt    # Project dependencies
└── 📜 README.md           # Documentation
```

## Unit Testing

```sh
python manage.py test todo.tests.unit
```

## Unit Testing

```sh
python manage.py test todo.tests.integration
```

## Deployment

The continuous deployment in Vercel has been enabled in this project. Any changes made will be deployed to the Vercel.

## Contributing

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a pull request.

## License

This project is licensed under the MIT License.
