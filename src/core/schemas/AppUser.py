from email.policy import default
from tokenize import Floatnumber
from mongoengine import StringField, DateTimeField, FloatField, Document
import datetime as dt
from passlib.hash import pbkdf2_sha256

class AppUser(Document):
    name = StringField(required=True,max_length=128)
    password = StringField(required=True)
    issuer=StringField(required=True,max_length=256)
    email=StringField(required=True, max_length=128, unique=True)
    role=StringField(requierd=True,max_length=128,default="user")
    createdAt=DateTimeField(default=dt.datetime.utcnow)
    updatedAt=DateTimeField(default=dt.datetime.utcnow)
    score=FloatField(default=0.0)

    def update(self, *args, **kwargs):
        super(AppUser, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.password = pbkdf2_sha256.hash(self.password)
        super(AppUser, self).save(*args, **kwargs)
        
    def val_password(self, out_password: str):
        return pbkdf2_sha256.verify(out_password, self.password)