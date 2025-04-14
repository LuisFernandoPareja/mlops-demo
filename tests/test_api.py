from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200

def test_predict():
    r = client.post("/predict", json=[5.1, 3.5, 1.4, 0.2])
    assert r.status_code == 200
    assert "prediction" in r.json()
