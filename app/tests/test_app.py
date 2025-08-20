from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_positive():
    response = client.post("/predict", json={"text": "I love this!"})
    assert response.status_code == 200
    assert response.json()["prediction"] == "positive"

def test_predict_negative():
    response = client.post("/predict", json={"text": "I hate this!"})
    assert response.status_code == 200
    assert response.json()["prediction"] == "negative"
