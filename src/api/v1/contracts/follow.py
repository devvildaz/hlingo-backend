from typing import Union
from pydantic import BaseModel


class FollowPost(BaseModel):
    follower_id: str
    followed_id: str