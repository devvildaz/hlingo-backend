from typing import Union
from pydantic import BaseModel


class ClassicUserPost(BaseModel):
    name: str
    password: str
    email: str

class ClassicLoginUser(BaseModel):
    email: str
    password: str
    
class ModifyUserPost(BaseModel):
    id: str
    name: str
    email: str
    score: float
