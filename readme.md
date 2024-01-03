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
   ```powershell
   python manage.py runserver
   ```
7. Seed Database with random notes and 2 users
   ```powershell
   python manage.py seed_db <num_notes>
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
6. **POST** /api/notes/:id/share/ : Share a note with another user for the authenticated user. (cannot share note with self)
7. **GET** /api/notes/search?q=query : Search for notes based on keywords for the authenticated user.

## Performance

For better performance, I have implemented **rate limiting** and **request throttling** as well as **Pagination** to have less load on the database.

## Images
### Authentication Endpoints
1. **POST** /api/auth/signup/ : Create a new user account.
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/112c55f5-8947-44e9-a84c-47845263476b)
2. **POST** /api/auth/login/ : Log in to an existing user account and receive an access token.
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/b6d4ab17-67cf-4988-b767-3640b28300e5)
3. **POST** /api/auth/refresh/ : Get new access token after the previous one has been expired
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/1415e623-8ae8-49de-ae6e-e879035906a2)

### Note Endpoints
1. **GET** /api/notes/ : Get a list of all notes for the authenticated user. (with pagination)
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/81627d15-6892-4db1-b898-15f68ebaea67)
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/4e1aba46-02b4-4721-a7a4-611f1c3f7af8)

2. **GET** /api/notes/:id/ : Get a note by ID for the authenticated user.
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/9784fa07-33e5-44b3-9576-3d875421aefb)

3. **POST** /api/notes/ : Create a new note for the authenticated user.
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/3a65ad07-7897-483b-bba8-f65f0e8da53c)

4. **PUT**/**PATCH** /api/notes/:id/ : Update an existing note by ID for the authenticated user.
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/8fb7dae6-6859-4631-853e-6e8d0bf8c6ce)

5. **DELETE** /api/notes/:id/ : Delete a note by ID for the authenticated user.
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/d49970a9-82d5-42fe-b0b0-66bcc2ae12c5)

6. **POST** /api/notes/:id/share/ : Share a note with another user for the authenticated user.
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/1613efc7-5813-4780-a006-2d56a6c4254f)

7. **GET** /api/notes/search?q=query : Search for notes based on keywords for the authenticated user.
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/392b886b-91eb-469e-8386-8bc724986099)



## For Security and Performance:
1. Access Token Expired:
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/80e4effa-c10d-48af-a3c6-0d4ba309bff2)
2. Rate Limiting:
   ![image](https://github.com/abhaybabbar/speer_assessment_backend/assets/65766449/ca826754-dd58-4e9c-81b5-8312e5a2d63d)

3. Pagination Shown above in note endpoints 1.
