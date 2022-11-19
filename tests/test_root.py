from fastapi.testclient import TestClient
from dotenv import load_dotenv
from main import app

load_dotenv()
client = TestClient(app)

def test_root():
    res = client.get('/v1/')
    assert res.status_code  == 200
    assert res.json() == {'api_version': 'v1'}

