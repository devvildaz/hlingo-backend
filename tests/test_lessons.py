from fastapi.testclient import TestClient
from dotenv import load_dotenv
from main import app

load_dotenv()
client = TestClient(app)

def test_post_lesson():
    response = client.post(
        "/v1/lessons/create",
        json={"title":"prueba", "description":"prueba",
        "example_video":"elvidio", "category_name":"pruebas"},     
    )
    assert response.status_code == 201

def test_search_lesson():
    response = client.get(
        "/v1/lessons/search",
        json={"term":"prueba"},     
    )
    assert response.status_code == 200

def test_get_lesson():
    lesson_id = 0
    response = client.get(
        f"/v1/lessons{lesson_id}",
        json={"lesson_id":0},     
    )
    assert response.status_code == 200

def test_get_lessons():
    response = client.get("/v1/lessons")
    assert response.status_code == 200