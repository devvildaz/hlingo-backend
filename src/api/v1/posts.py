from hashlib import new
from src.api.v1.contracts.post import PostPost
from src.core.schemas.Post import Post
from fastapi import APIRouter
import json

posts_router = APIRouter(prefix="/v1")

@posts_router.get("/posts")
def get_posts():
    return json.loads(Post.objects().to_json())


@posts_router.get("/posts/search/{term}")
def search_post(term: str):
    if term is None:
        return {"message": "Search term can not be empty"}

    posts_found = Post.objects(title__icontains=term)

    return json.loads(posts_found.to_json())

@posts_router.post("/posts/create")
def post_lessons(post: PostPost):
    new_post = Post(
        title=post.title,
        description=post.content
    )
    new_post.save()
    return {"message": "Lesson saved successfully"}