from fastapi.testclient import TestClient
from unittest import TestCase
from main import app
from mongoengine import connect, disconnect



class TestAuth(TestCase):
    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest',host='mongomock://localhost')
    client = TestClient(app)
    @classmethod
    def tearDownClass(cls):
        disconnect()
    
    test_user={"name":"test","email":"test_email@gmail.com","password":"altacontra"}
    
    def test_register(self): 
        response = self.client.post(
            "/v1/register/email",
            json=self.test_user,     
        )
        assert response.status_code == 201
        assert response.json()["name"] == self.test_user["name"]
    
    def test_login(self):
        response = self.client.post(
            "/v1/login/email",
            json={"email":"test_email@gmail.com","password":"altacontra"},     
        )
        assert response.status_code == 200   
    
    def test_get_users(self):
        response = self.client.get(
            "/v1/user",
            json=self.test_user,     
        )
        assert response.status_code == 200

    def test_logout(self):
        response = self.client.post(
            "/v1/logout"
        )
        assert response.status_code == 200




