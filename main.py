from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    id: int
    name: str
    age: int


persons = {
    1: Person(id=1, name="Damilola Boyewa", age=20),
    2: Person(id=2, name="Manuel Richard", age=20),
}


@app.get("/")
def home_page():
    return "Welcome, app is running"


@app.post("/api")
def create_person(person: Person):
    if person.id in persons:
        raise HTTPException(status_code=400, detail="Person already exists")

    # Additional validation for age (for example, age should be between 0 and 50)
    if not 0 <= person.age <= 50:
        raise HTTPException(status_code=400, detail="Invalid age")

    persons[person.id] = person
    return person


@app.get("/api/{user_id}")
def read_person(user_id: int):
    if user_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")
    return persons[user_id]


@app.put("/api/{user_id}")
def update_person(user_id: int, person: Person):
    if user_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")

    if person.id != user_id:
        raise HTTPException(status_code=400, detail="Person id mismatch")

    # Additional validation for age (for example, age should be between 0 and 50)
    if not 0 <= person.age <= 50:
        raise HTTPException(status_code=400, detail="Invalid age")

    persons[user_id] = person
    return person


@app.delete("/api/{user_id}")
def delete_person(user_id: int):
    if user_id not in persons:
        raise HTTPException(status_code=404, detail="Person not found")
    del persons[user_id]
    return {"message": "Person deleted successfully"}
