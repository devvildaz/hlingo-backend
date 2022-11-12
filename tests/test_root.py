from fastapi.testclient import TestClient
from dotenv import load_dotenv
from main import app

load_dotenv()
client = TestClient(app)

def test_root():
    res = client.get('/v1/')
    assert res.status_code  == 200
    assert res.json() == {'api_version': 'v1'}

def test_register():
    response = client.post(
        "/v1/register/email",
        json={"name":"test","email":"test_email@gmail.com","password":"altacontra"},     
    )
    assert response.status_code == 201
    assert response.json == {
        "name":"test","email":"test_email@gmail.com", "issuer":"localhost"
    }

def test_login():
    response = client.post(
        "/v1/login/email",
        json={"email":"test_email@gmail.com","password":"altacontra"},     
    )
    assert response.status_code == 200
    assert response.json["email"] == "test_email@gmail.com"

def test_logout():
    response = client.post(
        "/v1/logout"
    )
    assert response.status_code == 200
