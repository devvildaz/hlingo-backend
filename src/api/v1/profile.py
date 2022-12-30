from hashlib import new
from src.api.v1.contracts.follow import FollowPost
from src.core.schemas.AppUser import AppUser
from src.core.schemas.Follows import Follow
from fastapi import APIRouter
import json

profile_router = APIRouter(prefix="/v1")


@profile_router.get("/profile/followed_by/{follower_id}")
def get_followed_users(follower_id: str):
    if follower_id is None:
        return {"message": "Follower id not provided"}
        
    follows = Follow.objects(follower=follower_id)
    followed_users_id = map(lambda x: x.followed.id, follows)
    followed_users = AppUser.objects(id__in=followed_users_id)
    followed_users_info = [{'name': user.name, 'email': user.email, 'score': user.score} for user in followed_users]
    
    return followed_users_info


@profile_router.post("/profile/follow")
async def follow_user(follow: FollowPost):
    new_follow = Follow(
        follower=follow.follower_id,
        followed=follow.followed_id
    )
    new_follow.save()
    return {"message": "Now you have a new following!"}
