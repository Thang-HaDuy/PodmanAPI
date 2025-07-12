from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_containers():
    response = client.get("/api/v1/containers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)