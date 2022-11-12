from hashlib import new
from src.api.v1.contracts.lesson import *
from src.core.schemas.Lessons import *
from fastapi import APIRouter
import json

lessons_router = APIRouter(prefix="/v1")

@lessons_router.get('/lessons/search')
def search_lesson(term: str):
    if term is None:
        return {
            "message": "Search term can not be empty"
        }

    lessons_found = Lesson.objects(title__icontains=term)

    return json.loads(lessons_found.to_json())


@lessons_router.get('/lessons')
def get_lessons():
    return json.loads(Lesson.objects().to_json())


@lessons_router.get('/lessons{lesson_id}')
def get_lesson_by_id(lesson_id: str):
    try:
        lesson_found = Lesson.objects(id=lesson_id).first()
    except:
        return {
            "message": f"{lesson_id} is not a valid id"
        }

    if not lesson_found:
        return {
            "message": f"Lesson with id {lesson_id} not found"
        }

    return json.loads(lesson_found.to_json())


@lessons_router.post('/lessons/create')
async def post_lessons(lesson: LessonPost):
    new_lesson = Lesson(title=lesson.title, description=lesson.description,
                        example_video=lesson.example_video, category_name=lesson.category_name)
    new_lesson.save()
    return {
        'message': "Lesson saved successfully"
    }

@lessons_router.post('/lessons/grade')
async def post_grade(grade:GradeDTO):
    new_grade=Grade(user_id=grade.user_id,lesson_id=grade.lesson_id,grade=grade.grade,completed=grade.completed)
    new_grade.save()
    return{
        'message':'Grade saved successfully'
    }

@lessons_router.get('/lessons/grade')
async def get_grades():
    grades=Grade.objects().to_json()
    return json.loads(grades)

@lessons_router.get('/lessons/grade')
async def get_grade_by_user_id_lesson_id(user_id:str,lesson_id:str):
    try:
        grade_found=Grade.objects(user_id=user_id,lesson_id=lesson_id).first()
    except:
        return {
            "message": f"{user_id} or {lesson_id} is not a valid id"
        }
    if not grade_found:
        return{
            "message": f"{user_id} or {lesson_id} not found"
        }
    return json.loads(grade_found.to_json())