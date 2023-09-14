# Simple CRUD REST API

This is a simple REST API project for managing "person" resources, and providing basic CRUD operations. The project is built using Python and FastAPI and can be interfaced with any chosen database.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation and Setup](#installation-and-setup)
- [API Endpoints](#api-endpoints)
- [Sample Usage](#sample-usage)
- [UML Diagram](#uml-diagram)

## Project Overview

This project aims to create a simple REST API that allows you to perform the following CRUD operations on a "person" resource:

- CREATE: Add a new person
- READ: Fetch details of a person
- UPDATE: Modify details of an existing person
- DELETE: Remove a person

The API is built with Python and FastAPI, and it uses an in-memory data store for demonstration purposes (you can replace this with a real database).

## Installation and Setup

1. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt
   
3. Run the FastAPI application:
   uvicorn main:app --reload
The API will be accessible at http://localhost:8000.

## API Endpoints
POST /api: Create a new person
GET /api/{user_id}: Fetch details of a person by ID
PUT /api/{user_id}: Update details of an existing person by ID
DELETE /api/{user_id}: Remove a person by ID

## Sample Usage
Here are some sample API requests and responses:

Create a Person
POST /api
Content-Type: application/json

{
  "name": "Manuel Richard"
}
Response:
{
  "id": 1,
  "name": "Manuel Richard"
}

## Get a Person
GET /api/1

Response:
{
  "id": 1,
  "name": "Manuel Richard"
}

## Update a Person
PUT /api/1
Content-Type: application/json

{
  "name": "Damilola Boyewa"
}

Response:
{
  "id": 1,
  "name": "Damilola Boyewa"
}

## Delete a Person
DELETE /api/1

Response:
{
  "message": "Person deleted"
}
