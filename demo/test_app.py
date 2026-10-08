from fastapi.testclient import TestClient
from app import app, accounts, domains

client = TestClient(app)

def setup_function():
    accounts.clear()
    domains.clear()

def test_domain_ownership_and_uniqueness():
    a = client.post("/accounts", json={"customer": "Ada", "plan": "Pro"}).json()
    payload = {"name": "Example.cl", "account_id": a["id"]}
    assert client.post("/domains", json=payload).status_code == 201
    assert client.post("/domains", json=payload).status_code == 409
    assert client.get(f'/accounts/{a["id"]}/domains').json() == [
        {"name": "example.cl", "account_id": a["id"]}
    ]

def test_missing_account():
    assert client.post("/domains", json={"name":"x.cl","account_id":999}).status_code == 404
