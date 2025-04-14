from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Model is running!"}

def test_predict():
    response = client.post("/predict", json={"data": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert "prediction" in response.json()
