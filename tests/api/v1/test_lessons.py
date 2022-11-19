from fastapi.testclient import TestClient
from main import app
from unittest import TestCase
from mongoengine import connect, disconnect

class TestLessons(TestCase):
    
    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest',host='mongomock://localhost')
    client = TestClient(app)
    @classmethod
    def tearDownClass(cls):
        disconnect()
    client = TestClient(app)

    def test_post_lesson(self):
        response = self.client.post(
            "/v1/lessons/create",
            json={"title":"prueba", "description":"prueba",
            "example_video":"elvidio", "category_name":"pruebas"},     
        )
        assert response.status_code == 200

    def test_search_lesson(self):
        response = self.client.get(
            "/v1/lessons/search",
            json={"term":"prueba"},     
        )
        assert response.status_code == 200

    def test_get_lesson(self):
        lesson_id = 0
        response = self.client.get(
            f"/v1/lessons{lesson_id}",
            json={"lesson_id":0},     
        )
        assert response.status_code == 200

    def test_get_lessons(self):
        response = self.client.get("/v1/lessons")
        assert response.status_code == 200

