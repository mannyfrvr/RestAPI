from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Data model using Pydantic
class Person(BaseModel):
    id: int
    name: str
    age: int


# In-memory data store (replace with your database)
db = []


# The home page
@app.get("/")
def home_page():
    return "Welcome, page is running"


# Create a new person
@app.post("/api")
async def create_person(person: Person):
    db.append(person)
    return {"message": "Person created successfully"}


# Read a person by index (replace with database query)
@app.get("/api/{person_id}", response_model=Person)
async def read_person(person_id: int):
    if 0 <= person_id < len(db):
        return db[person_id]
    raise HTTPException(status_code=404, detail="Person not found")


# Update a person by index (replace with database query)
@app.put("/api/{person_id}")
async def update_person(person_id: int, updated_person: Person):
    if 0 <= person_id < len(db):
        db[person_id] = updated_person
        return {"message": "Person updated successfully"}
    raise HTTPException(status_code=404, detail="Person not found")


# Delete a person by index (replace with database query)
@app.delete("/api/{person_id}")
async def delete_person(person_id: int):
    if 0 <= person_id < len(db):
        deleted_person = db.pop(person_id)
        return {"message": "Person deleted successfully", "deleted_person": deleted_person}
    raise HTTPException(status_code=404, detail="Person not found")
