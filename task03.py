# virtual environment
# it helps isolate dependencies per project
# without it, all packages are installed globally
# this can break other projects if versions clash

# how to use it:
# python -m venv env         # create virtual environment
# source env/bin/activate    # activate (Linux/mac)
# env\Scripts\activate       # activate (Windows)
# deactivate                 # turn off

# django
# high-level web framework written in Python
# helps build secure, maintainable web applications fast
# uses MVT (Model View Template) architecture

# django vs django rest framework (drf)
# django -> full-stack framework (views, forms, templates)
# drf -> toolset to build RESTful APIs using Django
# focuses on serialization, authentication, and HTTP verbs (GET, POST, etc.)

# django architecture
# MVT:
# Model: defines the data (like tables in DB)
# View: handles business logic and connects model and template
# Template: the front-end HTML returned to user

# code flow
# request -> URL dispatcher -> view function -> model/template -> response

# request-response cycle
# 1. user sends a request (usually via browser)
# 2. Django matches the URL pattern
# 3. corresponding view function is called
# 4. view may use models to access data
# 5. result is passed to template for rendering (if HTML)
# 6. response is sent back to user

# django project vs django app
# project: full website, includes settings, URLs, and apps
# app: a component/module inside a project, like "blog" or "accounts"

# file structure (main project folder)
# manage.py            -> command-line utility
# projectname/
# ├── __init__.py
# ├── settings.py      -> all settings
# ├── urls.py          -> maps URLs to views
# ├── asgi.py / wsgi.py -> for deployment
# appname/
# ├── admin.py         -> admin interface
# ├── apps.py          -> config
# ├── models.py        -> database tables
# ├── views.py         -> request logic
# ├── serializers.py   -> for DRF (manual)
# ├── urls.py          -> app-level routes
# ├── templates/       -> HTML files
# ├── static/          -> CSS, JS, etc.

# admin panel
# built-in Django backend to manage models visually
# how to use:
# 1. register models in admin.py
# 2. create superuser -> python manage.py createsuperuser
# 3. login at /admin

# RESTful API
# architectural style for designing networked applications
# uses HTTP methods to perform CRUD

# HTTP methods used in DRF:
# GET -> retrieve data
# POST -> create data
# PUT -> replace (update) entire object
# PATCH -> partially update object
# DELETE -> remove object

# DRF example:
# create a serializer class to convert model to JSON
# create viewsets or APIView classes to handle requests
# connect them with routers in urls.py