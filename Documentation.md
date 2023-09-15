## Introduction

The "Person" API allows you to manage person records with basic CRUD operations: Create, Read, Update, and Delete. This documentation provides details on how to interact with the API.

## Endpoints

### Create a Person

- **URL:** `/api/`
- **Method:** `POST`
- **Request Format:**
  ```json
  {
    "name": "Damilola Boyewa",
    "age": 20
  }

## Response Format:
{
  "message": "Person created successfully"
}

## Read a Person
URL: /api/{person_id}
Method: GET
Response Format:

{
  "name": "Damilola Boyewa",
  "age": 20
}

## Update a Person
URL: /api/{person_id}
Method: PUT
Request Format:

{
  "name": "Damilola Boyewa",
  "age": 21
}

## Response Format:
{
  "message": "Person updated successfully"
}

## Delete a Person
URL: /api/{person_id}
Method: DELETE
Response Format:

{
  "message": "Person deleted successfully",
  "deleted_person": {
    "name": "Damilola Boyewa",
    "age": 21
  }
}

## Request and Response Formats
All requests and responses are in JSON format.
Ensure that the "name" field is a string, and the "age" field is an integer in the request payloads.

## Sample Usage
Here are some examples of how to use the API:

1. Create a Person:
   curl -X POST -H "Content-Type: application/json" -d '{"name": "ManuelRichard", "age": 20}' https://your-api-url.com/api/
2. Read a Person:
   curl https://your-api-url.com/api/1
3. Update a Person:
   curl -X PUT -H "Content-Type: application/json" -d '{"name": "ManuelRichard", "age": 21}' https://your-api-url.com/api/1
4. Delete a Person:
   curl -X DELETE https://your-api-url.com/api/1

Setting Up and Deploying the API
Follow these steps to set up and deploy the API:

## Clone the GitHub repository: https://github.com/mannyfrvr/RestAPI
Install the required dependencies by running pip install -r requirements.txt.
Configure your database connection in main.py.
Run the FastAPI application using uvicorn main:app --host 0.0.0.1 --port 8000 for local testing.
Deploy the application to a server or hosting platform of your choice for production use.
For more detailed setup instructions, refer to the README.md file in the repository.


