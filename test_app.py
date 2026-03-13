import json
from app import app

client = app.test_client()

def test_home():
    response = client.get('/')
    assert response.status_code == 200

def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "healthy"

def test_add_member():
    response = client.post(
        '/members',
        json={
            "name": "Rahul",
            "membership": "Gold"
        }
    )
    assert response.status_code == 201

def test_get_members():
    response = client.get('/members')
    assert response.status_code == 200