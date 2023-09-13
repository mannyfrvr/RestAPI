import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_person():
    new_person = {
        "id": 3,
        "name": "Abimbola Boyewa",
        "age": 46
    }
    response = client.post("/api", json=new_person)
    assert response.status_code == 200
    assert response.json() == new_person


def test_read_person():
    response = client.get("/api/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Damilola Boyewa",
        "age": 20
    }


def test_update_person():
    updated_person = {
        "id": 1,
        "name": "Olamilekan",
        "age": 25
    }
    response = client.put("/api/1", json=updated_person)
    assert response.status_code == 200
    assert response.json() == updated_person


def test_delete_person():
    response = client.delete("/api/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Person deleted successfully"}


def test_person_not_found():
    response = client.get("/api/100")
    assert response.status_code == 404
