# task 4 — build RESTful APIs using Django REST Framework

# prerequisites:
# - activated the virtual environment
# - installed DRF using pip
# - added 'rest_framework' to INSTALLED_APPS in settings.py
# - added .gitignore to exclude env/, __pycache__/, db.sqlite3, etc.

# model creation

# created a Book model with fields: title, author, published date, and price
# added constraints:
# - title is unique (unique=True)
# - published cannot be null (null=False)
# - price uses DecimalField with 2 decimal places

# this allows us to structure the data we want to expose via the API

# migrations

# ran makemigrations to generate migration files from models
# ran migrate to apply those changes and create the database schema

# SQLite used by default — no additional configuration needed

# serialization — what & why

# created a BookSerializer using ModelSerializer
# this converts Book model instances to JSON and vice versa
# useful for validating input and formatting output for APIs

# views — function based views (FBV)

# created two views:
# 1. book_list → handles GET (list all books) and POST (add a new book)
# 2. book_detail → handles GET (retrieve), PUT (update), DELETE (remove) for a specific book

# used DRF's @api_view decorator and Response for clear API interaction

# urls setup

# defined URL patterns in books/urls.py for /books/ and /books/<int:pk>/
# included those routes in the main project's urls.py under /api/ path

# this exposes our API endpoints at:
# - /api/books/
# - /api/books/<id>/

# Git workflow

# initialized Git repo and added remote origin
# committed code changes
# resolved pull conflicts with --allow-unrelated-histories (if needed)
# pushed code to GitHub for version tracking and collaboration

# .gitignore usage

# created a .gitignore file to exclude:
# - virtual environments
# - migration files
# - SQLite database
# - system files
# - IDE/editor folders

# keeps the repo clean and avoids pushing unnecessary or sensitive data

# testing with Postman

# started development server: python manage.py runserver
# tested API endpoints using Postman with Content-Type: application/json

# operations tested:
# - GET     /api/books/             → list all books
# - POST    /api/books/             → create new book
# - GET     /api/books/<id>/        → retrieve a book by ID
# - PUT     /api/books/<id>/        → update a book by ID
# - DELETE  /api/books/<id>/        → delete a book by ID

# sample entries tested:
# - "Ichigo Doumei" by Mita Masahiro
# - "Story of Your Life" by Ted Chiang

# verified each action worked as expected, using proper request body format