# RESTful API for Notes - README

## Introduction

This project is a secure and scalable RESTful API that allows users to m anage notes, share notes with other users, and search for notes based on keywords. It is built using the Django Rest Framework (DRF) and incorporates features such as user authentication, rate limiting, request throttling, share notes and search functionality.

# Choice of Framework/Database/Tools

## Framework

**Django Rest Framework (DRF)** is chosen as the primary framework for building the API due to its robust features, simplicity, and excellent support for building RESTful APIs in Django. <br/>
Also because of my love for Django! 💓

## Database

**PostgreSQL** is used as the database of choice due to its reliability, scalability, and support for complex queries. It is suitable for applications with high transaction rates and data integrity requirements.

Also, **Django's default Object-Relational Mapping (ORM)** system is designed to work with relational databases, making it a perfect pick.

For simplicity in installing and running in other node, I have kept **sqlite** as my db for now, which comes as default with Django

## Third-Party Tools

**djangorestframework-simplejwt**: Provides JSON Web Token (JWT) authentication for the API.

### Getting Started

**Prerequisites**<br/>
Python (>=3.8)<br/>
PostgreSQL

Libraries to be installed in python are listed in **requirements.txt**

## Installation

1. Clone repository
2. Navigate to the project directory
3. Create and activate a virtual environment
   ```powershell
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac
   source venv/bin/activate
   ```
4. Install dependency
   ```powershell
   pip install -r requirements.txt
   ```
5. Run migrations to create database tables
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Run Server
   ```
   python manage.py runserver
   ```

## API Endpoints

### Authentication Endpoints

1. **POST** /api/auth/signup/ : Create a new user account.
2. **POST** /api/auth/login/ : Log in to an existing user account and receive an access token.
3. **POST** /api/auth/refresh/ : Get new access token after the previous one has been expired

### Note Endpoints

1. **GET** /api/notes/ : Get a list of all notes for the authenticated user.
2. **GET** /api/notes/:id/ : Get a note by ID for the authenticated user.
3. **POST** /api/notes/ : Create a new note for the authenticated user.
4. **PUT**/**PATCH** /api/notes/:id/ : Update an existing note by ID for the authenticated user.
5. **DELETE** /api/notes/:id/ : Delete a note by ID for the authenticated user.
6. **POST** /api/notes/:id/share/ : Share a note with another user for the authenticated user.
7. **GET** /api/search?q=query : Search for notes based on keywords for the authenticated user.

## Performance

For better performance, I have implemented **rate limiting** and **request throttling** as well as **Pagination** to have less load on the database.
