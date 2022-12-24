from fastapi.testclient import TestClient
from unittest import TestCase
from dotenv import load_dotenv
from src.api.v1.contracts.auth import ClassicUserPost
from src.utils.token import *
import codecs


load_dotenv()

class TestToken(TestCase):
    test_user=ClassicUserPost(email="test@gmail.com",name="test_user",password="test_password")
    

    def test_create_token(self): 
        token = create_access_token(self.test_user)
        decoded_token=jwt.decode(codecs.encode(token),JWT_SECRET_KEY,algorithms=[ALGORITHM])
        assert self.test_user.email==decoded_token.get('sub')
