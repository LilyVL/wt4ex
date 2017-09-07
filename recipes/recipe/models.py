from django.db import models
from mongoengine import *	

# Create your models here.
class Recipe(models.Model):
	name = StringField(max_length=200)
	calories = IntField(default=0)
	ingredients = ListField()
	prep_time = DateTimeField()
	def __str__(self):
		return self.name

