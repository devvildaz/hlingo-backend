from mongoengine import StringField, DateTimeField, Document
import datetime as dt

class Post(Document):
    title = StringField(required=True,max_length=75)
    content=StringField(max_length=500)
    createdAt=DateTimeField(default=dt.datetime.utcnow)