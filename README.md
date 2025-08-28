# ASAL Auth Task

## Project Overview

ASAL Auth Task is a Django-based project focused on implementing authentication features using Django REST Framework. This project provides user registration, login, and logout

## Features

* User registration and login and logout
* Token-based authentication (JWT or DRF Token)
* API endpoints for user management
* Clean project structure suitable for extension

## Technology Stack

* Python 3.8+
* Django 4.x
* Django REST Framework
* Django Allauth (optional for email/social authentication)
* SQLite / PostgreSQL (configurable)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/darxx03eh/ASAL-Auth-Task.git
cd ASAL-Auth-Task
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

* On Windows:

```bash
venv\Scripts\activate
```

* On macOS/Linux:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

## Project Structure

```
ASAL-Auth-Task/
├── api/                 # API endpoints and serializers
├── auth_task/           # Django project settings
├── utils/               # Utility functions
├── manage.py
├── requirements.txt
└── .gitignore
```

## example for error response
```
{
  "error": {
    "status_code":400,
    "message":"Bad request syntax or unsupported method",
    "details":{
      "username":[
        "Username must be at least 10 character long."
      ],
      "email":[
        "Enter a valid email address."
      ]
    }
  }
}
```

##


