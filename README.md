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

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed.
- (Add any database-specific prerequisites if applicable)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/person-api.git
   cd person-api

2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt
   
4. Run the FastAPI application:
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
  "name": "Damilola Boyewa"
}
Response:
{
  "id": 0,
  "name": "Damilola Boyewa"
}

## Get a Person
GET /api/0

Response:
{
  "id": 0,
  "name": "Damilola Boyewa"
}

## Update a Person
PUT /api/0
Content-Type: application/json

{
  "name": "ManuelRichard"
}

Response:
{
  "id": 0,
  "name": "ManuelRichard"
}

## Delete a Person
DELETE /api/0

Response:
{
  "message": "Person deleted"
}


## UML Diagram

   +------------------+          +------------------------+
   |     Person       |          |   PersonRepository     |
   +------------------+          +------------------------+
   | - name: str      |          | + add_person()          |
   | - age: int       |--------->| + get_person()          |
   |                  |          | + update_person()       |
   | + create_person()|          | + delete_person()       |
   | + read_person()  |          +------------------------+
   | + update_person()|
   | + delete_person()|
   +------------------+


