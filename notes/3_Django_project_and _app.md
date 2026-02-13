# Django Project vs App - Notes

# 1. Django Project
A project is the entire web application configuration.
It’s essentially the container that holds all apps, settings, and configurations for your website.
When you create a project using:
django-admin startproject <project_name> .


# 2. Django App
An app is a modular component of a project that performs a specific function.
Think of an app as a smaller web application that can be reused in multiple projects.
When you create an app using:
django-admin startapp <app_name>


## 1. Django Project Files

**Created by:** `django-admin startproject projectname`

```
projectname/
    manage.py
    projectname/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
```

### manage.py

* Command-line utility to manage the project.
* Used to run server, make/apply migrations, create apps, etc.

### **init**.py

* Marks the folder as a Python package.
* Usually empty.

### settings.py

* Global project configuration.
* Contains installed apps, database setup, middleware, templates, static files, debug mode.

### urls.py

* Project-level URL routing.
* Maps URLs to views or app URLs.

### wsgi.py

* WSGI entry point for deployment.
* Handles synchronous requests on servers like Gunicorn or Apache.

### asgi.py

* ASGI entry point for asynchronous deployment.
* Handles async requests like WebSockets.

---

## 2. Django App Files

**Created by:** `python manage.py startapp appname`

```
appname/
    __init__.py
    admin.py
    apps.py
    models.py
    views.py
    tests.py
    migrations/
```

### **init**.py

* Marks the folder as a Python package.
* Usually empty.

### admin.py

* Register models for the Django admin panel.
* Enables management of database models via admin interface.

### apps.py

* App configuration.
* Defines app-specific settings or signals.

### models.py

* Define database tables as Python classes.
* Each model represents a database table.

### views.py

* Contains functions or classes to handle requests.
* Returns responses (HTML, JSON, etc.) to users.

### tests.py

* Write unit tests for the app.
* Ensures app behaves correctly.

### migrations/

* Stores database migration files.
* Tracks changes to models and applies them to the database.

### Optional: urls.py

* App-level URL routing.
* Maps app-specific URLs to views.

---

### Summary Table

| File        | Project/App | Purpose                         |
| ----------- | ----------- | ------------------------------- |
| manage.py   | Project     | CLI tool to manage project      |
| settings.py | Project     | Global configuration            |
| urls.py     | Project/App | Map URLs to views               |
| wsgi.py     | Project     | Deployment interface (sync)     |
| asgi.py     | Project     | Deployment interface (async)    |
| **init**.py | Both        | Marks folder as Python package  |
| admin.py    | App         | Register models for admin panel |
| apps.py     | App         | App configuration               |
| models.py   | App         | Database tables                 |
| views.py    | App         | Request handling logic          |
| tests.py    | App         | Unit testing                    |
| migrations/ | App         | Database migration tracking     |
