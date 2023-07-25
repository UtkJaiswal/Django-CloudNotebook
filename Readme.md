# Cloud Notebook

This project implements a simple API for managing notes, where authenticated users can create, view, update, and delete their own notes. The API is built using Django REST Framework, which provides powerful tools for building web APIs.

## Setup

    -   Clone the repository to your local machine:

        ```bash
        git clone Django-CloudNotebook
        cd Django-CloudNotebook
        ```

    -   Create a virtual environment (optional but recommended) and activate it:

        ```bash
        python -m venv venv
        source venv/bin/activate   # On Windows: venv\Scripts\activate
        ```

    -   Install the required dependencies:

        ```bash
        pip install -r requirements.txt
        ```

    -   Apply the database migrations to create the necessary database tables:

        ```bash
        python manage.py migrate
        ```

    -   Create a superuser to access the Django admin interface (optional but useful for managing users and notes):

        ```bash
        python manage.py createsuperuser
        ```

    -   Start the development server:

        ```bash
        python manage.py runserver
        ```

    -   The API will be accessible at http://localhost:8000/

## Endpoints

### User Registration

    -   Endpoint: /users/
    -   Method: POST
    -   Description: Register a new user by providing a username, password, and optional notes. Only authenticated users can access this endpoint. The user will be associated with the notes they create.

### User Detail

    -   Endpoint: /users/<int:pk>/
    -   Method: GET, PUT, PATCH, DELETE
    -   Description: Retrieve, update, or delete a specific user. Only authenticated users can access this endpoint. Users can view their own details, but updating or deleting a user is restricted to the user themselves.

### User Login

    -   Endpoint: /users/login/
    -   Method: POST
    -   Description: Authenticate a user by providing their username and password. If the credentials are valid, the user will be logged in and receive an authentication token.

### NoteList

    -   Endpoint: /notes/
    -   Method: GET, POST
    -   Description: Retrieve a list of notes or create a new note. Only authenticated users can access this endpoint. Users can view only their own notes and create new notes associated with their account.

### Note Detail

    -   Endpoint: /notes/<int:pk>/
    -   Method: GET, PUT, PATCH, DELETE
    -   Description: Retrieve, update, or delete a specific note. Only authenticated users can access this endpoint. Users can view, update, or delete only the notes they created.


