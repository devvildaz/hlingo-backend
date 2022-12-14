import os
from datetime import datetime, timedelta
from typing import Union, Any
import jwt
from src.api.v1.contracts.auth import ClassicLoginUser
import codecs
from fastapi import FastAPI, Body, Depends

from src.core.settings import settings

from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = settings.jwt_secret  # should be kept secret
JWT_REFRESH_SECRET_KEY = settings.jwt_secret_refresh


def create_access_token(subject: ClassicLoginUser, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": subject.email}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return codecs.decode(encoded_jwt)

def create_refresh_token(subject: ClassicLoginUser, expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": subject.email}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return codecs.decode(encoded_jwt)

def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token if datetime.utcfromtimestamp(decoded_token["exp"]) >=  datetime.utcnow() else None
    except Exception:
        return {}
