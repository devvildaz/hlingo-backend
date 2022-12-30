from pydantic import BaseModel

class PostPost(BaseModel):
    title: str
    content: str