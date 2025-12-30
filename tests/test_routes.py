import pytest
from app import create_app
from app.config import TestConfig

@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["message"] == "Hello, Flask!"


def test_health_route(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "OK"
