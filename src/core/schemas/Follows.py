from mongoengine import ReferenceField, Document
import datetime as dt

from src.core.schemas.AppUser import AppUser

class Follow(Document):
    follower= ReferenceField(AppUser)
    followed = ReferenceField(AppUser)