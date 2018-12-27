from peewee import *
from db import db

class BaseModel(Model):
	class Meta:
		database = db

class User(BaseModel):
	username = CharField()
	email = CharField(unique=True)
	age = IntegerField()
	

			