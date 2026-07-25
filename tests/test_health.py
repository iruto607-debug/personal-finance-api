from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_read_users_returns_list():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_read_finances_returns_list():
    response = client.get("/finances")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
