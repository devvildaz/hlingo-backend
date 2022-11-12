from typing import Union
from unicodedata import category, name
from pydantic import BaseModel


class LessonPost(BaseModel):
    title: str
    description: str
    example_video: str
    category_name: str

class GradeDTO(BaseModel):
    user_id: str
    lesson_id: str
    grade: float
    completed:bool