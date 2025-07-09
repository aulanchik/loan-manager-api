from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_apply_loan_success():
    res = client.post("/apply-loan", json={
        "loan_amount": 1000,
        "term": 12,
        "name": "Alice",
        "surname": "Smith",
        "personal_id": "1234567890"
    })
    assert res.status_code == 200
    assert res.json()["status"] == "approved"

def test_blacklisted_loan():
    res = client.post("/apply-loan", json={
        "loan_amount": 1000,
        "term": 12,
        "name": "Bob",
        "surname": "Brown",
        "personal_id": "0000000000"
    })
    assert res.status_code == 400

def test_get_loans():
    res = client.get("/loans")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_get_loans_by_user():
    res = client.get("/loans/1234567890")
    assert res.status_code == 200
